var ResumeForm = React.createClass({
  getInitialState: function() {
    return {
      fields: [
        { name: 'title', question: 'What\'s your job title?' }
      ],
      currentField: 0
    };
  },
  render: function() {
    return (
      <div className="row">
        <div className="col-md-offset-2 col-md-8">
          <div className="resume-form">
            <div className="resume-question">
              { this.state.fields[this.state.currentField].question }
            </div>
            <input className="resume-form-input"/>
            <button type="button">
              Next
            </button>
          </div>
        </div>
      </div>
    );
  }
});

var Experience = React.createClass({
  render: function() {
    var past_experience = this.props.experience.map(function(exp, i) {
      var points = exp.description.map(function(p, i) {
        return (
          <li key={i}>
            { p }
          </li>
         );
      });

      return (
          <div className="resume-block" key={i}>
            <div className="primary-header">{exp.title}</div>
            <div className="secondary-header">{exp.company} - {exp.location}</div>
            <ul className="experience-description">
              { points }
            </ul>
          </div>
      );
    });

    return (
      <div className="row">
        <div className="col-md-offset-2 col-md-8">
          <div className="title">Experience</div>
          <div> {past_experience} </div>
        </div>
      </div>
    );
  }
});

var Education = React.createClass({
  render: function() {
    var education = this.props.education.map(function(ed, i) {
      return (
        <div key={i}>
          <div className="primary-header">{ed.degree}</div>
          <div className="secondary-header">{ed.school}</div>
        </div>
      )
    });

    return (
      <div className="row">
        <div className="col-md-offset-2 col-md-8">
          <div className="title">Education</div>
          { education }
        </div>
      </div>
    );
  }
});

var StudentResume = React.createClass({
  render: function() {
    return (
      <div className="container">
        <ResumeForm />
        <Experience experience={this.props.student_info.experience} />
        <Education education={this.props.student_info.education} />
      </div>
    );
  }
});

while(!window.pageData.studentInfo) {}

console.log(window.pageData.studentInfo);

ReactDOM.render(
    <StudentResume student_info = { window.pageData.studentInfo } />,
    document.getElementById('react-placeholder')
    );
