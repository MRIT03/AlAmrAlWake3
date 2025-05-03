import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './SettingsPage.css'; 

import PostAuthNavbar from '../Navigation/PostAuthNavbar';
import SettingsPanel from './SettingsPanel';
import OutletCard from '../Misc/OutletCard';

const SettingsPage = () => {
  const [username, setUsername] = useState('');
  const [ressourcesFollowed, setRessourcesFollowed] = useState([]);

  useEffect(() => {
    // Fetch username
    axios.get("http://localhost:5120/getusername")
      .then(response => {
        setUsername(response.data.username); // Update to the real name of the route, queryName is fetch_username
      })
      .catch(error => {
        console.error("Error fetching username:", error);
      });

    // Fetch outlets
    axios.get("http://localhost:5120/getOutlets") // Update to the real name of the route, queryName is fetch_followed_sources
      .then(response => {
        setRessourcesFollowed(response.data); // expecting array of outlet objects
      })
      .catch(error => {
        console.error("Error fetching outlets:", error);
      });
  }, []);

  return (
    <div className='settings-page-wrapper'>
      <PostAuthNavbar />
      <SettingsPanel givenUsername={username} />

      {/* Outlet Cards for followed resources */}
      {ressourcesFollowed.map(outlet => (
        <OutletCard
          key={outlet.id}
          sourceName={outlet.sourceName}
          SRR={outlet.SRR}
          followingStatus={outlet.followingStatus}
        />
      ))}
    </div>
  );
};

export default SettingsPage;
