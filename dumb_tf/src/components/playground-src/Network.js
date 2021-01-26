import React, { Component } from "react";
import { Grid, IconButton, Icon, Typography } from "@material-ui/core";
import Layer from "../playground-src/Layer";

export default class Network extends Component {

  // constructor() {
  //   super();
  //   var inputLayerRef = React.createRef();
  //   var outputLayerRef = React.createRef();

  //   this.state = {
  //     inputLayer: [this.addLayerComp("inputLayer", inputLayerRef)], // so this is a list of layer components
  //     outputLayer: [this.addLayerComp("outputLayer", outputLayerRef)],
  //     inputLayerRef: inputLayerRef,
  //     outputLayerRef: outputLayerRef,

  //     hidLayers: [],
  //     hidLayersCount: 0,
  //     hidLayersRefs: [],

  //     edges: [],
  //     edgesRendered: false,

  //     nodeStates:[]
  //   };
  // }

  // addLineComp(x1, x2, y1, y2) {
  //   return <line x1={x1} y1={y1} x2={x2} y2={x2} stroke="black"></line>;
  // }

  // computeEdges() {
  //   // Layers have been mounted, compute the edges

  //   var edges = [];

  //   if (this.state.hidLayers.length > 0) {
  //     this.state.hidLayers.map((layer, index) => {
  //       if (index === 0) {
  //         // Make lines with input layer

  //         console.log(this.state.inputLayerRef.current);
  //       }

  //       if (index === this.state.hidLayers.length - 1) {
  //         // Make lines with output
  //       } else {
  //         // Inter hidden layer connections
  //       }
  //     });
  //   } else {
  //     // No  hidden layers; just connect input and output layers
  //     var ipNodeRefs = this.state.inputLayerRef.current.state.nodeRefs;
  //     var opNodeRefs = this.state.outputLayerRef.current.state.nodeRefs;
  //     const nodeStates = [];

  //     // calculate position of node by name for input layer
  //     for(let i=0; i<ipNodeRefs.length; i++)
  //       nodeStates.push( this.calculateNodePositionByName(ipNodeRefs[i].current.props.name))
  //     for(let j=0; j<opNodeRefs.length; j++)
  //       nodeStates.push( this.calculateNodePositionByName(opNodeRefs[j].current.props.name))

  //     this.setState({ edges: edges, nodeStates:nodeStates });
  //   }
  // }

  // calculateNodePositionByName(name){
    // const { x, y } = document
    // .getElementById(name)
    // .getBoundingClientRect();

    // const {x,y} = getSvgCoordinates(); - MAPPING FUNCTION TO MAP DOCUMENT COORDINATES TO PARENT SVG COORDINATES

    // WORST CASE SCENARIO
    // ------------------
    // If state is not accessible where the line is to be drawn, calc. lines using number of layers
    // and the array of no. of nodes in Playground.js


  //   const nodeStateObject = {
  //     x,
  //     y,
  //     name
  //   }
  //   console.log(nodeStateObject)
  //   return nodeStateObject
  // }

  // renderLines() {
  //   return <svg>{this.state.edges}</svg>;
  // }

  // componentDidMount() {
  //   if (this.state.edges.length > 0) {
  //     if (!this.state.edgesRendered) {
  //       // Edges have been computed, render them; set edgesRendered = true
  //     } else {
  //       // Edges have already been rendered
  //     }
  //   } else {
  //     this.computeEdges();
  //   }
  // }

  // addLayerComp(name, ref) {
  //   return <Layer name={name} ref={ref}></Layer>;
  // }

  // addLayer() {
  //   var stateObject = {};
  //   stateObject["hidLayersCount"] = Math.min(6, this.state.hidLayersCount + 1);

  //   if (stateObject["hidLayersCount"] < 6) {
  //     var hidLayers = this.state.hidLayers;
  //     var hidLayersRefs = this.state.hidLayersRefs;

  //     var newLayerName = "hidLayer_" + stateObject["hidLayersCount"];
  //     var newLayerRef = React.createRef();

  //     hidLayers.push(this.addLayerComp(newLayerName, newLayerRef));
  //     hidLayersRefs.push(newLayerRef);

  //     stateObject["hidLayersRefs"] = hidLayersRefs;
  //     stateObject["hidLayers"] = hidLayers;

  //     // So that edges are recomputed
  //     stateObject["edges"] = [];
  //     stateObject["edgesRendered"] = false;
  //     this.setState(stateObject);
  //   }
  // }

  // removeLayer() {
  //   var stateObject = {};
  //   if (this.state.hidLayersCount > 0) {
  //     stateObject["hidLayersCount"] = this.state.hidLayersCount - 1;
  //     var hidLayers = this.state.hidLayers;
  //     var hidLayersRefs = this.state.hidLayersRefs;
  //     hidLayersRefs.pop();
  //     hidLayers.pop();
  //     stateObject["hidLayers"] = hidLayers;
  //     stateObject["hidLayersRefs"] = hidLayersRefs;

  //     // So that edges are recomputed
  //     stateObject["edges"] = [];
  //     stateObject["edgesRendered"] = false;
  //     this.setState(stateObject);
  //   }
  // }

  render() {

    {/*

      // show i/p layer


      if(props.layers>0){
        // show  hidden layer
      }

      // show o/p layer

    */}

    return (
      // Layer
      // Return <svg height={} width={}><Layer name={input} nodeCount={}/></svg>
      // Return <svg height={} width={}><Layer name={hidden} nodeCount={}/></svg>
      // Return <svg height={} width={}><Layer name={output} nodeCount={}/></svg>

      // <svg /** svg for i/p layer */>
          //   <line x1="100" y1="0" x2="1000" y2="2000" stroke="black"/ >
          // </svg>


          // {/* dynamic hidden layers generated based on props */}

          // <svg /** svg for o/p layer */>
          //   <line x1="100" y1="0" x2="1000" y2="2000" stroke="black"/ >
          // </svg>
    //);

    );
  }
}
