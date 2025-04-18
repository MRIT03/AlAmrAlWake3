import React, {useState} from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './SettingsPage.css'; 

import SettingsInputField from './SettingsInputField';
import PostAuthNavbar from '../Navigation/PostAuthNavbar';
import SettingsPanel from './SettingsPanel';

const SettingsPage = ({ username="its.nourr"}) => { 

        return (
        <div className='settings-page-wrapper'>

            <PostAuthNavbar/>
            <SettingsPanel givenUsername={username} />

        </div>    
  );
};

export default SettingsPage;
