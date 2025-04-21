import React, { useState } from 'react';
import PostAuthNavbar from '../Navigation/PostAuthNavbar';
import './SearchPage.css';
import SearchBar from '../Navigation/SearchBar';
import PostElement from '../PostFeed/PostElement';
import OutletCard from '../Misc/OutletCard';
import PreAuthNavbar from '../Navigation/PreAuthNavbar';

const SearchPage = () => {
  const [query, setQuery] = useState("");
  const [postResults, setPostResults] = useState([]);
  const [resourceResults, setResourceResults] = useState([]);
  const [searched, setSearched] = useState(false); // flag to show 'No matches' only after search

  const handleSearch = (e) => {
    if (e.key === 'Enter') {
      console.log("Search triggered for:", query);
      setSearched(true);

      if (query.trim().startsWith("@")) {
        // TO-DO Query
        const fakeOutlets = [
          { id: 1, sourceName: "MTV", SRR: 4.2, followingStatus: true },
          { id: 2, sourceName: "OTV", SRR: 3.5, followingStatus: false},
        ];
        const filtered = fakeOutlets.filter(outlet =>
          outlet.sourceName.toLowerCase().includes(query.substring(1).toLowerCase())
        );
        setResourceResults(filtered);
        setPostResults([]); 
      } else {
        // TO-DO Query
        const fakePosts = [
          {
            "city": "Beirut",
            "selectedReaction": null,
            "counters": [120, 10, 0, 0, 3, 1, 2, 0],
            "headline": "إضراب تعاقدو الأساسي الرسمي: نطالب الحكومة بالعودة عن قرارها المجحف",
            "body": "وللمناسبة، قالت رئيسة الرابطة نسرين شاهين: \"جئنا اليوم لندافع عن كرامة المعلمين...\"",
            "sourceName": "MTV",
            "SRR": 3.6,
            "PTS": 78,
            "dateTime": "4/18/2025 15:53",
            "admin": ""
          },
          {
            "city": "Tripoli",
            "selectedReaction": 2,
            "counters": [90, 5, 4, 0, 1, 0, 1, 0],
            "headline": "إضراب عام في المدارس الرسمية الثلاثاء القادم",
            "body": "إضراب عام بسبب الأجور غير المدفوعة ومطالب بتثبيت العقود",
            "sourceName": "LBCI",
            "SRR": 3.9,
            "PTS": 82,
            "dateTime": "4/16/2025 09:00",
            "admin": "Verified"
          }
        ];
        
        const filtered = fakePosts.filter(post =>
          post.headline.toLowerCase().includes(query.toLowerCase())
        );
        setPostResults(filtered);
        setResourceResults([]); 
      }
    }
  };

  const renderResults = () => {
    if (query.trim().startsWith("@")) {
      return resourceResults.length > 0 ? (
        <>
          <p className="results-count">{resourceResults.length} result(s) found</p>
          {resourceResults.map(outlet => (
            <OutletCard key={outlet.id} sourceName={outlet.sourceName} SRR={outlet.SRR} followingStatus={outlet.followingStatus} />
          ))}
        </>
      ) : (
        searched && <p className="no-results">No matches found</p>
      );
    } else {
      return postResults.length > 0 ? (
        <>
          <p className="results-count">{postResults.length} result(s) found</p>
          {postResults.map(post => (
            <PostElement key={post.id} postData={post} />
          ))}
        </>
      ) : (
        searched && <p className="no-results">No matches found</p>
      );
    }
  };
  
  return (
    <div>
      <PostAuthNavbar />
      <div className='search-page-wrapper'>
        <h2 className='search-page-heading'> Search for the Latest News </h2>
        <SearchBar 
          placeholder="Search news or @sources..." 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          onKeyDown={handleSearch} 
        />

        <div className="search-results-container">
          {renderResults()} {/* Whether Outlets or Posts */}
        </div>
      </div>
    </div>
  );
};

export default SearchPage;