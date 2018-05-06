import axios from 'axios';
import { authenticationUrls, getHeaders } from 'config/api';
import errorHandler from 'utils/error';

const AuthenticationService = {
  signUpLinkedIn(data) {
    return axios({
      method: 'post',
      headers: getHeaders(),
      url: authenticationUrls.signUpLinkedIn,
      data,
    }).then(res => res)
      .catch(err => errorHandler(err));
  },
  loginLinkedIn(data) {
    return axios({
      method: 'post',
      headers: getHeaders(),
      url: authenticationUrls.loginLinkedIn,
      data,
    }).then(res => res)
      .catch(err => errorHandler(err));
  },
};

export default AuthenticationService;
