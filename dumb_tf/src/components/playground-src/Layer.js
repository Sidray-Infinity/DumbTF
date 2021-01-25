import React, { Component } from "react";
import { Grid, IconButton, Icon } from "@material-ui/core";
import Node from "../playground-src/Node";

export default class Layer extends Component {
  state = {
    name: this.props.name,
    nodesCount: 2,
    nodes: ["node:1", "node:2"],
    nodeRefs: [React.createRef(), React.createRef()],
    nodeState: []
  };

  addNode() { // should we store node component here?
    var stateObject = {};
    stateObject["nodesCount"] = Math.min(10, this.state.nodesCount + 1);
    if (stateObject["nodesCount"] < 10) {
      var nodes = this.state.nodes;
      var nodeRefs = this.state.nodeRefs;
      var newNodeName = "node:" + stateObject["nodesCount"];
      nodes.push(newNodeName);
      nodeRefs.push(React.createRef());
      stateObject["nodes"] = nodes;
      stateObject["nodeRefs"] = nodeRefs;
      this.setState(stateObject);
    }
  }

  removeNode() {
    var stateObject = {};
    stateObject["nodesCount"] = Math.max(0, this.state.nodesCount - 1);
    if (stateObject["nodesCount"] >= 1) {
      var nodes = this.state.nodes;
      var nodeRefs = this.state.nodeRefs;
      nodes.pop();
      nodeRefs.pop();
      stateObject["nodes"] = nodes;
      stateObject["nodeRefs"] = nodeRefs;
      this.setState(stateObject);
    }
  }

  // componentDidMount() {
  //   console.log(this.state.name);
  //   this.state.nodeRefs.forEach((x, i) => {
  //     console.log(x.current);
  //   });
  // }

  render() {
    var allNodes = [];
    for (let i = 0; i < this.state.nodesCount; i++)
      allNodes.push(
        <Node
          name={this.props.name + "-" + this.state.nodes[i]}
          ref={this.state.nodeRefs[i]}
        ></Node>
      );

    return (
      <div>
        <Grid
          container
          style={{
            //backgroundColor: "#90c8ea",
            height: "60vh",
            width: "10vw",
          }}
          justify="center"
        >
          <Grid
            justify="center"
            container
            style={{ //backgroundColor: "#ffc8ea",
            height: "5vh", width: "10vw" }}
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

          <Grid item style={{ //backgroundColor: "#f46e7f"
          }}>
            {allNodes}
          </Grid>
          {}
        </Grid>
      </div>
    );
  }
}
