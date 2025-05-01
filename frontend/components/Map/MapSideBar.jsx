import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation
import './MapSideBar.css'; 

const MapSideBar = ({ newsByLoc = [] }) => {
  const navigate = useNavigate(); // Initialize navigate function

  const handlePostNavigation = (loc, headline) => {
    const postData = {
      "city": "Beirut",
      "selectedReaction": null,
      "counters": [120, 10, 0, 0, 3, 1, 2, 0],
      "headline": "متعاقدو الأساسي الرسمي: نطالب الحكومة بالعودة عن قرارها المجحف",
      "body": "وللمناسبة، قالت رئيسة الرابطة نسرين شاهين: \"جئنا اليوم لندافع عن كرامة المعلمين...\"",
      "sourceName": "OTV",
      "SRR": 3.6,
      "PTS": 78,
      "dateTime": "4/18/2025 15:53",
      "admin": ""
    };
    // TO-DO Query #1
    // useEffect(() => {
  //   axios.get("http://localhost:4000/posts") // TO-DO Query #1 Change Port Number
  //     .then(response => {
  //       setPosts(response.data);
  //     })
  //     .catch(error => {
  //       console.error("Error fetching posts:", error);
  //     })
  // }, []);
    const query = new URLSearchParams(postData).toString();
    navigate(`/post?${query}`);
  };  

  return (
    <div className="map-sidebar"> {/* Container for the sidebar */}
      
      {/* Title of the Sidebar */}
      {/* <h3 className='map-sidebar-title'>📰 Latest News by Location</h3> */}

      
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

      {/* TRIAL ZONE */}

      {/* List of news headlines */}
      <div className="headline-list">
        {newsByLoc.map((loc, index) => (
          <div key={index} className="city-headlines"> {/* City-specific container */}
            
            {/* City name as header */}
            <h3>{loc.city}</h3>
            
            {/* Headlines for the city */}
            <ul>
              {loc.headlines.map((headline, i) => (
                <li
                  key={i}
                  onClick={() => handlePostNavigation(loc, headline)} 
                  title="See Post"  
                  className="headline-item"  
                >
                  {/* Headline Text */}
                  <span className="headline-text">{headline}</span>

                  {/* Arrow Button to "See Post" */}
                  <button
                    className="see-post-button"
                    onClick={(e) => {
                      e.stopPropagation();  {/* Prevents event from bubbling up */}
                      handlePostNavigation(loc, headline);  {/* Navigate to SinglePostView */}
                    }}
                    title="See Post"
                  >
                    ➜ {/* Arrow pointing to the left */}
                  </button>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MapSideBar;