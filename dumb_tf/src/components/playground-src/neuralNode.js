import Sketch from "react-p5";
import React, { Component } from "react";
var nodesCopy = [];

export default class Network extends Component {
  constructor() {
    super();
    this.state = {
      paths: [],
      filtered: [],
      nodes: [],
    };
  }

  componentDidUpdate() {
    var {
      numNodes,
      nodes,
      nodesBegin,
      nodesEnd,
      nodesDist,
    } = this.props.params;
    nodesCopy = [];
    for (let i = 0; i < numNodes; i++)
      nodesCopy.push(
        new Node(
          window.p5Global,
          numNodes,
          nodes,
          nodesBegin,
          nodesEnd,
          nodesDist
        )
      );
  }

  render() {
    console.log(this.props.params.numNodes);
    return (
      <div>
        <Sketch
          setup={(p5, parentRef) => {
            p5.createCanvas(600, 400).parent(parentRef);
            p5.frameRate(20);
            p5.noStroke();
            window.p5Global = p5;
          }}
          draw={(p5) => {
            p5.fill(0, 10);
            p5.rect(0, 0, p5.width, p5.height);
            nodesCopy.forEach((node, idx) => {
              node.draw(p5);
              node.distBetweenNode(p5, nodesCopy.slice(idx), idx);
            });
          }}
        />
      </div>
    );
  }
}

class Node {
  constructor(p5, nn, n, nb, ne, nd) {
    this.pos = p5.createVector(
      Math.floor(Math.random() * 300),
      Math.floor(Math.random() * 200)
    );
    this.size = 40;
    this.numNodes = nn;
    this.nodes = n;
    this.nodesBegin = nb;
    this.nodesEnd = ne;
    this.nodesDist = nd;
  }

  draw(p5) {
    p5.fill("orange");
    p5.noStroke();
    p5.circle(this.pos.x, this.pos.y, this.size);
  }

  distBetweenNode(p5, nodes, idx) {
    let distance;
    nodes.forEach((node) => {
      if (this.nodesBegin.length <= this.nodes.length)
        this.nodesBegin.push({
          x: node.pos.x,
          y: node.pos.y,
        });
      distance = p5.dist(this.pos.x, this.pos.y, node.pos.x, node.pos.y);
      if (distance !== 0 && distance > this.size) {
        if (this.nodesEnd.length !== this.nodes.length - 1) {
          this.nodesEnd.push({
            x: node.pos.x,
            y: node.pos.y,
          });
        }
      }
    });
  }
}
