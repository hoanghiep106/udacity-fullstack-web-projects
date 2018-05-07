import axios from 'axios';
import { catalogUrls, getHeaders } from 'config/api';

const CatalogService = {
  getCatalogs() {
    return axios({
      method: 'get',
      url: catalogUrls.catalogs,
    });
  },
  createCatalog(catalog) {
    return axios({
      method: 'post',
      url: catalogUrls.catalogs,
      headers: getHeaders(),
      data: catalog,
    });
  },
  updateCatalog(id, catalog) {
    return axios({
      method: 'put',
      url: catalogUrls.catalogById(id),
      headers: getHeaders(),
      data: catalog,
    });
  },
  deleteCatalog(id) {
    return axios({
      method: 'delete',
      url: catalogUrls.catalogById(id),
      headers: getHeaders(),
    });
  },
};

export default CatalogService;
