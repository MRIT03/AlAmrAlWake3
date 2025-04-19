import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './SearchBar.css'; 

const SearchBar = ({ placeholder="this is a placeholder", onChange=null, value=null }) => {
  
    const handleKeyPress = (e) => {
        if(e.key === 'Enter') {
            console.log("Search for: ", value);
            // add query logic here
        }
    };
  
    return (
    <div className='search-bar-container'>

        <div className="input-group search-bar">

            <span className="input-group-text search-icon">
                <i className="bi bi-search"></i> {/* Bootstrap icon */}
            </span>

            <input
                type="text"
                className="form-control"
                placeholder={placeholder}
                value={value}
                // onChange={onChange}
                onKeyDown={handleKeyPress}
            />
        </div>        

    </div>
  );
};

export default SearchBar;
