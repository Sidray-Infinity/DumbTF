import Sketch from "react-p5";
import React, { Component } from "react";

export default class Network extends Component {
  constructor() {
    super();
    this.state = {
      numNodes: 4,
      nodes: [],
      nodesBegin: [],
      nodesEnd: [],
      nodesDist: [],
      paths: [],
      filtered: [],
    };
  }

  // TODO: Implement add-delete neurons functionality in buttons

  //   alterNumNodes(more) {
  //     if (!more && this.state.numNodes - 1 === 0) return;
  //     if (this.state.numNodes > 0) {
  //       more
  //         ? this.setState((state) => ({ numNodes: state.numNodes + 1 }))
  //         : this.setState((state) => ({ numNodes: state.numNodes - 1 }));
  //     }
  //   }

  render() {
    const { numNodes, nodes, nodesBegin, nodesEnd, nodesDist } = this.state;
    return (
      <div>
        <Sketch
          setup={(p5, parentRef) => {
            p5.createCanvas(600, 400).parent(parentRef);
            p5.frameRate(20);
            p5.noStroke();
            for (let i = 0; i < this.state.numNodes; i++)
              this.state.nodes.push(
                new Node(p5, numNodes, nodes, nodesBegin, nodesEnd, nodesDist)
              );
          }}
          draw={(p5) => {
            p5.fill(0, 10);
            p5.rect(0, 0, p5.width, p5.height);
            this.state.nodes.forEach((node, idx) => {
              node.draw(p5);
              node.distBetweenNode(p5, nodes.slice(idx), idx);
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
