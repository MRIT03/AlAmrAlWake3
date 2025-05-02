import React, { useState } from 'react';
import 'bootstrap-icons/font/bootstrap-icons.css';
import AuthField from './AuthField';
import './SignupForm.css'; 
import { useNavigate } from 'react-router-dom';
 
const AdminSingupForm = ({ }) => {
    
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [checkPassword, setCheckPassword] = useState("");

  const handleUsernameInput = (e) => setUsername(e.target.value);
  const handleEmailInput = (e) => setEmail(e.target.value);
  const handlePasswordInput = (e) => setPassword(e.target.value);
  const handlePasswordCheckInput = (e) => setCheckPassword(e.target.value);
  const [error, setError] = useState(""); 
  const [loading, setLoading] = useState(false); 
  const navigate = useNavigate();

  // Buttons Configuration
  const submitSignup = async () => {
    // Check if passwords match
    if (password !== checkPassword) {
      setError("Passwords do not match.");
      return;
    }
  
    try {
      setLoading(true);
      setError(""); // Clear any previous error
  
      // Create FormData to match [FromForm] binding in .NET
      const formData = new FormData();
      formData.append("UserName", username);
      formData.append("EmailAddress", email);
      formData.append("Password", password);
      formData.append("UserRole", "User");  // Indicate that this is not an admin
  
      // Send POST request to .NET back-end
      const response = await fetch('http://localhost:5120/api/User/SignUp', {
        method: 'POST',
        body: formData,
      });
  
      const result = await response.json();
  
      if (response.ok) {
        // Handle successful signup (e.g., redirect to login page or show success message)
        alert('Account created successfully!');
        window.location.href = '/login';
      } else {
        // Handle error from back-end
        setError(result.message || "Something went wrong. Please try again.");
      }
    } catch (err) {
      console.error('Error during sign-up:', err);
      setError('An error occurred. Please try again later.');
    } finally {
      setLoading(false);
    }
  };
  

  const backToLanding = () => navigate('/'); 

  return (
    <div className='overall-container signup'>
        <div className='back-button-container signup'>
          <button className='back-button' title='Back to Beatopia' onClick={backToLanding}>← Back to Main</button>
        </div>
          <h1 className='welcome-message'><span className='login-span'>Ahlan!</span> Welcome to <span className='login-span'>khabar</span>.lb</h1>
          {/* <h4 className='intro-message'>Let's first create an account for you :</h4> */}
          <div className="inputfields-container">
                <AuthField type={"text"} placeholder={"Username"} value={username} onChange={handleUsernameInput}/>
                <AuthField type={"text"} placeholder={"Email Address"} value={email} onChange={handleEmailInput}/>
                <AuthField type={"password"} placeholder={"Enter Password"} value={password} onChange={handlePasswordInput}/>
                <AuthField type={"password"} placeholder={"Confirm Password"} value={checkPassword} onChange={handlePasswordCheckInput}/>
          </div>
          {error && <div className="error-message">{error}</div>} {/* Display error message */}
          <button className='submit-button' type="submit" onClick={submitSignup} disabled={loading}>Submit</button>
          {loading ? <div className="loading-text">Creating Account...</div> : ''}
          {checkPassword && password !== checkPassword && (
            <div className="error-message">Passwords do not match.</div>
          )}
      </div>

    
    
  );
};

export default AdminSingupForm;
