
var EmployerProfile = React.createClass({
  render: function() {
    return (
      <div className="container">
        <EmployerInfo />
        <EmployerListings />
      </div>
    );
  }
});


class EmployerInfo extends React.Component {
  constructor(props) {
    super(props);    
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
             <div className="mb20 full-width">this.props.employer.name</div>
            <div className="col-md-2 secondary-header">
              E-mail
             </div>
             <div className="mb20 full-width">this.props.employer.email</div>
            <div className="col-md-2 secondary-header">
              Website
             </div>
             <div className="mb20 full-width">this.props.employer.website</div>
            <div className="col-md-2 secondary-header">
              Description
             </div>
             <div className="mb20 full-width">this.props.employer.description</div>
          </div>
        </div>
      </div>
    );
  }
}

class EmployerListings extends React.Component {
  constructor(props) {
    super(props);    
  }

  render() {
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
            { results }
          </div>
        </div>
      </div>
    );
  }
}

ReactDOM.render(
    <EmployerProfile />,
    document.getElementById('react-placeholder')
    );