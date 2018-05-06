import React from 'react';
import { Router, Route, Switch, Redirect } from 'react-router-dom';
import history from 'utils/history';
// App shell
import Header from 'components/Header';
import LoadingIndicator from 'components/LoadingIndicator';
// Pages
import Catalog from 'pages/Catalog';


class Container extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isFetchingInfo: false,
    };
  }

  renderRoutes() {
    return (
      <Switch>
        <Route path="/catalogs" name="Catalog" component={Catalog} />
        <Redirect from="/" to="/catalogs" />
      </Switch>
    );
  }

  render() {
    if (this.state.isFetchingInfo) {
      return (
        <div className="loading-page">
          <LoadingIndicator />
        </div>
      );
    }
    return (
      <Router history={history}>
        <div>
          <Header />
          {this.renderRoutes()}
        </div>
      </Router>
    );
  }
}

export default Container;
