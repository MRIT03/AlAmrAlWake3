import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap-icons/font/bootstrap-icons.css';
import AuthField from './AuthField';
import './LoginForm.css';
import { useNavigate } from 'react-router-dom';

const AdminLoginForm = () => {
    
  const [loginText, setLoginText] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  const handleLoginTextInput = (e) => setLoginText(e.target.value);
  const handlePasswordInput = (e) => setPassword(e.target.value);

  // Buttons Configuration
  const authenticateLogin = async () => {
    try {
      const formData = new FormData();
      formData.append("Username", loginText);
      formData.append("Password", password);
      formData.append("UserRole", "Admin");
  
      const response = await axios.post('http://localhost:5120/api/User/Login', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        withCredentials: true,
      });
  
      console.log('Login successful. Redirecting...');
      navigate('/home');
    } catch (error) {
      if (error.response && error.response.data) {
        setErrorMessage(error.response.data);
      } else {
        setErrorMessage("Something went wrong. Please try again.");
      }
      setPassword("");
    }
  };  

  const forgotPassword = () => {
    console.log('Redirecting to the password reset page...');
  };

  const backToLanding = () => navigate('/');

  return ( 
    <div className='overall-container login'>
        <div className='back-button-container login'>
          <button className='login-back-button' title='Back' onClick={backToLanding}>← Back to Main</button>
        </div>
        <h1 className='welcome-message-login'>Welcome back to <span className='login-span'>khabar</span>.lb</h1>
        {/* <h4 className='login-intro-message'>Latest Lebanese news in one place!</h4> */}
        <div className="inputfields-container">
              <AuthField type={"text"} placeholder={"Username or email address"} value={loginText} onChange={handleLoginTextInput}/>
              <AuthField type={"password"} placeholder={"Enter your password"} value={password} onChange={handlePasswordInput}/>
        </div>
        {errorMessage && (
          <div className="error-message">
            <i className="bi bi-exclamation-circle"></i> {errorMessage}
          </div>
        )}
        <button className='authenticate-button' type="authenticate" onClick={authenticateLogin}>Authenticate</button>
        <p className='forgot-password'>Forgot your password? &nbsp;
            <span onClick={forgotPassword} title="Reset Password" style={{ textDecoration: 'underline', cursor: 'pointer'}}>Click Here</span>
        </p>
    </div>
  );
};

export default AdminLoginForm;
