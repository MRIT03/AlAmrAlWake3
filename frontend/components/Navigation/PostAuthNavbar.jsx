import 'bootstrap-icons/font/bootstrap-icons.css';
import React from 'react';
import './PostAuthNavbar.css';
import { useNavigate } from 'react-router-dom';

const PostAuthNavbar = () => {
  const navigate = useNavigate();

  const goToHome = () => navigate('/'); // FeedPage route
  const goToFeed = () => navigate('/'); // This is assuming FeedPage is at '/'
  const goToSearch = () => navigate('/search'); // Assuming search page is at '/search'
  const goToMap = () => navigate('/map'); // Assuming map page is at '/map'
  const goToSettings = () => navigate('/settings'); // Assuming settings page is at '/settings'

  return (
    <div className="navbar-container">
      <div className="logo-container">
        <img
          src="/navbar-logo-khabar.png"
          alt="Logo"
          className="navlogo"
          onClick={goToHome}
          title="Back to Home"
        />
      </div>
      <div className="post-auth-navbar-links">
        <button className="post-auth-navbar-button" onClick={goToFeed} title="Feed">
          Feed
        </button>
        <button className="post-auth-navbar-button" onClick={goToMap} title="Map">
          Map
        </button>
        <button className="post-auth-navbar-button" onClick={goToSearch} title="Search">
          Search
        </button>
        <button className="post-auth-navbar-button" onClick={goToSettings} title="Settings">
          Settings
        </button>
      </div>
    </div>
  );
};

export default PostAuthNavbar;