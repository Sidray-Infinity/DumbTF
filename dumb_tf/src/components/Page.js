import React from 'react';
import {Switch,Route} from "react-router-dom";
import GetStarted from "./Pages/GetStarted";
import Learn from "./Pages/Learn";
import Playground from "./Pages/Playground";
import Home from "./Pages/Home";

function Page() {
    return (
            <Switch>
                <Route path="/" exact component={Home}/>
                <Route path="/playground" exact component={Playground}/>
                <Route path="/get-started" exact component={GetStarted}/>
                <Route path="/learn" exact component={Learn}/>
            </Switch>
    )
}

export default Page;