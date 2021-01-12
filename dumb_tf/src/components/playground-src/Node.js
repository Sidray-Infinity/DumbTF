import React, { Component } from "react";

const rectangle = {
  display: "inline-block",
  width: "30px",
  height: "30px",
  background: "green",
}

export default class Node extends Component {
	render() {
		return (
			<div>
				<div style={rectangle}></div>
			</div>
		);
	} 
}
