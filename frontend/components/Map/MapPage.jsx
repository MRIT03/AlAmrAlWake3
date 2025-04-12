import React, { useState } from 'react';
import MapContainer from './MapContainer';
import MapSideBar from './MapSideBar';

const newsByLoc = [
  {
    city: 'Beirut',
    coords: [33.8938, 35.5018],
    headlines: ['Protests indeed continue and continue to continue to continue to Continue', 'Downtown Explosion']
  },
  {
    city: 'Tripoli',
    coords: [34.4381, 35.8308],
    headlines: ['Port Expansion', 'Archaeological Discovery', 'Electricity Cut']
  },
  {
    city: 'Tyre',
    coords: [33.2700, 35.2033],
    headlines: ['Beach Cleanup', 'Ancient Ruins Discovered']
  },
  {
    city: 'Sidon',
    coords: [33.5606, 35.3750],
    headlines: ['Festival Announced']
  },
  {
    city: 'Zahle',
    coords: [33.8947, 35.8623],
    headlines: ['Ceasefire', 'New Parliament', 'Municipality Elections']
  },
  {
    city: 'Baalbek',
    coords: [34.0058, 36.2181],
    headlines: ['Temple Restoration', 'Cultural Week', 'Water Shortage']
  },
  {
    city: 'Jounieh',
    coords: [33.9808, 35.6171],
    headlines: ['Concert Series', 'Traffic Reroute']
  },
  {
    city: 'Aley',
    coords: [33.8106, 35.5972],
    headlines: ['Fire Near Forest', 'School Renovation']
  },
  {
    city: 'Nabatieh',
    coords: [33.3772, 35.4836],
    headlines: ['New Hospital Opens']
  },
  {
    city: 'Byblos',
    coords: [34.1230, 35.6519],
    headlines: ['Tourist Boom', 'Harbor Restoration', 'Local Elections', 'Heritage Festival']
  }
];

const MapPage = () => {

  const [selectedLoc, setSelectedLoc] = useState(null);

  const handleMarkerClick = (loc) => {
    setSelectedLoc(loc);
  };

  const filteredNews = selectedLoc ? [selectedLoc] : newsByLoc;

  return (
    <div style={{ display: 'flex' }}>
    {/* <div> */}
      <MapContainer newsByLoc={newsByLoc} center={[33.8547, 35.8623]} zoom={8} onMarkerClick={handleMarkerClick}/> {/* centered at lebanon*/}
      <MapSideBar newsByLoc={filteredNews} />
    </div>
  );
};

export default MapPage;
