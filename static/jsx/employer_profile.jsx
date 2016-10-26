


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
  	console.log(this.props.employer_info[0]);
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
             <div className="mb20 full-width primary-header">{this.props.employer_info[0].company_name}</div>
            <div className="col-md-2 secondary-header">
              E-mail
             </div>
             <div className="mb20 full-width primary-header">{this.props.employer_info[0].emails}</div>
            <div className="col-md-2 secondary-header">
              Website
             </div>
             <div className="mb20 full-width primary-header">{this.props.employer_info[0].website}</div>
            <div className="col-md-2 secondary-header">
              Description
             </div>
             <div className="mb20 full-width primary-header">{this.props.employer_info[0].description}</div>
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
            test
          </div>
        </div>
      </div>
    );
  }
}


var EmployerProfile = React.createClass({
  render: function() {
    return (
      <div className="container">
        <EmployerInfo employer_info={this.props.employer_info} />
        <EmployerListings />
      </div>
    );
  }
});


ReactDOM.render(
    <EmployerProfile employer_info = {window.pageData.employerInfo} />,
    document.getElementById('react-placeholder')
    );