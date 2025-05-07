import 'bootstrap-icons/font/bootstrap-icons.css';
import React from 'react';
import './PostAuthNavbar.css';
import { useNavigate } from 'react-router-dom';

const PostAuthNavbar = () => {
  const navigate = useNavigate();

  const goToHome = () => navigate('/home');
  const goToSearch = () => navigate('/search'); 
  const goToMap = () => navigate('/map'); 
  const goToSettings = () => navigate('/settings'); 
  // const goToLLM = () => navigate('/llm');
  const goToLLM = () => window.open('https://localhost:8501', '_blank');

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
        <button className="post-auth-navbar-button" onClick={goToHome} title="Feed">
          Feed
        </button>
        <button className="post-auth-navbar-button" onClick={goToMap} title="Map">
          Map
        </button>
        <button className="post-auth-navbar-button" onClick={goToSearch} title="Search">
          Search
        </button>
        <button className="post-auth-navbar-button" onClick={goToLLM} title="SumerAI">
          SumerAI
        </button>
        <button className="post-auth-navbar-button" onClick={goToSettings} title="Settings">
          Settings
        </button>
      </div>
    </div>
  );
};

export default PostAuthNavbar;