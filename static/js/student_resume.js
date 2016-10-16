"use strict";

var Experience = React.createClass({
  displayName: "Experience",

  render: function render() {
    var past_experience = this.props.experience.map(function (exp, i) {
      var points = exp.description.map(function (p, i) {
        return React.createElement(
          "li",
          { key: i },
          p
        );
      });

      return React.createElement(
        "div",
        { key: i },
        React.createElement(
          "div",
          { className: "primary-header" },
          exp.title
        ),
        React.createElement(
          "div",
          { className: "secondary-header" },
          exp.company,
          " - ",
          exp.location
        ),
        React.createElement(
          "ul",
          { className: "experience-description" },
          points
        )
      );
    });

    return React.createElement(
      "div",
      { className: "row" },
      React.createElement(
        "div",
        { className: "col-md-offset-2 col-md-8" },
        React.createElement(
          "div",
          { className: "title" },
          "Experience"
        ),
        React.createElement(
          "div",
          null,
          " ",
          past_experience,
          " "
        )
      )
    );
  }
});

var Education = React.createClass({
  displayName: "Education",

  render: function render() {
    return React.createElement(
      "div",
      { className: "row" },
      React.createElement(
        "div",
        { className: "col-md-offset-2 col-md-8" },
        React.createElement(
          "div",
          { className: "title" },
          "Education"
        )
      )
    );
  }
});

var StudentResume = React.createClass({
  displayName: "StudentResume",

  render: function render() {
    return React.createElement(
      "div",
      { className: "container" },
      React.createElement(Experience, { experience: this.props.student_info.experience }),
      React.createElement(Education, null)
    );
  }
});

while (!window.pageData.studentInfo) {}

console.log(window.pageData.studentInfo);

ReactDOM.render(React.createElement(StudentResume, { student_info: window.pageData.studentInfo }), document.getElementById("react-placeholder"));