var Experience = React.createClass({
  render: function() {
    var past_experience = this.props.experience.map(function(exp, i) {
      return (
          <div key={i}>{exp.title}</div>
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
    return (
      <div className="row">
        <div className="col-md-offset-2 col-md-8">
          <div className="title">Education</div>
        </div>
      </div>
    );
  }
});

var StudentResume = React.createClass({
  render: function() {
    return (
      <div className="container">
        <Experience experience={this.props.student_info.experience} />
        <Education />
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
