var AddExperience = React.createClass({
  addExperience: function() {
    var jobTitle = $('#job-title-input').val();
    var company = $('#company-input').val();
    var jobLocation = $('#location-input').val();
    var jobDescription = $('#description-input').val();
    var postData = {company: company,
                    title: jobTitle,
                    description: jobDescription,
                    location: jobLocation};
    var studentId = window.pageData.studentInfo.id;
    $.post('/api/students/' + studentId + '/experience' , postData , function() {
        location.reload();
      });
  },

  render: function() {
    return (
      <div className="row mb20">
        <div className="col-md-offset-2 col-md-8">
          <div className="title">Add Experience</div>
          <div>
            <div className="secondary-header">
              Job Title
             </div>
             <input id="job-title-input" className="full-width" />
             <div className="secondary-header">
               Company
              </div>
              <input id="company-input" className="full-width"/>
             <div className="secondary-header">
               Location
              </div>
              <input id="location-input" className="full-width"/>
             <div className="secondary-header">
               Description
              </div>
              <textarea id="description-input" className="full-width"/>
          </div>
          <button type="button" className="btn bt-default" onClick={this.addExperience}>
            Add Experience
          </button>
        </div>
      </div>
    );
  }
});

var AddEducation = React.createClass({
  addEducation: function() {
    var schoolName = $('#school-input').val();
    var degreeName = $('#degree-input').val();
    var majorName = $('#major-input').val();
    var postData = {school: schoolName,
                    degree: degreeName,
                    major: majorName};
    var studentId = window.pageData.studentInfo.id;
    $.post('/api/students/' + studentId + '/education' , postData , function() {
      });
  },

  render: function() {
    return (
      <div className="row mb20">
        <div className="col-md-offset-2 col-md-8">
          <div className="title">Add Education</div>
          <div>
            <div className="secondary-header">
              School
             </div>
             <input id="school-input" className="full-width" />
             <div className="secondary-header">
               Degree
              </div>
              <input id="degree-input" className="full-width"/>
             <div className="secondary-header">
               Major
              </div>
              <input id="major-input" className="full-width"/>
          </div>
          <button type="button" className="btn bt-default" onClick={this.addEducation}>
            Add Education
          </button>
        </div>
      </div>
    );
  }
});

var Experience = React.createClass({
  render: function() {
    var past_experience = this.props.experience.map(function(exp, i) {
      var points = exp.description.split('\n').map(function(p, i) {
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
          <div className="primary-header">{ed.degree} - {ed.major}</div>
          <div className="secondary-header">{ed.school}</div><br/>
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
    var add_experience = <AddExperience />;
    if (window.pageData.view) {
      add_experience = null;
    }
    var add_education = <AddEducation />;
    if (window.pageData.view) {
      add_education = null;
    }

    return (
      <div className="container">
        { add_experience }
        { add_education }
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
