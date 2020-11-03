import { Box } from "@material-ui/core";
import NavBar from "./components/NavBar";
import Page from "./components/Page";
function App() {
  return (
    <>
      <NavBar />
      <Box display="flex" justifyContent="center">
        <Page />
      </Box>
    </>
  );
}

export default App;
