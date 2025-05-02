import React, { useState, useEffect } from 'react';
import axios from "axios";
import './PostFeed.css';
import PostElement from './PostElement';

const PostFeed = ({ filterOutlet = false }) => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5120/api/Posts/GetFeedPosts") // 
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => {
        console.error("Error fetching posts:", error);
      })
  }, []);
  
  if(!filterOutlet){ 
    useEffect(() => {})
  }

  return (
    <div>
      {posts.map((post, index) => (
        <PostElement key={index} postData={post} />
      ))}
    </div>
  );
};

export default PostFeed;
