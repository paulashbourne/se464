"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var EmployerProfile = React.createClass({
  displayName: "EmployerProfile",

  render: function render() {
    return React.createElement(
      "div",
      { className: "container" },
      React.createElement(EmployerInfo, null),
      React.createElement(EmployerListings, null)
    );
  }
});

var EmployerInfo = function (_React$Component) {
  _inherits(EmployerInfo, _React$Component);

  function EmployerInfo(props) {
    _classCallCheck(this, EmployerInfo);

    return _possibleConstructorReturn(this, (EmployerInfo.__proto__ || Object.getPrototypeOf(EmployerInfo)).call(this, props));
  }

  _createClass(EmployerInfo, [{
    key: "render",
    value: function render() {
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
  }]);

  return EmployerInfo;
}(React.Component);

var EmployerListings = function (_React$Component2) {
  _inherits(EmployerListings, _React$Component2);

  function EmployerListings(props) {
    _classCallCheck(this, EmployerListings);

    return _possibleConstructorReturn(this, (EmployerListings.__proto__ || Object.getPrototypeOf(EmployerListings)).call(this, props));
  }

  _createClass(EmployerListings, [{
    key: "render",
    value: function render() {
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
  }]);

  return EmployerListings;
}(React.Component);

ReactDOM.render(React.createElement(EmployerProfile, null), document.getElementById('react-placeholder'));