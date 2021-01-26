import React, { Component } from "react";
import { Grid, IconButton, Icon } from "@material-ui/core";
import Node from "../playground-src/Node";

export default class Layer extends Component {
  constructor() {
    super();
    var nodeRefs = [React.createRef(), React.createRef()];
    this.state = {
      name: null,
      nodesCount: 2,
      nodes: [
        this.addNodeComp("node:1", nodeRefs[0]),
        this.addNodeComp("node:2", nodeRefs[1]),
      ],
      nodeRefs: nodeRefs,
      nodeState: [],
    };
  }

  addNodeComp(name, ref) {
    return <Node name={name} ref={ref}></Node>;
  }

  addNode() {
    var stateObject = {};
    stateObject["nodesCount"] = Math.min(10, this.state.nodesCount + 1);
    if (stateObject["nodesCount"] < 10) {
      var nodes = this.state.nodes;
      var nodeRefs = this.state.nodeRefs;

      var newNodeRef = React.createRef();
      var newNodeName = "node:" + stateObject["nodesCount"];

      nodes.push(this.addNodeComp(newNodeName, newNodeRef));
      nodeRefs.push(newNodeRef);

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

  render() {
    console.log(this.state.nodeState);
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
            style={{
              //backgroundColor: "#ffc8ea",
              height: "5vh",
              width: "10vw",
            }}
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

          <Grid
            item
            style={
              {
                //backgroundColor: "#f46e7f"
              }
            }
          >
            {this.state.nodes.map((node, index) => (
              <React.Fragment key={index}>{node}</React.Fragment>
            ))}
          </Grid>
          {}
        </Grid>
      </div>
    );
  }
}
