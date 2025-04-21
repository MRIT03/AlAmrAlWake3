import 'bootstrap-icons/font/bootstrap-icons.css';
import React from 'react'; 
import './LandingPage.css';
import PreAuthNavbar from '../Navigation/PreAuthNavbar';
import { useNavigate } from 'react-router-dom';

const LandingPage = () => {

   const navigate = useNavigate();
   const goToSignup = () => navigate('/home'); // EDIT LATER

  return (
    <div className='landing-page-wrapper'>
        <PreAuthNavbar />
        <div className="landing-page-content">
            <h1 className="landing-title primary-blue">Stay Informed.</h1>
            <h2 className="landing-subtitle secondary-blue">Curated News, Tailored for You.</h2>

            <p className="landing-description">
                Discover headlines from the most trusted sources, rated for reliability and personalized to your interests.
            </p>

            <button className="get-started-btn" onClick={goToSignup}>
                <i className="bi bi-box-arrow-in-right" style={{ marginRight: '0.5rem' }}></i>
                Skip Login To Feed
            </button>
        </div>
    </div>
  );
};

export default LandingPage;
