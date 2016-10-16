"use strict";

var Profile = React.createClass({
  displayName: "Profile",

  render: function render() {

    return React.createElement(
      "div",
      null,
      "St"
    );
  }
});

var Joblist = React.createClass({
  displayName: "Joblist",

  render: function render() {

    return React.createElement("div", null);
  }
});

var EmployerProfile = React.createClass({
  displayName: "EmployerProfile",

  render: function render() {
    return React.createElement(
      "div",
      { className: "container" },
      React.createElement(Profile, null),
      React.createElement(JobList, null)
    );
  }
});

ReactDOM.render(React.createElement(EmployerProfile, null), document.getElementById("react-placeholder"));