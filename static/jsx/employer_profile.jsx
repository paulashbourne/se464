var Profile = React.createClass({
  render: function() {

    return (
    	<div>St</div>
    );
  }
});


var Joblist = React.createClass({
  render: function() {

    return (
    	<div>
    		
    	</div>
    );
  }
});


var EmployerProfile = React.createClass({
  render: function() {
    return (
      <div className="container">
        <Profile />
        <JobList />
      </div>
    );
  }
});


ReactDOM.render(
    <EmployerProfile />,
    document.getElementById('react-placeholder')
    );
