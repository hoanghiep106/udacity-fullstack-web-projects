import React from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom';
import history from 'utils/history';
// App shell
import Header from 'components/Header';
// Pages
import Catalogs from 'pages/Catalogs';
import Items from 'pages/Items';


const Container = () => (
  <Router history={history}>
    <div>
      <Header />
      <Switch>
        <Route path="/catalogs/:id" name="Catalog items" component={Items} />
        <Route path="/catalogs" name="Catalogs" component={Catalogs} />
        <Redirect from="/" to="/catalogs" />
      </Switch>
    </div>
  </Router>
);

export default Container;
