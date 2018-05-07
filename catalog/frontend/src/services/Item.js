import axios from 'axios';
import { itemUrls, getHeaders } from 'config/api';

const ItemService = {
  getItemsByCatalog(catalogId) {
    return axios({
      method: 'get',
      url: itemUrls.itemsByCatalogId(catalogId),
    });
  },
  createItem(catalogId, item) {
    return axios({
      method: 'post',
      url: itemUrls.itemsByCatalogId(catalogId),
      headers: getHeaders(),
      data: item,
    });
  },
  updateItem(id, item) {
    return axios({
      method: 'put',
      url: itemUrls.itemById(id),
      headers: getHeaders(),
      data: item,
    });
  },
  deleteItem(id) {
    return axios({
      method: 'delete',
      url: itemUrls.itemById(id),
      headers: getHeaders(),
    });
  }
};

export default CatalogService;
