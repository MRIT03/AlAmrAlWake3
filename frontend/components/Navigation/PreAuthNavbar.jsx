import 'bootstrap-icons/font/bootstrap-icons.css';
import React from 'react'; 
import './PreAuthNavbar.css';
import { useNavigate } from 'react-router-dom';

const PreAuthNavbar = () => {

    const navigate = useNavigate();

    const goToLogin = () => navigate('/login');
    const goToSignup = () => navigate('/signup');

  return (
    <div className='navbar-container'>
        <div className='logo-container'>
          <img
            src="/navbar-logo-khabar.png"
            alt="Logo"
            className="navlogo"
            onClick={null}
            title="Back to Home"
          />
        </div>
        <div className='pre-auth-pages-links'>
            <button className='pre-auth-navbar-button' onClick={goToLogin} title='Login'>Log in</button>
            <button className='signup-button' onClick={goToSignup} title='Signup'>Sign up</button>
        </div> 
    </div>
  );
};

export default PreAuthNavbar;
