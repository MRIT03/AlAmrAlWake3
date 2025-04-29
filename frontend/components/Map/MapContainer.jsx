// src/components/MapContainer.jsx
import { MapContainer as LeafletMap, TileLayer, Marker, Popup, Tooltip } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import markerIcon2x from 'leaflet/dist/images/marker-icon-2x.png';
import markerIcon from 'leaflet/dist/images/marker-icon.png';
import markerShadow from 'leaflet/dist/images/marker-shadow.png';
import './MapContainer.css'; 

// Fix for default marker icons
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: markerIcon2x,
  iconUrl: markerIcon,
  shadowUrl: markerShadow,
});

const MapContainer = ({ newsByLoc, center=[33.8547, 35.8623], zoom=8, onMarkerClick }) => {    

    const handleClick = (loc) => {
        console.log(`Clicked on ${loc.city}`);
        onMarkerClick?.(loc);
    };
      

  return (
    <div className="map-wrapper">
      <LeafletMap center={center} zoom={zoom} scrollWheelZoom={true} style={{ height: '100%', width: '100%' }}>
        <TileLayer
          
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        
        {newsByLoc.map((loc, idx) => {
            // const popupRef = useRef();

            return (
                <Marker
                className='map-marker'
                key={idx} // the indx of the currently processed location 
                position={loc.coords} 
                eventHandlers={{
                    click: () => handleClick(loc), 
                  }}
                >
                    <Tooltip direction="top" offset={[-15, -10]} opacity={1} permanent={false}> {/* offset to the left, up */}
                        {`${loc.city} (${loc.headlines.length})`}
                    </Tooltip>
                </Marker>
            );
        })}

      </LeafletMap>
    </div>
  );
};

export default MapContainer;
