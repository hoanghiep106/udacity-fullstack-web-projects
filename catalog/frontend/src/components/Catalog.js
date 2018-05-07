import React from 'react';
import { shortenString } from 'utils/string';
import CatalogService from 'services/Catalog';

const Catalog = (props) => (
  <div className="col-md-4 mb-3">
    <div className="card card-catalog">
      <div className="card-body">
        <h4>{props.name}</h4>
        <p>{shortenString(props.description)}</p>
      </div>
      <div className="card-footer text-right">
        <button className="btn btn-secondary btn-sm mr-2">
          <i className="fa fa-pencil" />
        </button>
        <button
          className="btn btn-danger btn-sm"
          onClick={() => CatalogService.deleteCatalog(props.id)}
        >
          <i className="fa fa-trash" />
        </button>
      </div>
    </div>
  </div>
);

export default Catalog;
