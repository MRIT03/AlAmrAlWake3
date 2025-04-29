import React, {useState} from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './SettingsPage.css'; 

import SettingsInputField from './SettingsInputField';
import PostAuthNavbar from '../Navigation/PostAuthNavbar';
import SettingsPanel from './SettingsPanel';

const SettingsPage = ({ username="its.nourr"}) => { 

  // useEffect(() => { // Fetch USERNAME
  //   axios.get("http://localhost:4000/posts") // TO-DO Query #8 + Change Port Number
  //     .then(response => {
  //       setPosts(response.data);
  //     })
  //     .catch(error => {
  //       console.error("Error fetching posts:", error);
  //     })
  // }, []);

        return (
        <div className='settings-page-wrapper'>

            <PostAuthNavbar/>
            <SettingsPanel givenUsername={username} />

        </div>    
  );
};

export default SettingsPage;
