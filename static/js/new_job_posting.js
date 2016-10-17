class NewJobForm extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
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
}

ReactDOM.render(React.createElement(NewJobForm, null), document.getElementById('react-placeholder'));