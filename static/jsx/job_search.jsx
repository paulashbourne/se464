var studentId = '507f191e810c19729de860ea';

var JobPosting = React.createClass({
  getInitialState: function() {
    return {
      applied: this.props.job.application
    };
  },

  apply: function() {
    console.log("Applying to " + this.props.job.job_id);
    var that = this;
    $.post('/api/apply/' + studentId + '/' + this.props.job.job_id, function() {
      console.log("Applied");
      that.setState({applied: true});
    });
  },

  render: function() {
    console.log(this.state);
    var buttonText = this.state.applied ? "Applied" : "Apply";
    return (
      <div className="row job-posting">
        <div className="col-md-8">
          <div className="primary-header">
            {this.props.job.position}
          </div>
          <div className="secondary-header">
            {this.props.job.company_name} - {this.props.job.location}
          </div>
        </div>
        <div className="col-md-4">
          <button type="button" onClick={this.apply}>{buttonText}</button>
        </div>
      </div>
    );
  }
});

var JobSearchPage = React.createClass({
  getInitialState: function() {
    return { results: undefined };
  },

  handleSearch: function() {
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
    $.get('/api/jobs?' + queryString, function(results) {
      that.setState({'results': $.parseJSON(results)});
    });
  },

  render: function() {
    var results = <div></div>;
    console.log(this.state.results);
    if (this.state.results) {
      var jobs = this.state.results.map(function(job, i) {
        return <JobPosting job={job} key={i} />;
      });
      results = (
        <div>
          Showing {this.state.results.length} results
          <div>
            { jobs }
          </div>
        </div>
      );
    }

    return (
      <div className="container">
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <span className="search-title">
              Search for your next internship
             </span>
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <div className="secondary-header">
              Who would you like to work for?
             </div>
             <input id="company-input" className="mb20 full-width" placeholder="Company" />
             <div className="secondary-header">
               Where would you like to work?
              </div>
              <input id="company-location" className="full-width" placeholder="Location" />
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <button type="button" onClick={this.handleSearch}>Search</button>
          </div>
        </div>

        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            { results }
          </div>
        </div>
      </div>
    );
  }
});

ReactDOM.render(
    <JobSearchPage />,
    document.getElementById('react-placeholder')
    );
