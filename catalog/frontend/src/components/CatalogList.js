import React from 'react';
import Catalog from 'components/Catalog';

const CatalogList = (props) => {
  const catalogList = props.catalogs.map(catalog => (
    <Catalog key={catalog.id} {...catalog} />
  ));
  return (
    <div className="row">
      {catalogList}
    </div>
  )
};

export default CatalogList;
