class NewEmployerProfile extends React.Component {
  constructor(props) {
    super(props);    
  }

  render() {
    return (
      <form>
        <label>Employer Name</label>
        <input type="text" />
        <label>Employer Description</label>
        <input type="text" />
        <label>Employer Website</label>
        <input type="text" />
        <label>E-mail</label>
        <input type="text" />
        <label>Job Descriptions</label>
        <textarea rows="5" cols="50" />
        <input type="submit" name="submit" value="Submit" />
      </form>
    );
  }
}

ReactDOM.render(
    
    <NewJobForm />,
    document.getElementById('react-placeholder')
    );