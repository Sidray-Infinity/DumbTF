import React, { Component } from "react";
import { Grid, IconButton, Icon } from "@material-ui/core";
import Node from "../playground-src/Node";

export default class Layer extends Component {
  constructor() {
    super();
    this.state = {
      nodesCount: 2,
      nodes: ["node_1", "node_2"],
    };
  }

  addNode() {
    var stateObject = {};
    stateObject["nodesCount"] = Math.min(10, this.state.nodesCount + 1);
    if (stateObject["nodesCount"] < 10) {
      var nodes = this.state.nodes;
      var newNodeName = "node_" + stateObject["nodesCount"];
      nodes.push(newNodeName);
      stateObject["nodes"] = nodes;
      this.setState(stateObject);
    }
  }

  removeNode() {
    var stateObject = {};
    stateObject["nodesCount"] = Math.max(0, this.state.nodesCount - 1);
    if (stateObject["nodesCount"] >= 1) {
      var nodes = this.state.nodes;
      nodes.pop();
      stateObject["nodes"] = nodes;
      this.setState(stateObject);
    }
  }

  render() {
    var allNodes = [];
    for (let i = 0; i < this.state.nodesCount; i++)
      allNodes.push(<Node name={this.props.name + "_" + this.state.nodes[i]}></Node>);

    return (
      <div>
        <Grid
          container
          style={{
            backgroundColor: "#90c8ea",
            height: "60vh",
            width: "10vw",
          }}
          justify="center"
        >
          <Grid
            justify="center"
            container
            style={{ backgroundColor: "#ffc8ea", height: "5vh", width: "10vw" }}
          >
            <Grid item>
              <IconButton onClick={() => this.addNode()}>
                <Icon
                  style={{
                    color: "#546e7a",
                  }}
                >
                  add_circle
                </Icon>
              </IconButton>
            </Grid>
            <Grid item>
              <IconButton onClick={() => this.removeNode()}>
                <Icon
                  style={{
                    color: "#546e7a",
                  }}
                >
                  remove_circle
                </Icon>
              </IconButton>
            </Grid>
          </Grid>

          <Grid item style={{ backgroundColor: "#f46e7f" }}>
            {allNodes}
          </Grid>
          {/* <Typography
            align="center"
            type="h1"
            style={{ transform: "rotate(270deg)" }}
          >
            {this.props.name}
          </Typography> */}
        </Grid>
      </div>
    );
  }
}
