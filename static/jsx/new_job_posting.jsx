class NewJobForm extends React.Component {
  constructor(props) {
    super(props);    
  }

  render() {
    return (
      <form>
        <label>Job Name</label><br/>
        <input type="text" /><br/>
        <label>Number of Openings</label><br/>
        <input type="number" /><br/>
        <label>Job Descriptions</label><br/>
        <textarea rows="5" cols="50" /><br/>
        <input type="submit" name="submit" value="Create Job" />
      </form>
    );
  }
}

ReactDOM.render(
    <NewJobForm />,
    document.getElementById('react-placeholder')
    );