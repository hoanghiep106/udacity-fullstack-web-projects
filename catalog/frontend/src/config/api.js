import Auth from 'utils/auth';
import config from 'config';

const baseUrl = config.apiUrl;

export const getHeaders = () => ({
  'Content-Type': 'application/json',
  Authorization: Auth.isAuth() ? `Token ${Auth.getToken()}` : '',
});

export const filterUrls = {
  locations: `${baseUrl}/api/locations/`,
  programs: `${baseUrl}/api/programs/`,
  positions: `${baseUrl}/api/positions/`,
  companies: `${baseUrl}/api/companies/`,
  sessions: `${baseUrl}/api/sessions/`,
  currentLocations: `${baseUrl}/api/current-locations/`,
};

export const alumniUrls = {
  alumni: `${baseUrl}/api/users/`,
  loginLinkedIn: `${baseUrl}/api/users/linkedin/login/`,
  signUpLinkedIn: `${baseUrl}/api/users/linkedin/signup/`,
  linkedInRedirect: redirectUrl => `https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=${config.linkedInClientId}&redirect_uri=${redirectUrl}&state=987654321&scope=r_basicprofile%20r_emailaddress`,
  myInfo: `${baseUrl}/api/me/`,
};

export const authenticationUrls = {
  loginLinkedIn: `${baseUrl}/api/users/linkedin/login/`,
  signUpLinkedIn: `${baseUrl}/api/users/linkedin/signup/`,
  linkedInRedirect: redirectUrl => `https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=${config.linkedInClientId}&redirect_uri=${redirectUrl}&state=987654321&scope=r_basicprofile%20r_emailaddress`,
};

export const profileUrls = {
  profile: `${baseUrl}/api/me/`,
  session: id => `${baseUrl}/api/users/${id}/sessions/`,
};
