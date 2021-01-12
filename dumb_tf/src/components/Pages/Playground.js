import React, { Component } from "react";
import {
  Toolbar,
  IconButton,
  Icon,
  Typography,
  Grid,
  TextField,
  MenuItem,
} from "@material-ui/core";
import { lr, act, probType } from "../playground-src/dropDownData";
import Layer from "../playground-src/Layer";

export default class Playground extends Component {
  constructor() {
    super();
    this.state = {
      learningRate: lr[0].label,
      activation: act[0].label,
      problemType: probType[0].label,
      hidLayers: [],
      hidLayerCount: 0,
    };
  }

  handleChange(e, field) {
    var stateObject = {};
    stateObject[field] = e.target.value;
    this.setState(stateObject);
  }

  addLayer() {
    var stateObject = {};
    stateObject["hidLayerCount"] = Math.min(6, this.state.hidLayerCount + 1);

    if (stateObject["hidLayerCount"] < 6) {
      var hidLayers = this.state.hidLayers;
      var newLayerName = "hidden_layer_" + stateObject["hidLayerCount"];
      hidLayers.push(newLayerName);
      stateObject["hidLayers"] = hidLayers;
      this.setState(stateObject);
    }
  }

  removeLayer() {
    var stateObject = {};
    stateObject["hidLayerCount"] = Math.max(0, this.state.hidLayerCount - 1);
    if (stateObject["hidLayerCount"] >= 0) {
      var hidLayers = this.state.hidLayers;
      hidLayers.pop();
      stateObject["hidLayers"] = hidLayers;
      this.setState(stateObject);
    }
  }

  render() {
    var hiddenLayers = [];
    for (let i = 0; i < this.state.hidLayers.length; i++)
      hiddenLayers.push(<Layer name={this.state.hidLayers[i]}></Layer>);

    return (
      <div>
        <Grid container alignItems="center" spacing={2}>
          <Grid
            container
            style={{
              backgroundColor: "#eeeeee",
              height: "15vh",
              width: "100vw",
            }}
            alignItems="center"
          >
            <Grid item xs>
              <Toolbar>
                <IconButton>
                  <Icon
                    style={{
                      color: "#546e7a",
                    }}
                  >
                    rotate_left_icon
                  </Icon>
                </IconButton>
                <IconButton size="medium">
                  <Icon
                    style={{
                      color: "#546e7a",
                      fontSize: 60,
                    }}
                  >
                    play_circle_filled_icon
                  </Icon>
                </IconButton>
                <IconButton>
                  <Icon
                    style={{
                      color: "#546e7a",
                    }}
                  >
                    skip_next_icon
                  </Icon>
                </IconButton>
              </Toolbar>
            </Grid>

            <Grid item xs>
              <Typography
                style={{
                  fontSize: "0.8rem",
                }}
                variant="subtitle1"
                align="center"
                color="textSecondary"
              >
                Epoch
              </Typography>
              <Typography variant="h5" align="center">
                000, 334
              </Typography>
            </Grid>

            <Grid item xs>
              <Typography
                style={{
                  fontSize: "0.8rem",
                }}
                variant="subtitle1"
                color="textSecondary"
              >
                Learning rate
              </Typography>
              <TextField
                select
                value={this.state.learningRate}
                onChange={(e) => this.handleChange(e, "learningRate")}
              >
                {lr.map((option) => (
                  <MenuItem key={option.label} value={option.label}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>

            <Grid item xs>
              <Typography
                style={{
                  fontSize: "0.8rem",
                }}
                variant="subtitle1"
                color="textSecondary"
              >
                Activation
              </Typography>
              <TextField
                select
                value={this.state.activation}
                onChange={(e) => this.handleChange(e, "activation")}
              >
                {act.map((option) => (
                  <MenuItem key={option.label} value={option.label}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>

            <Grid item xs>
              <Typography
                style={{ fontSize: "0.8rem" }}
                variant="subtitle1"
                color="textSecondary"
              >
                Problem type
              </Typography>
              <TextField
                select
                value={this.state.problemType}
                onChange={(e) => this.handleChange(e, "problemType")}
              >
                {probType.map((option) => (
                  <MenuItem key={option.label} value={option.label}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
          </Grid>

          {/* DEFINING LAYERS */}

          <Grid
            container
            style={{
              backgroundColor: "#ee3eee",
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
              <Typography>{this.state.hidLayerCount} Hidden Layers</Typography>
            </Grid>
          </Grid>
          <Grid
            container
            style={{
              height: "35vw",
              width: "100vw",
              backgroundColor: "#4d164d",
            }}
            
            justify="center"
            alignItems="center"
          >
            <Layer name="input_layer"></Layer>
            {hiddenLayers}
            <Layer name="output_layer"></Layer>
          </Grid>
        </Grid>
      </div>
    );
  }
}
