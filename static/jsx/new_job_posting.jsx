class NewJobForm extends React.Component {
  constructor(props) {
    super(props);    
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
             <input className="mb20 full-width" />
             <div className="secondary-header">
               Number of Openings
              </div>
              <input type="number" className="full-width" value="1"/>
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <div className="secondary-header">
              Job Title
             </div>
             <input className="mb20 full-width" />
             <div className="secondary-header">
               Job Description
              </div>
              <textarea className="full-width" />
          </div>
        </div>
        <div className="row mb20">
          <div className="col-md-offset-2 col-md-8">
            <input type="submit" type="button" value="Create Job"/>
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