
import React, { createContext, useState, useContext } from 'react';

// Create the Context
const GlobalContext = createContext();

// Custom hook to use the GlobalContext
export const useGlobalContext = () => useContext(GlobalContext);

// Provider component that holds the global state
export const GlobalProvider = ({ children }) => {
  const [userID, setUserID] = useState(null); // Initially, userID is null
  const [isAdmin, setIsAdmin] = useState(false); // Initially, isAdmin is false

  // Function to update userID after authentication
  const updateUserID = (id) => {
    setUserID(id);
  };

  // Function to update isAdmin after checking user's role (like from API or login)
  const updateIsAdmin = (status) => {
    setIsAdmin(status);
  };

  return (
    <GlobalContext.Provider value={{ userID, updateUserID, isAdmin, updateIsAdmin }}>
      {children} {/* This will render the nested components */}
    </GlobalContext.Provider>
  );
};
