import React from 'react';

import './App.css';

function App(this: any) {
  return (
    <div className="App">
      <header className="App-header">

        <label htmlFor="name">Name:</label>
        <input type="text" id="name" name="name"></input><br></br>
        
        <label htmlFor="email">Email Address:</label>
        <input type="email" id="email" name="email"></input><br></br>

        <label htmlFor="lname">Favourite Source Control:</label>
        
          <select >
            <option value="github">GitHub</option>
            <option value="gitlab">GitLab</option>
            <option value="bitbucket">BitBucket</option>
            <option value="tfs">TFS</option>
            <option value="other">Other</option>
          </select>
        <br></br>

        <label htmlFor="lname">How many people work on your team?</label>
        <input type="number" id="team" name="team"></input><br></br>

        <input type="submit" value="Submit"></input>

      </header>
      <body>

      </body>
    </div>
  );
}

export default App;
