import React, { Component } from "react";
import { Grid, IconButton, Icon, Typography } from "@material-ui/core";
import Layer from "../playground-src/Layer";

export default class Network extends Component {
  constructor() {
    super();
    var inputLayerRef = React.createRef();
    var outputLayerRef = React.createRef();

    this.state = {
      inputLayer: [this.addLayerComp("inputLayer", inputLayerRef)],
      outputLayer: [this.addLayerComp("outputLayer", outputLayerRef)],
      inputLayerRef: inputLayerRef,
      outputLayerRef: outputLayerRef,

      hidLayers: [],
      hidLayersCount: 0,
      hidLayersRefs: [],

      edges: [],
      edgesRendered: false,
    };
  }

  addLineComp(x1, x2, y1, y2) {
    return <line x1={x1} y1={y1} x2={x2} y2={x2} stroke="black"></line>;
  }

  computeEdges() {
    // Layers have been mounted, compute the edges

    var edges = [];

    if (this.state.hidLayers.length > 0) {
      this.state.hidLayers.map((layer, index) => {
        if (index === 0) {
          // Make lines with input layer

          console.log(this.state.inputLayerRef.current);
        }

        if (index === this.state.hidLayers.length - 1) {
          // Make lines with output layer
        } else {
          // Inter hidden layer connections
        }
      });
    } else {
      // No  hidden layers; just connect input and output layers
      var ipNodeRefs = this.state.inputLayerRef.current.state.nodeRefs;
      var opNodeRefs = this.state.outputLayerRef.current.state.nodeRefs;

      // STUPID JS BUG AHEAD
      // STATE VALUE CHANGES ON ACCESSING THEM
      // SCHRODINGER MUST BE HAPPY

      for(let i=0; i<ipNodeRefs.length; i++) {
        console.log(ipNodeRefs[i].current);
        console.log(ipNodeRefs[i].current.state);
        for(let j=0; j<opNodeRefs.length; j++) {
          
        }
      }

      console.log(edges);
      this.setState({ edges: edges });
    }
  }

  renderLines() {
    return <svg>{this.state.edges}</svg>;
  }

  componentDidMount() {
    if (this.state.edges.length > 0) {
      if (!this.state.edgesRendered) {
        // Edges have been computed, render them; set edgesRendered = true
      } else {
        // Edges have already been rendered
      }
    } else {
      this.computeEdges();
    }
  }

  addLayerComp(name, ref) {
    return <Layer name={name} ref={ref}></Layer>;
  }

  addLayer() {
    var stateObject = {};
    stateObject["hidLayersCount"] = Math.min(6, this.state.hidLayersCount + 1);

    if (stateObject["hidLayersCount"] < 6) {
      var hidLayers = this.state.hidLayers;
      var hidLayersRefs = this.state.hidLayersRefs;

      var newLayerName = "hidLayer_" + stateObject["hidLayersCount"];
      var newLayerRef = React.createRef();

      hidLayers.push(this.addLayerComp(newLayerName, newLayerRef));
      hidLayersRefs.push(newLayerRef);

      stateObject["hidLayersRefs"] = hidLayersRefs;
      stateObject["hidLayers"] = hidLayers;

      // So that edges are recomputed
      stateObject["edges"] = [];
      stateObject["edgesRendered"] = false;
      this.setState(stateObject);
    }
  }

  removeLayer() {
    var stateObject = {};
    if (this.state.hidLayersCount > 0) {
      stateObject["hidLayersCount"] = this.state.hidLayersCount - 1;
      var hidLayers = this.state.hidLayers;
      var hidLayersRefs = this.state.hidLayersRefs;
      hidLayersRefs.pop();
      hidLayers.pop();
      stateObject["hidLayers"] = hidLayers;
      stateObject["hidLayersRefs"] = hidLayersRefs;

      // So that edges are recomputed
      stateObject["edges"] = [];
      stateObject["edgesRendered"] = false;
      this.setState(stateObject);
    }
  }

  render() {
    return (
      <div>
        <Grid
          container
          style={{
            //backgroundColor: "#ee3eee",
            height: "6vh",
            width: "100vw",
          }}
          justify="center"
          alignItems="center"
        >
          <Grid item xs>
            <IconButton onClick={() => this.addLayer()}>
              <Icon
                style={{
                  color: "#546e7a",
                }}
              >
                add_circle
              </Icon>
            </IconButton>
          </Grid>
          <Grid item xs>
            <IconButton onClick={() => this.removeLayer()}>
              <Icon
                style={{
                  color: "#546e7a",
                }}
              >
                remove_circle
              </Icon>
            </IconButton>
          </Grid>
          <Grid item xs>
            <Typography>
              {this.state.hidLayerCount} Hidden layerNames
            </Typography>
          </Grid>
        </Grid>
        <Grid
          container
          style={{
            height: "35vw",
            width: "100vw",
            //backgroundColor: "#4d164d",
          }}
          justify="center"
          alignItems="center"
        >
          {this.state.inputLayer}
          {this.state.hidLayers.map((layer, index) => (
            <React.Fragment key={index}>{layer}</React.Fragment>
          ))}
          {this.state.outputLayer}
          {/* {console.log(this.state.edges)}
          <svg>
            {this.state.edges.map((edge, index) => {
              return edge;
            })}
            <line x1="0" y1="0" x2="1000" y2="2000" stroke="black"></line>
          </svg> */}
          
        </Grid>
      </div>
    );
  }
}
