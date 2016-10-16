class NewEmployerProfile extends React.Component {
  constructor(props) {
    super(props);    
  }

  render() {
    return (
      <form>
        <label>Employer Name</label><br/>
        <input type="text" /><br/>
        <label>Employer Description</label><br/>
        <input type="text" /><br/>
        <label>Employer Website</label><br/>
        <input type="text" /><br/>
        <label>E-mail</label><br/>
        <input type="text" /><br/>
        <label>Job Descriptions</label><br/>
        <textarea rows="5" cols="50" /><br/>
        <input type="submit" name="submit" value="Submit" />
      </form>
    );
  }
}

ReactDOM.render(
    
    <NewEmployerProfile />,
    document.getElementById('react-placeholder')
    );