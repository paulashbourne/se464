class JobPosting extends React.Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this);
    this.state = {
      expanded: false
    };
  }

  handleClick() {
    this.setState({ expanded: !this.state.expanded });
  }

  render() {
    var applications = <div></div>;

    if (this.state.expanded) {
      applications = this.props.job.applications.map(function(app, i) {
        var link = "/student/" + app.student_id + "/resume/view";
        return (
          <div key={i}>
            <a href={ link }>
              Application {i + 1}
            </a>
          </div>
        )
      });
    }

    var isHidden = this.props.job.applications.length && this.state.expanded ?
      "" : "hidden";

    return (
      <div>
        <div className="row job-posting mb5" onClick={this.handleClick}>
          <div className="col-md-8">
            <div className="primary-header">
              {this.props.job.position}
            </div>
            <div className="secondary-header">
              {this.props.job.company_name} - {this.props.job.location}
            </div>
          </div>
          <div className="col-md-4">
            <div className="secondary-header">
              {this.props.job.applications.length} Applications
            </div>
          </div>
        </div>
        <div className={"row job-posting " + isHidden}>
          <div className="col-md-8">
            { applications }
          </div>
        </div>
      </div>
    );
  }
}

class EmployerInfo extends React.Component {
  constructor(props) {
    super(props);
    /*var that = this;
    $.get('/api/employer/' + window.pageData.employerId, function(results) {
      that.setState({'employer_info': $.parseJSON(results)});
      console.log("done");
    });*/

    //console.log(that.state.employer_info);
  }

  render() {
    return (
      <div className="row">
      	<div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <span className="search-title">
              Your Profile
             </span>
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <div className="col-md-2 secondary-header">
              Name
             </div>
             <div className="mb20 full-width col-md-2 primary-header">{this.props.employer_info[0].company_name}</div>
            <div className="col-md-2 secondary-header">
              E-mail
             </div>
             <div className="mb20 full-width col-md-2 primary-header">{this.props.employer_info[0].emails.join(",  ")}</div>
            <div className="col-md-2 secondary-header">
              Website
             </div>
             <div className="mb20 full-width col-md-2 primary-header">{this.props.employer_info[0].website}</div>
            <div className="col-md-2 secondary-header">
              Description
             </div>
             <div className="mb20 full-width col-md-2 primary-header">{this.props.employer_info[0].description}</div>
          </div>
        </div>
      </div>
    );
  }
}

class EmployerListings extends React.Component {
  render() {
    var jobs = window.pageData.jobs.map(function(job, i) {
      return <JobPosting job={job} key={i} />;
    });

    return (
      <div className="row">
      	<div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <span className="search-title">
              Your Job Listings
             </span>
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
          { jobs }
          </div>
        </div>
      </div>
    );
  }
}

class EmployerProfile extends React.Component {
  render() {
    return (
      <div className="container">
        <EmployerInfo employer_info={this.props.employer_info} />
        <EmployerListings />
      </div>
    );
  }
}

ReactDOM.render(
  <EmployerProfile employer_info = {window.pageData.employerInfo} />,
  document.getElementById('react-placeholder')
);
