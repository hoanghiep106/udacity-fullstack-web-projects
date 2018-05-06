import React, { Component } from 'react';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false,
    };
  }

  handleLogin = (res) => {
    console.log(res);
  }

  handleLogout = (res) => {
    console.log(res);
  }

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light global-header">
        <div className="container">
          <a className="navbar-brand">
            <h2>Catalog</h2>
          </a>
        </div>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav navbar-right ml-auto">
            {!this.state.isLoggedIn ?
              <GoogleLogin
                clientId="819305314472-l8pgmpri6tg3c5g2nmda33cu738k98e2.apps.googleusercontent.com"
                onSuccess={this.handleLogin}
                onFailure={this.handleLogin}
                accessType="offline"
                responseType="code"
              >
                <i className="fa fa-google fa-lg" /> |
                <span> Login with Google</span>
              </GoogleLogin>
              :
              <GoogleLogout
                buttonText="Logout"
                onLogoutSuccess={this.handleLogout}
              />
            }
          </ul>
        </div>
      </nav>
    );
  }
}

export default Header;
