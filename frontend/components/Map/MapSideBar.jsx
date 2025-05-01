import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './MapSideBar.css';

const MapSideBar = () => {
  const navigate = useNavigate();
  const [newsByLoc, setNewsByLoc] = useState([]);
  // TO-DO, pass the two filters values to the useEffect method querying for news
  useEffect(() => {
    axios.get('http://localhost:5120/api/Posts/')
      .then(response => {
        // response.data is already the array you showed in Postman
        setNewsByLoc(response.data);
      })
      .catch(console.error);
  }, []);

  const handlePostNavigation = (loc, article) => {
    const postData = {
      city: loc.city,
      articleId: article.articleId,
      headline: article.headline,
      // …add any other fields you need
    };
    const query = new URLSearchParams(postData).toString();
    navigate(`/post?${query}`);
  };

  return (
    <div className="map-sidebar">
      <div className="d-flex justify-content" style={{ gap: '1rem'}}>
      {/* First Dropdown */}
        <div className="dropdown custom-dropdown">
          <button
            className="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenuButton1"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Recent
          </button>
          <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
            <li><a className="dropdown-item" href="#">Last 24 hrs</a></li>
            <li><a className="dropdown-item" href="#">Last 7 days</a></li>
            {/* <li><a className="dropdown-item" href="#">Something else</a></li> */}
          </ul>
        </div>

        {/* Second Dropdown */}
        <div className="dropdown custom-dropdown">
          <button
            className="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenuButton2"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Following
          </button>
          <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton2">
            <li><a className="dropdown-item" href="#">All</a></li>
            <li><a className="dropdown-item" href="#">Following</a></li>
            {/* <li><a className="dropdown-item" href="#">Option C</a></li> */}
          </ul>
        </div>
      </div>

      <div className="headline-list">
        {newsByLoc?.map((loc, idx) => (
          <div key={idx} className="city-headlines">
            <h3>{loc.city}</h3>
            <ul>
              {Array.isArray(loc.articles) && loc.articles.length > 0 ? (
                loc.articles.map((article, i) => (
                  <li
                    key={i}
                    className="headline-item"
                    onClick={() => handlePostNavigation(loc, article)}
                    title="See Post"
                  >
                    <span className="headline-text">
                      {article.headline}
                    </span>
                    <button
                      className="see-post-button"
                      onClick={e => {
                        e.stopPropagation();
                        handlePostNavigation(loc, article);
                      }}
                      title="See Post"
                    >
                      ➜
                    </button>
                  </li>
                ))
              ) : (
                <li>No articles</li>
              )}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MapSideBar;
