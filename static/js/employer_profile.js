
var EmployerProfile = React.createClass({
  displayName: "EmployerProfile",

  render: function () {
    return React.createElement(
      "div",
      { className: "container" },
      React.createElement(EmployerInfo, null),
      React.createElement(EmployerListings, null)
    );
  }
});

class EmployerInfo extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return React.createElement(
      "div",
      { className: "row" },
      React.createElement(
        "div",
        { className: "row mb20" },
        React.createElement(
          "div",
          { className: "col-md-offset-2 col-md-8" },
          React.createElement(
            "span",
            { className: "search-title" },
            "Your Profile"
          )
        )
      ),
      React.createElement(
        "div",
        { className: "row mb20" },
        React.createElement(
          "div",
          { className: "col-md-offset-2 col-md-8" },
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "Name"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.name"
          ),
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "E-mail"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.email"
          ),
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "Website"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.website"
          ),
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "Description"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.description"
          )
        )
      )
    );
  }
}

class EmployerListings extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return React.createElement(
      "div",
      { className: "row" },
      React.createElement(
        "div",
        { className: "row mb20" },
        React.createElement(
          "div",
          { className: "col-md-offset-2 col-md-8" },
          React.createElement(
            "span",
            { className: "search-title" },
            "Your Job Listings"
          )
        )
      ),
      React.createElement(
        "div",
        { className: "row mb20" },
        React.createElement(
          "div",
          { className: "col-md-offset-2 col-md-8" },
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "Name"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.name"
          ),
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "E-mail"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.email"
          ),
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "Website"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.website"
          ),
          React.createElement(
            "div",
            { className: "col-md-2 secondary-header" },
            "Description"
          ),
          React.createElement(
            "div",
            { className: "mb20 full-width" },
            "this.props.employer.description"
          )
        )
      )
    );
  }
}

ReactDOM.render(React.createElement(EmployerProfile, null), document.getElementById('react-placeholder'));