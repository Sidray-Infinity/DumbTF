import React, { Component } from "react";
import { Grid } from "@material-ui/core";

const rectangle = {
  display: "inline-block",
  width: "30px",
  height: "30px",
  background: "green",
};

export default class Node extends Component {
  // componentDidMount() {
  //   if (this.props.name === "output_layer_node_1") {
  //     var ele = document.getElementById("input_layer_node_1");
  //     console.log(this.props.name);
  //     console.log(ele.getBoundingClientRect());
  //   }
  // }

  render() {
    // console.log(this.props.name);

    return (
      <div>
        {/* <div id={this.props.name} style={rectangle}></div> */}
        <Grid container style={{ width: "30px", height: "50px" }}>
          <svg>
            <rect width="30" height="30" rx="2"></rect>
          </svg>
        </Grid>
      </div>
    );
  }
}
