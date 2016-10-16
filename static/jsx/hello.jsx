var CommentBox = React.createClass({
  render: function() {
    return (
        <div className="commentBox">
        Hello, world! I am a CommentBox.
        {this.props.student_info.name}
        </div>
        );
  }
});
ReactDOM.render(
    <CommentBox student_info = { window.pageData.studentInfo } />,
    document.getElementById('react-placeholder')
    );
