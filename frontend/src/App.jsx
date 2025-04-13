import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import MapContainer from '/components/Map/MapContainer';
import MapPage from '../components/Map/MapPage';
import PostFeed from '../components/PostFeed/PostFeed';

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="app-layout">
      <PostFeed />
    </div>
  )
}

export default App
