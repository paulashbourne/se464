'use strict';

var studentId = '507f191e810c19729de860ea';

var JobPosting = React.createClass({
  displayName: 'JobPosting',

  getInitialState: function getInitialState() {
    return {
      applied: this.props.job.application
    };
  },

  apply: function apply() {
    console.log("Applying to " + this.props.job.job_id);
    var that = this;
    $.post('/api/apply/' + studentId + '/' + this.props.job.job_id, function () {
      that.setState({ applied: true });
    });
  },

  render: function render() {
    var buttonText = this.state.applied ? "Applied" : "Apply";
    return React.createElement(
      'div',
      { className: 'row job-posting' },
      React.createElement(
        'div',
        { className: 'col-md-8' },
        React.createElement(
          'div',
          { className: 'primary-header' },
          this.props.job.position
        ),
        React.createElement(
          'div',
          { className: 'secondary-header' },
          this.props.job.company_name,
          ' - ',
          this.props.job.location
        )
      ),
      React.createElement(
        'div',
        { className: 'col-md-4' },
        React.createElement(
          'button',
          { disabled: this.state.applied, type: 'button', onClick: this.apply },
          buttonText
        )
      )
    );
  }
});

var JobSearchPage = React.createClass({
  displayName: 'JobSearchPage',

  getInitialState: function getInitialState() {
    return { results: undefined };
  },

  handleSearch: function handleSearch() {
    console.log("Searching...");
    var that = this;
    var companyName = $('#company-input').val();
    var companyLocation = $('#company-location').val();
    var queryString = '';
    if (companyName.length > 0) {
      queryString += "&company_name=" + companyName;
    }
    if (companyLocation.length > 0) {
      queryString += "&location=" + companyLocation;
    }
    $.get('/api/jobs?' + queryString, function (results) {
      that.setState({ 'results': $.parseJSON(results) });
    });
  },

  render: function render() {
    var results = React.createElement('div', null);
    console.log(this.state.results);
    if (this.state.results) {
      var jobs = this.state.results.map(function (job, i) {
        return React.createElement(JobPosting, { job: job, key: i });
      });
      results = React.createElement(
        'div',
        null,
        'Showing ',
        this.state.results.length,
        ' results',
        React.createElement(
          'div',
          null,
          jobs
        )
      );
    }

    return React.createElement(
      'div',
      { className: 'container' },
      React.createElement(
        'div',
        { className: 'row mb20' },
        React.createElement(
          'div',
          { className: 'col-md-offset-2 col-md-8' },
          React.createElement(
            'span',
            { className: 'search-title' },
            'Search for your next internship'
          )
        )
      ),
      React.createElement(
        'div',
        { className: 'row mb20' },
        React.createElement(
          'div',
          { className: 'col-md-offset-2 col-md-8' },
          React.createElement(
            'div',
            { className: 'secondary-header' },
            'Who would you like to work for?'
          ),
          React.createElement('input', { id: 'company-input', className: 'mb20 full-width', placeholder: 'Company' }),
          React.createElement(
            'div',
            { className: 'secondary-header' },
            'Where would you like to work?'
          ),
          React.createElement('input', { id: 'company-location', className: 'full-width', placeholder: 'Location' })
        )
      ),
      React.createElement(
        'div',
        { className: 'row mb20' },
        React.createElement(
          'div',
          { className: 'col-md-offset-2 col-md-8' },
          React.createElement(
            'button',
            { type: 'button', onClick: this.handleSearch },
            'Search'
          )
        )
      ),
      React.createElement(
        'div',
        { className: 'row mb20' },
        React.createElement(
          'div',
          { className: 'col-md-offset-2 col-md-8' },
          results
        )
      )
    );
  }
});

ReactDOM.render(React.createElement(JobSearchPage, null), document.getElementById('react-placeholder'));