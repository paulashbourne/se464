var JobSearchPage = React.createClass({
  handleSearch: function() {
    console.log("Searching...");
    $.get("/api/jobs", function(result) {
      console.log(result);
    });
  },

  render: function() {
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
             <input className="mb20 full-width" placeholder="Company" />
             <div className="secondary-header">
               Where would you like to work?
              </div>
              <input className="full-width" placeholder="Location" />
          </div>
        </div>
        <div className="row">
          <div className="col-md-offset-2 col-md-8">
            <button type="button" onClick={this.handleSearch}>Search</button>
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
