"use strict";

var _createClass = (function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; })();

var _get = function get(_x, _x2, _x3) { var _again = true; _function: while (_again) { var object = _x, property = _x2, receiver = _x3; desc = parent = getter = undefined; _again = false; if (object === null) object = Function.prototype; var desc = Object.getOwnPropertyDescriptor(object, property); if (desc === undefined) { var parent = Object.getPrototypeOf(object); if (parent === null) { return undefined; } else { _x = parent; _x2 = property; _x3 = receiver; _again = true; continue _function; } } else if ("value" in desc) { return desc.value; } else { var getter = desc.get; if (getter === undefined) { return undefined; } return getter.call(receiver); } } };

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) subClass.__proto__ = superClass; }

var NewJobForm = (function (_React$Component) {
  function NewJobForm(props) {
    _classCallCheck(this, NewJobForm);

    _get(Object.getPrototypeOf(NewJobForm.prototype), "constructor", this).call(this, props);
  }

  _inherits(NewJobForm, _React$Component);

  _createClass(NewJobForm, [{
    key: "render",
    value: function render() {
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
              React.createElement("input", { type: "submit", type: "button", value: "Create Job" })
            )
          )
        )
      );
    }
  }]);

  return NewJobForm;
})(React.Component);

ReactDOM.render(React.createElement(NewJobForm, null), document.getElementById("react-placeholder"));