import React from 'react';
import auth from 'utils/auth';
import CatalogService from 'services/Catalog';
import CatalogList from 'components/CatalogList';
import CatalogForm from 'components/CatalogForm';

class Catalogs extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isAuth: auth.isAuth(),
      catalogs: [],
      modalOpen: false,
    };
  }

  componentDidMount() {
    this.fetchCatalogs();
    this.removeAuthListener = auth.addListener(() => {
      this.setState({ isAuth: auth.isAuth() });
    });
  }

  componentWillUnmount() {
    this.removeAuthListener();
  }

  fetchCatalogs = () => {
    CatalogService.getCatalogs().then((res) => {
      if (res.data && res.data.catalogs) {
        this.setState({ catalogs: res.data.catalogs });
      }
    });
  }

  openModal = () => {
    this.setState({ modalOpen: true });
  }

  closeModal = () => {
    this.setState({ modalOpen: false });
  }

  createCatalog = (catalog) => {
    CatalogService.createCatalog(catalog).then(() => {
      this.closeModal();
      this.fetchCatalogs();
    });
  }

  render() {
    const { catalogs } = this.state;
    return (
      <div className="container my-5">
        {this.state.isAuth &&
        <div className="text-right">
          <button
            className="btn btn-light mb-4"
            onClick={this.openModal}
          >
            New catalog
          </button>
        </div>
        }
        <div>
          {catalogs &&
            (catalogs.length > 0 ?
              <CatalogList
                catalogs={this.state.catalogs}
                fetchCatalogs={this.fetchCatalogs}
              />
              :
              <h3>No catalogs</h3>
            )
          }
        </div>
        {this.state.modalOpen &&
          <CatalogForm
            isOpen={this.state.modalOpen}
            closeModal={this.closeModal}
            action={this.createCatalog}
            title="Create catalog"
          />
        }
      </div>
    );
  }
}

export default Catalogs;
