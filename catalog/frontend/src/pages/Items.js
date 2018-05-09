import React from 'react';
import history from 'utils/history';
import auth from 'utils/auth';
import userInfo from 'utils/userInfo';
import ItemService from 'services/Item';
import CatalogService from 'services/Catalog';
import ItemList from 'components/ItemList';
import ItemForm from 'components/ItemForm';

class Items extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isAuth: auth.isAuth(),
      userInfo: userInfo.getInfo(),
      catalog: {},
      items: [],
      modalOpen: false,
      catalogId: this.props.match.params.id,
    };
  }

  componentDidMount() {
    this.fetchCatalog();
    this.fetchItems();
    this.removeAuthListener = auth.addListener(() => {
      this.setState({ isAuth: auth.isAuth() });
    });
    this.removeUserInfoListener = userInfo.addListener(() => {
      this.setState({ userInfo: userInfo.getInfo() });
    });
  }

  componentWillUnmount() {
    this.removeAuthListener();
    this.removeUserInfoListener();
  }

  fetchCatalog() {
    CatalogService.getCatalog(this.state.catalogId).then((res) => {
      this.setState({ catalog: res.data.catalog });
    }).catch(() => history.push('/catalogs'));
  }

  fetchItems = () => {
    ItemService.getItemsByCatalog(this.state.catalogId).then((res) => {
      this.setState({ items: res.data.items });
    });
  }

  openModal = () => {
    this.setState({ modalOpen: true });
  }

  closeModal = () => {
    this.setState({ modalOpen: false });
  }

  createItem = (item) => {
    ItemService.createItem(this.state.catalogId, item).then(() => {
      this.closeModal();
      this.fetchItems();
    });
  }

  render() {
    const { catalog, items } = this.state;
    return (
      <div className="container my-5">
        <div className="jumbotron">
          <h2>{catalog.name}</h2>
          <p>{catalog.description}</p>
          <a className="btn-link" onClick={() => history.push('/catalogs')}>
            Back
          </a>
        </div>
        {this.state.isAuth && this.state.userInfo.id === catalog.user_id &&
        <div className="text-right">
          <button
            className="btn btn-light mb-4"
            onClick={this.openModal}
          >
            New item
          </button>
        </div>
        }
        <div>
          {items && items.length > 0 &&
            <ItemList
              items={this.state.items}
              fetchItems={this.fetchItems}
            />
          }
        </div>
        {this.state.modalOpen &&
        <ItemForm
          isOpen={this.state.modalOpen}
          closeModal={this.closeModal}
          action={this.createItem}
          title="Create item"
        />
        }
      </div>
    );
  }
}

export default Items;
