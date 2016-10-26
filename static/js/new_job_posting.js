"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var NewJobForm = function (_React$Component) {
  _inherits(NewJobForm, _React$Component);

  function NewJobForm(props) {
    _classCallCheck(this, NewJobForm);

    return _possibleConstructorReturn(this, (NewJobForm.__proto__ || Object.getPrototypeOf(NewJobForm)).call(this, props));
  }

  _createClass(NewJobForm, [{
    key: "render",
    value: function render() {
      var _React$createElement;

      return React.createElement(
        "div",
        { className: "container" },
        React.createElement(
          "form",
          null,
          React.createElement(
            "div",
            { className: "row mb20" },
            React.createElement(
              "div",
              { className: "col-md-offset-2 col-md-8" },
              React.createElement(
                "span",
                { className: "search-title" },
                "New Job Posting"
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
                { className: "secondary-header" },
                "Job Title"
              ),
              React.createElement("input", { className: "mb20 full-width" }),
              React.createElement(
                "div",
                { className: "secondary-header" },
                "Number of Openings"
              ),
              React.createElement("input", { type: "number", className: "full-width", value: "1" })
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
                { className: "secondary-header" },
                "Job Title"
              ),
              React.createElement("input", { className: "mb20 full-width" }),
              React.createElement(
                "div",
                { className: "secondary-header" },
                "Job Description"
              ),
              React.createElement("textarea", { className: "full-width" })
            )
          ),
          React.createElement(
            "div",
            { className: "row mb20" },
            React.createElement(
              "div",
              { className: "col-md-offset-2 col-md-8" },
              React.createElement("input", (_React$createElement = { type: "submit" }, _defineProperty(_React$createElement, "type", "button"), _defineProperty(_React$createElement, "value", "Create Job"), _React$createElement))
            )
          )
        )
      );
    }
  }]);

  return NewJobForm;
}(React.Component);

ReactDOM.render(React.createElement(NewJobForm, null), document.getElementById('react-placeholder'));