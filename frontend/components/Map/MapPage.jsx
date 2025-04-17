import React, { useState } from 'react';
import MapContainer from './MapContainer';
import MapSideBar from './MapSideBar';
import PostAuthNavbar from '../Navigation/PostAuthNavbar';
import './MapPage.css';
import MapView from './MapView';

const MapPage = () => {

  return (
    <div>
      <PostAuthNavbar />
      <div className='map-view-wrapper'>
        <MapView />
      </div>
    </div>
  );
};

export default MapPage;
