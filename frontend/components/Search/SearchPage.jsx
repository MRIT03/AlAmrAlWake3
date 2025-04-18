import React, { useState } from 'react';
import PostAuthNavbar from '../Navigation/PostAuthNavbar';
import './SearchPage.css';
import SearchBar from '../Navigation/SearchBar';

const SearchPage = () => {

  return (
    <div>
      <PostAuthNavbar />
      <div className='search-page-wrapper'>
        <h2 className='search-page-heading'> Search for the Latest News </h2>
        <SearchBar />
      </div>
    </div>
  );
};

export default SearchPage;
