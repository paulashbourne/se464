"use strict";

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

var _get = function get(_x, _x2, _x3) { var _again = true; _function: while (_again) { var object = _x, property = _x2, receiver = _x3; desc = parent = getter = undefined; _again = false; if (object === null) object = Function.prototype; var desc = Object.getOwnPropertyDescriptor(object, property); if (desc === undefined) { var parent = Object.getPrototypeOf(object); if (parent === null) { return undefined; } else { _x = parent; _x2 = property; _x3 = receiver; _again = true; continue _function; } } else if ("value" in desc) { return desc.value; } else { var getter = desc.get; if (getter === undefined) { return undefined; } return getter.call(receiver); } } };

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) subClass.__proto__ = superClass; }

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

var EmployerInfo = (function (_React$Component) {
  function EmployerInfo(props) {
    _classCallCheck(this, EmployerInfo);

    _get(Object.getPrototypeOf(EmployerInfo.prototype), "constructor", this).call(this, props);
  }

  _inherits(EmployerInfo, _React$Component);

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
})(React.Component);

var EmployerListings = (function (_React$Component2) {
  function EmployerListings(props) {
    _classCallCheck(this, EmployerListings);

    _get(Object.getPrototypeOf(EmployerListings.prototype), "constructor", this).call(this, props);
  }

  _inherits(EmployerListings, _React$Component2);

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
})(React.Component);

ReactDOM.render(React.createElement(EmployerProfile, null), document.getElementById("react-placeholder"));