class NewEmployerProfile extends React.Component {
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
        "Employer Name"
      ),
      React.createElement("input", { type: "text" }),
      React.createElement(
        "label",
        null,
        "Employer Description"
      ),
      React.createElement("input", { type: "text" }),
      React.createElement(
        "label",
        null,
        "Employer Website"
      ),
      React.createElement("input", { type: "text" }),
      React.createElement(
        "label",
        null,
        "E-mail"
      ),
      React.createElement("input", { type: "text" }),
      React.createElement(
        "label",
        null,
        "Job Descriptions"
      ),
      React.createElement("textarea", { rows: "5", cols: "50" }),
      React.createElement("input", { type: "submit", name: "submit", value: "Submit" })
    );
  }
}

ReactDOM.render(React.createElement(NewJobForm, null), document.getElementById('react-placeholder'));