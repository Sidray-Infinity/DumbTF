import React, { Component } from "react";
import { Grid } from "@material-ui/core";

export default class Node extends Component {

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
