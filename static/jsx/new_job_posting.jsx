class NewJobForm extends React.Component {
  constructor(props) {
    super(props);    
  }

  createJob() {
    console.log("Adding Job...");
    var that = this;
    var jobTitle = $('#title-input').val();
    var numOpenings = $('#openings-input').val();
    var jobLocation = $('#location-input').val();
    var jobDescription = $('#description-input').val();
    var postData = {employer_id: 1, 
                    position: jobTitle, 
                    description: jobDescription, 
                    location: jobLocation,   
                    openings: numOpenings };
    console.log(postData);
    $.post('/api/jobs' , JSON.stringify(postData) , function() {
        console.log("Added Job!");
      });
  }


  render() {
    return (

      <div className="container">
        <form>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <span className="search-title">
              New Job Posting
             </span>
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <div className="secondary-header">
              Job Title
             </div>
             <input id="title-input" className="mb20 full-width" />
             <div className="secondary-header">
               Number of Openings
              </div>
              <input id="openings-input" type="number" className="full-width"/>
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <div className="secondary-header">
              Job Location
             </div>
             <input id="location-input" className="mb20 full-width" />
             <div className="secondary-header">
               Job Description
              </div>
              <textarea id="description-input" className="full-width" />
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
          <button type="button" onClick={this.createJob}>Create Job</button>
          </div>
        </div>
        </form>
      </div>
    );
  }
}

ReactDOM.render(
    <NewJobForm />,
    document.getElementById('react-placeholder')
    );