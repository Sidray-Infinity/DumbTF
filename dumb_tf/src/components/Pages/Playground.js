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
import Network from "../playground-src/Network";

export default class Playground extends Component {
  constructor() {
    super();
    this.state = {
      learningRate: lr[0].label,
      activation: act[0].label,
      problemType: probType[0].label,
      networkRef: React.createRef(),
    };
  }

  renderLines() {
    var lines = [];
    // for (let i = 1; i < this.state.layerRefs.length; i++) {
    //   var currNodes = this.state.layerRefs[i].current.state.nodeRefs;
    //   var prevNodes = this.state.layerRefs[i - 1].current.state.nodeRefs;

    //   for (let j = 0; j < currNodes.length; j++) {
    //     var { x1, y1 } = currNodes[j].current.state;
    //     for (let k = 0; j < prevNodes.length; k++) {
    //       var { x2, y2 } = prevNodes[k].current.state;
    //       lines.append(<line x1={x1} y1={y1} x2={x2} y2={y2} stroke="black" />);
    //     }
    //   }
    // }

    return lines;
  }

  handleChange(e, field) {
    var stateObject = {};
    stateObject[field] = e.target.value;
    this.setState(stateObject);
  }

  render() {
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
          
          {/* DEFINING NETWORK */}
          <Network ref={this.state.networkRef}></Network>
          {console.log(this.state.networkRef)}
        </Grid>
      </div>
    );
  }
}
