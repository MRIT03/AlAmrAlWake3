import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

// Importing pages
import FeedPage from '../components/PostFeed/FeedPage';
import MapPage from '../components/Map/MapPage';
import SearchPage from '../components/Search/SearchPage';
import SettingsPage from '../components/Settings/SettingsPage';
import SinglePostView from '../components/Misc/SinglePostView';
import NewsSourcePage from '../components/Misc/NewsSourcePage';
import LoginForm from '../components/Authentication/LoginForm';
import SignupForm from '../components/Authentication/SignupForm';

function App() {
  return (
    <Router>
      <div className="app-layout">
        {/* Define Routes for FeedPage, MapPage, SearchPage, SettingsPage */}
        <Routes>
          <Route path="/" element={<FeedPage />} />
          <Route path="/map" element={<MapPage />} />
          <Route path="/search" element={<SearchPage />} /> 
          <Route path="/settings" element={<SettingsPage />} /> 
          <Route path="/post" element={<SinglePostView />} />
          <Route path="/outlet" element={<NewsSourcePage />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/signup" element={<SignupForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;