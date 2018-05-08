import React, { Component } from 'react';
import history from 'utils/history';
import { GoogleLogin } from 'react-google-login';
import AuthenticationService from 'services/Authentication';
import auth from 'utils/auth';
import userInfo from 'utils/userInfo';

class Header extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isAuth: auth.isAuth(),
      userInfo: userInfo.getInfo(),
      dropdownOpen: false,
    };
  }

  componentDidMount() {
    window.document.addEventListener('click', e => this.hideDropDown(e));
    this.removeAuthListener = auth.addListener(() => {
      this.setState({ isAuth: auth.isAuth(), dropdownOpen: false });
    });
    this.removeUserInfoListener = userInfo.addListener(() => {
      this.setState({ userInfo: userInfo.getInfo() });
    });
  }

  componentWillUnmount() {
    this.removeAuthListener();
    this.removeUserInfoListener();
    window.document.removeEventListener('click', e => this.hideDropDown(e));
  }

  toggleDropDown() { this.setState({ dropdownOpen: !this.state.dropdownOpen }); }

  hideDropDown(e) {
    if (this.dropDownToggleRef && !this.dropDownToggleRef.contains(e.target)) {
      this.setState({ dropdownOpen: false });
    }
  }

  handleLogin = (data) => {
    AuthenticationService.login(data).then((res) => {
      if (res.data && res.data.user && res.data.access_token) {
        userInfo.setInfo(res.data.user);
        auth.setAccessToken(res.data.access_token);
      }
    });
  }

  handleLogout = () => {
    AuthenticationService.logout();
  }

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light global-header">
        <div className="container">
          <a className="navbar-brand" onClick={() => history.push('/catalogs')}>
            <h2>Catalog</h2>
          </a>
          <ul className="navbar-nav navbar-right ml-auto">
            {!this.state.isAuth ?
              <li className="nav-item">
                <GoogleLogin
                  clientId="890058489988-pe58hoh8jmnm8ah7d149v6girbpet6g2.apps.googleusercontent.com"
                  onSuccess={this.handleLogin}
                  onFailure={this.handleLogin}
                  responseType="code"
                  className="btn-google"
                >
                  <i className="fa fa-google fa-lg d-inline" /> | Login
                </GoogleLogin>
              </li>
              :
              <React.Fragment>
                <li className="nav-item dropdown">
                  <img
                    className="profile--image"
                    src={this.state.userInfo.picture || 'img/default_profile_image.svg'}
                    width="35px"
                    height="35px"
                    alt="Profile"
                  />
                  <a
                    ref={ref => this.dropDownToggleRef = ref}
                    className="nav-link dropdown-toggle"
                    onClick={() => this.toggleDropDown()}
                  >
                    {this.state.userInfo.name}
                  </a>
                  <div className={`dropdown-menu ${this.state.dropdownOpen ? 'show' : ''}`}>
                    <a className="dropdown-item logout" onClick={this.handleLogout}>Log out</a>
                  </div>
                </li>
              </React.Fragment>
            }
          </ul>
        </div>
      </nav>
    );
  }
}

export default Header;
