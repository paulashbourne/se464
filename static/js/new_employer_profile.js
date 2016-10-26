"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var NewEmployerProfile = function (_React$Component) {
  _inherits(NewEmployerProfile, _React$Component);

  function NewEmployerProfile(props) {
    _classCallCheck(this, NewEmployerProfile);

    return _possibleConstructorReturn(this, (NewEmployerProfile.__proto__ || Object.getPrototypeOf(NewEmployerProfile)).call(this, props));
  }

  _createClass(NewEmployerProfile, [{
    key: "render",
    value: function render() {
      return React.createElement(
        "form",
        null,
        React.createElement(
          "label",
          null,
          "Employer Name"
        ),
        React.createElement("br", null),
        React.createElement("input", { type: "text" }),
        React.createElement("br", null),
        React.createElement(
          "label",
          null,
          "Employer Description"
        ),
        React.createElement("br", null),
        React.createElement("input", { type: "text" }),
        React.createElement("br", null),
        React.createElement(
          "label",
          null,
          "Employer Website"
        ),
        React.createElement("br", null),
        React.createElement("input", { type: "text" }),
        React.createElement("br", null),
        React.createElement(
          "label",
          null,
          "E-mail"
        ),
        React.createElement("br", null),
        React.createElement("input", { type: "text" }),
        React.createElement("br", null),
        React.createElement(
          "label",
          null,
          "Job Descriptions"
        ),
        React.createElement("br", null),
        React.createElement("textarea", { rows: "5", cols: "50" }),
        React.createElement("br", null),
        React.createElement("input", { type: "submit", name: "submit", value: "Submit" })
      );
    }
  }]);

  return NewEmployerProfile;
}(React.Component);

ReactDOM.render(React.createElement(NewEmployerProfile, null), document.getElementById('react-placeholder'));