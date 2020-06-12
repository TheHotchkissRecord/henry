var Split = require('split.js');

Split(['#one', '#two', '#three']);

/*
class App extends React.Component {
  componentDidMount () {
    let left = document.getElementById('left');
    let right = document.getElementById('right');
    dragula([left, right]);
  }

  render () {
    return (
      <div className="container">
        <div id="left" className="container">
          <Card body="Card 3"/>
          <Card body="Card 4"/>
        </div>
        <div id="right" className="container">
          <Card body="Card 1"/>
          <Card body="Card 2"/>
        </div>
      </div>
    );
  }
}

class Card extends React.Component {
  constructor (props) {
    super(props);
  }

  render () {
    return (
      <div className="card">
        <div className="card-header">
          <h3>Example Card</h3>
        </div>
        <div className="card-body">
          <p>{this.props.body}</p>
        </div>
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('container'));*/
var React = require('react');
var ReactDOM = require('react-dom');
var reactDragula = require('react-dragula');

class App extends React.Component {
  render () {
    return (<div className="container" id="article-box">
      <div>card 1</div>
      <div>card 2</div>
      <div>card 3</div>
      <div>card 4</div>
      <div>card 5</div>
    </div>
    );
  }
  componentDidMount () {
    let container = document.getElementById('article-box');
    reactDragula([container]);
  }
}
ReactDOM.render(<App />, document.getElementById('container'));


function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
