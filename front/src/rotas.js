import React from "react";
import { Route, BrowserRouter } from "react-router-dom";
import Body from '../src/componentes/Body'
import Relatorio from '../src/componentes/relatorio'
// import 'index.css'
const Routes = () => {
    return(
        <BrowserRouter>
            <Route component = { Body } path="/home"/>
            <Route component = { Relatorio }  path="/relatorio" />
        </BrowserRouter>
    )
 }
 export default Routes;