import React from 'react';
import './MapSideBar.css'; 

const MapSideBar = ({ newsByLoc = [], onHeadlineClick = () => {} }) => {
  return (
    <div className="map-sidebar">
      <h3 className='map-sidebar-title'>📰 Latest News by Location</h3>
      <div className="headline-list">
        {newsByLoc.map((loc, index) => (
          <div key={index} className="city-headlines">
            <h3>{loc.city}</h3>
            <ul>
              {loc.headlines.map((headline, i) => (
                <li key={i} onClick={() => onHeadlineClick(loc, headline)}>
                  {headline}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MapSideBar;