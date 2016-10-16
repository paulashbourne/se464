class NewJobForm extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return React.createElement(
      "form",
      null,
      React.createElement(
        "label",
        null,
        "Job Name"
      ),
      React.createElement("br", null),
      React.createElement("input", { type: "text" }),
      React.createElement("br", null),
      React.createElement(
        "label",
        null,
        "Number of Openings"
      ),
      React.createElement("br", null),
      React.createElement("input", { type: "number" }),
      React.createElement("br", null),
      React.createElement(
        "label",
        null,
        "Job Descriptions"
      ),
      React.createElement("br", null),
      React.createElement("textarea", { rows: "5", cols: "50" }),
      React.createElement("br", null),
      React.createElement("input", { type: "submit", name: "submit", value: "Create Job" })
    );
  }
}

ReactDOM.render(React.createElement(NewJobForm, null), document.getElementById('react-placeholder'));