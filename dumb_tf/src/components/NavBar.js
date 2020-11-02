import Button from "@material-ui/core/Button";
import {
  Toolbar,
  IconButton,
  Typography,
  AppBar,
  Icon,
  Hidden,
  SwipeableDrawer,
  List,
  ListItem,
  ListItemText,
} from "@material-ui/core";
import { useState } from "react";
import { Link } from "react-router-dom";
function NavBar() {
  const [isOpen, setOpen] = useState(false);
  const navBarOptions = [
    {
      title: "EXPLORE",
      to: "/playground",
    },
    {
      title: "LEARN",
      to: "/learn",
    },
    {
      title: "GET STARTED",
      to: "/get-started",
    },
  ];
  return (
    <div>
      <AppBar position="static" color="#bcbcbc" variant="outlined">
        <Toolbar>
          <Hidden smUp>
            <IconButton
              edge="start"
              color="inherit"
              aria-label="menu"
              onClick={() => setOpen(true)}
            >
              <Icon>menu</Icon>
            </IconButton>
          </Hidden>
          <Typography variant="h6" style={{ flex: 1 }}>
            DumbTF
          </Typography>
          <Hidden xsDown>
            {navBarOptions.map((item) => (
              <Link
                to={item.to}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <Button color="inherit">{item.title}</Button>
              </Link>
            ))}
          </Hidden>
        </Toolbar>
      </AppBar>
      {/*  Drawer  */}

      <SwipeableDrawer
        open={isOpen}
        anchor="left"
        onClose={() => setOpen(false)}
        onOpen={() => setOpen(true)}
      >
        {navBarOptions.map((item) => (
          <List>
            <ListItem button>
              <Link
                style={{ textDecoration: "none", color: "inherit" }}
                to={item.to}
              >
                <ListItemText primary={item.title} />
              </Link>
            </ListItem>
          </List>
        ))}
      </SwipeableDrawer>
    </div>
  );
}
export default NavBar;
