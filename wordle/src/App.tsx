import React from 'react';
import logo from './logo.svg';
import './App.css';
import { TextField } from '@material-ui/core';
import './game.tsx';
import Game from './game';
import inputWordleProps from './game';



function App() {
  // Define the props for the InputWordle component

  return (
    <div className="App">
      <header className="App-header">
        <Game/>
      </header>
    </div>
  );
}

export default App;
