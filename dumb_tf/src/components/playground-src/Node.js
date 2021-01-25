import React, { Component } from "react";
import { Grid } from "@material-ui/core";

export default class Node extends Component {

  constructor() {
    super();
    this.state = {
      name: null,
      x: -1,
      y: -1,
    };
  }
  

  componentDidMount() {
    const { x, y } = document
      .getElementById(this.props.name)
      .getBoundingClientRect();
    this.setState({ x: x, y: y, name: this.props.name });
  }

  render() {
    return (
      <div id={this.props.name}>
        {/* <div id={this.props.name} style={rectangle}></div> */}
        <Grid container style={{ width: "30px", height: "40px" }}>
          <svg>
            <rect
              width="30"
              height="30"
              rx="7"
              fill="transparent"
              stroke-width="5"
              stroke="black"
            ></rect>
          </svg>
        </Grid>
      </div>
    );
  }
}
