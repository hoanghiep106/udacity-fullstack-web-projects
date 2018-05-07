import auth from 'utils/auth';

const baseUrl = 'http://127.0.0.1:5001';

export const getHeaders = () => ({
  Authorization: `Bearer ${auth.getAccessToken()}`,
  'Content-Type': 'application/json',
});

export const authenticationUrls = {
  login: `${baseUrl}/login`,
};

export const catalogUrls = {
  catalogs: `${baseUrl}/catalogs`,
  catalogById: (id) => `${baseUrl}/catalogs/${id}`,
};

export const itemUrls = {
  itemsByCatalogId: (catalogId) => `${baseUrl}/catalogs/${catalogId}/items`,
  itemById: (id) => `${baseUrl}/items/${id}`,
};
