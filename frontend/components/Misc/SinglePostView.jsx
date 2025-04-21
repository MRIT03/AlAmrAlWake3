import React, { useEffect, useState } from "react";
import { useLocation } from 'react-router-dom';
import './SinglePostView.css';
import PostAuthNavbar from "../Navigation/PostAuthNavbar";
import PostElement from "../PostFeed/PostElement";

const SinglePostView = () => {
  const location = useLocation();
  const [postData, setPostData] = useState(null);

  useEffect(() => {
    // Use URLSearchParams to parse the query string
    const queryParams = new URLSearchParams(location.search);

    // Extract each field from the query parameters
    const countersParam = queryParams.get('counters');

    // Safely parse the counters parameter (only if it exists and is a valid JSON)
    let counters = [];
        try {
        if (countersParam) {
            // Split by comma and convert each value to a number
            counters = countersParam.split(',').map(num => parseInt(num, 10));
        }
        } catch (e) {
        console.error("Failed to parse counters:", e);
        counters = [];
        }

    const postData = {
      city: queryParams.get('city'),
      selectedReaction: queryParams.get('selectedReaction'),
      counters: counters, // Use the parsed counters
      headline: queryParams.get('headline'),
      body: queryParams.get('body'),
      sourceName: queryParams.get('sourceName'),
      SRR: parseFloat(queryParams.get('SRR')),
      PTS: parseInt(queryParams.get('PTS')),
      dateTime: queryParams.get('dateTime'),
      admin: queryParams.get('admin')
    };

    // Set the postData state
    setPostData(postData);
  }, [location]);

  // If postData isn't available, show a loading or fallback message
  if (!postData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="single-post-view">
      <PostAuthNavbar />

      <div className="single-post-view-back-button-wrapper">
        <button
          className="single-post-view-back-button"
          onClick={() => window.history.back()} // or router (to see later)
        >
          <i className="bi bi-arrow-left me-2"></i>
          Back To Map
        </button>
      </div>

      <div className="single-post-wrapper">
        <PostElement postData={postData} />
      </div>
    </div>
  );
};

export default SinglePostView;
