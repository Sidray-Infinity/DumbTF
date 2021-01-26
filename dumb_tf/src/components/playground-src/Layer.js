import React, { Component } from "react";
import { Grid, IconButton, Icon } from "@material-ui/core";
import Node from "../playground-src/Node";

export default class Layer extends Component {

  state = {
    name: this.props.name,
    nodesCount: 2,
    nodes: ["node:1", "node:2"],
    nodeRefs: [React.createRef(), React.createRef()],
    nodePosition: [],
  };


  // calculateNodePosition and append in nodePosition[]
  // fn(){

  //}

  addNode() { // should we store node component here?

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


    return (
      // state = nodeCount, which we get from props above
      // for(node in nodeCount)
      // return <svg><Node calcNodePos={fn}/></svg>

    );
  }
}
