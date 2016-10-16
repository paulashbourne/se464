var JobSearchPage = React.createClass({
  getInitialState: function() {
    return { results: undefined };
  },

  handleSearch: function() {
    console.log("Searching...");
    var that = this;
    $.get("/api/jobs", function(results) {
      that.setState({'results': $.parseJSON(results)});
    });
  },

  render: function() {
    var results = <div></div>;
    console.log(this.state.results);
    if (this.state.results) {
    console.log(this.state.results.length);
      results = (
        <div>
          Showing {this.state.results.length} results
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
             <input className="mb20 full-width" placeholder="Company" />
             <div className="secondary-header">
               Where would you like to work?
              </div>
              <input className="full-width" placeholder="Location" />
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
