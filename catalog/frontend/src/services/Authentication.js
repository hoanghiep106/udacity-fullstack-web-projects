import axios from 'axios';
import { authenticationUrls } from 'config/api';
import auth from 'utils/auth';
import userInfo from 'utils/userInfo';

const AuthenticationService = {
  login(data) {
    return axios({
      method: 'post',
      url: authenticationUrls.login,
      data,
    });
  },
  logout() {
    auth.setAccessToken('');
    userInfo.setInfo({});
  },
};

export default AuthenticationService;
