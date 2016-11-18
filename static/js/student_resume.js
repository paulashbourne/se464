'use strict';

var AddExperience = React.createClass({
  displayName: 'AddExperience',

  addExperience: function addExperience() {
    var jobTitle = $('#job-title-input').val();
    var company = $('#company-input').val();
    var jobLocation = $('#location-input').val();
    var jobDescription = $('#description-input').val();
    var postData = { company: company,
      title: jobTitle,
      description: jobDescription,
      location: jobLocation };
    var studentId = window.pageData.studentInfo.id;
    $.post('/api/students/' + studentId + '/experience', postData, function () {
      location.reload();
    });
  },

  render: function render() {
    return React.createElement(
      'div',
      { className: 'row mb20' },
      React.createElement(
        'div',
        { className: 'col-md-offset-2 col-md-8' },
        React.createElement(
          'div',
          { className: 'title' },
          'Add Experience'
        ),
        React.createElement(
          'div',
          null,
          React.createElement(
            'div',
            { className: 'secondary-header' },
            'Job Title'
          ),
          React.createElement('input', { id: 'job-title-input', className: 'full-width' }),
          React.createElement(
            'div',
            { className: 'secondary-header' },
            'Company'
          ),
          React.createElement('input', { id: 'company-input', className: 'full-width' }),
          React.createElement(
            'div',
            { className: 'secondary-header' },
            'Location'
          ),
          React.createElement('input', { id: 'location-input', className: 'full-width' }),
          React.createElement(
            'div',
            { className: 'secondary-header' },
            'Description'
          ),
          React.createElement('textarea', { id: 'description-input', className: 'full-width' })
        ),
        React.createElement(
          'button',
          { type: 'button', className: 'btn bt-default', onClick: this.addExperience },
          'Add Experience'
        )
      )
    );
  }
});

var Experience = React.createClass({
  displayName: 'Experience',

  render: function render() {
    var past_experience = this.props.experience.map(function (exp, i) {
      var points = exp.description.split('\n').map(function (p, i) {
        return React.createElement(
          'li',
          { key: i },
          p
        );
      });

      return React.createElement(
        'div',
        { className: 'resume-block', key: i },
        React.createElement(
          'div',
          { className: 'primary-header' },
          exp.title
        ),
        React.createElement(
          'div',
          { className: 'secondary-header' },
          exp.company,
          ' - ',
          exp.location
        ),
        React.createElement(
          'ul',
          { className: 'experience-description' },
          points
        )
      );
    });

    return React.createElement(
      'div',
      { className: 'row' },
      React.createElement(
        'div',
        { className: 'col-md-offset-2 col-md-8' },
        React.createElement(
          'div',
          { className: 'title' },
          'Experience'
        ),
        React.createElement(
          'div',
          null,
          ' ',
          past_experience,
          ' '
        )
      )
    );
  }
});

var Education = React.createClass({
  displayName: 'Education',

  render: function render() {
    var education = this.props.education.map(function (ed, i) {
      return React.createElement(
        'div',
        { key: i },
        React.createElement(
          'div',
          { className: 'primary-header' },
          ed.degree
        ),
        React.createElement(
          'div',
          { className: 'secondary-header' },
          ed.school
        )
      );
    });

    return React.createElement(
      'div',
      { className: 'row' },
      React.createElement(
        'div',
        { className: 'col-md-offset-2 col-md-8' },
        React.createElement(
          'div',
          { className: 'title' },
          'Education'
        ),
        education
      )
    );
  }
});

var StudentResume = React.createClass({
  displayName: 'StudentResume',

  render: function render() {
    return React.createElement(
      'div',
      { className: 'container' },
      React.createElement(AddExperience, null),
      React.createElement(Experience, { experience: this.props.student_info.experience }),
      React.createElement(Education, { education: this.props.student_info.education })
    );
  }
});

while (!window.pageData.studentInfo) {}

console.log(window.pageData.studentInfo);

ReactDOM.render(React.createElement(StudentResume, { student_info: window.pageData.studentInfo }), document.getElementById('react-placeholder'));