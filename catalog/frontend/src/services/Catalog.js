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
  }
};

export default CatalogService;
