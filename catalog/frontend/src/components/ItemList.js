import React from 'react';
import Item from 'components/Item';

const ItemList = (props) => {
  const itemList = props.items.map(item => (
    <Item
      key={item.id}
      {...item}
      fetchItems={props.fetchItems}
    />
  ));
  return (
    <div className="row">
      {itemList}
    </div>
  );
};

export default ItemList;
