import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './SearchBar.css'; 

const SearchBar = ({ placeholder="", onChange=null, value=null, onKeyDown=null }) => {
    return (
      <div className='search-bar-container'>
        <div className="input-group search-bar">
          <span className="input-group-text search-icon">
            <i className="bi bi-search"></i>
          </span>
          <input
            type="text"
            className="form-control"
            placeholder={placeholder}
            value={value}
            onChange={onChange}
            onKeyDown={onKeyDown}
          />
        </div>        
      </div>
    );
};

export default SearchBar;