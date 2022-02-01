import React from 'react';
import './App.css';

class App extends React.Component {

  constructor(props: any) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event: { target: { value: any; }; }) {
    this.setState({ value: event.target.value });
  }

  handleSubmit(event: any) {
    console.log("making request")
    fetch('/submit/')
      .then(response => {
        console.log(response)
        return response.json()
      })
      .then(json => {
        console.log = (json)
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit} action="http://localhost:5000/submit/" method="get">

          <h1> Enter your information.</h1>

          <label>Name: </label>
          <input type="text" name="name" />
          <br></br>
          <br></br>

          <label htmlFor="email">Email Address: </label>
          <input type="email" id="email" name="email"></input>
          <br></br>
          <br></br>

          <label htmlFor="sc">Favourite Source Control: </label>
          <select name="sc" id="sc">
            <option value="github">GitHub</option>
            <option value="gitlab">GitLab</option>
            <option value="bitbucket">BitBucket</option>
            <option value="tfs">TFS</option>
            <option value="other">Other</option>
          </select>
          <br></br>
          <br></br>

          <label htmlFor="team">How many people work on your team? </label>
          <input type="number" id="team" name="team"></input
          ><br></br>
          <br></br>

          <input type="submit" onChange={this.handleChange} value="Submit Info." />

        </form>
   
      </div>
    );
  }
}

export default App;
