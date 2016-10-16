var CommentBox = React.createClass({
  displayName: "CommentBox",

  render: function () {
    return React.createElement(
      "div",
      { className: "commentBox" },
      "Hello, world! I am a CommentBox.",
      this.props.student_info.name
    );
  }
});
ReactDOM.render(React.createElement(CommentBox, { student_info: window.pageData.studentInfo }), document.getElementById('react-placeholder'));