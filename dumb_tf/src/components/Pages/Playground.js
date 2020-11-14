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
import Network from "../playground-src/neuralNode";

const lr = [
  {
    label: "0.00001",
  },
  {
    label: "0.0001",
  },
  {
    label: "0.001",
  },
  {
    label: "0.003",
  },
  {
    label: "0.01",
  },
  {
    label: "0.03",
  },
  {
    label: "0.1",
  },
  {
    label: "0.3",
  },
  {
    label: "1",
  },
  {
    label: "3",
  },
  {
    label: "10",
  },
];

export default class Playground extends Component {
  constructor() {
    super();
    this.state = {
      learningRate: lr[0].label,
      numNodes: 1,
      nodes: [],
      nodesBegin: [],
      nodesEnd: [],
      nodesDist: [],
      paths: [],
      filtered: [],
    };
  }

  handleChange(e) {
    this.setState({
      learningRate: e.target.value,
    });
  }

  render() {
    return (
      <div>
        <Grid
          container
          style={{ backgroundColor: "#eeeeee", height: "15vh", width: "100vw" }}
          alignItems="center"
        >
          <Grid item xs>
            <Toolbar>
              <IconButton>
                <Icon style={{ color: "#546e7a" }}>rotate_left_icon</Icon>
              </IconButton>
              <IconButton size="medium">
                <Icon style={{ color: "#546e7a", fontSize: 60 }}>
                  play_circle_filled_icon
                </Icon>
              </IconButton>
              <IconButton>
                <Icon style={{ color: "#546e7a" }}>skip_next_icon</Icon>
              </IconButton>
            </Toolbar>
          </Grid>
          <Grid item xs>
            <Typography
              style={{ fontSize: "0.8rem" }}
              variant="subtitle1"
              align="center"
              color="textSecondary"
            >
              Epoch
            </Typography>
            <Typography variant="h5" align="center">
              000,334
            </Typography>
          </Grid>
          <Grid item xs>
            <Typography
              style={{ fontSize: "0.8rem" }}
              variant="subtitle1"
              color="textSecondary"
            >
              Learning rate
            </Typography>
            <TextField
              select
              value={this.state.learningRate}
              onChange={(e) => this.handleChange(e)}
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
              style={{ fontSize: "0.8rem" }}
              variant="subtitle1"
              color="textSecondary"
            >
              Activation
            </Typography>
            <TextField
              select
              value={this.state.learningRate}
              onChange={(e) => this.handleChange(e)}
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
              style={{ fontSize: "0.8rem" }}
              variant="subtitle1"
              color="textSecondary"
            >
              Regularization
            </Typography>
            <TextField
              select
              value={this.state.learningRate}
              onChange={(e) => this.handleChange(e)}
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
              style={{ fontSize: "0.8rem" }}
              variant="subtitle1"
              color="textSecondary"
            >
              Regularization rate
            </Typography>
            <TextField
              select
              value={this.state.learningRate}
              onChange={(e) => this.handleChange(e)}
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
              style={{ fontSize: "0.8rem" }}
              variant="subtitle1"
              color="textSecondary"
            >
              Problem type
            </Typography>
            <TextField
              select
              value={this.state.learningRate}
              onChange={(e) => this.handleChange(e)}
            >
              {lr.map((option) => (
                <MenuItem key={option.label} value={option.label}>
                  {option.label}
                </MenuItem>
              ))}
            </TextField>
          </Grid>
        </Grid>
        <div style={{ textAlign: "center", marginTop: "2px" }}>
          <IconButton size="small">
            <Icon style={{ color: "#546e7a", fontSize: 25 }}>
              add_circle_icon
            </Icon>
          </IconButton>
          <IconButton size="small">
            <Icon style={{ color: "#546e7a", fontSize: 25 }}>
              remove_circle_icon
            </Icon>
          </IconButton>
          <Network />
        </div>
      </div>
    );
  }
}
