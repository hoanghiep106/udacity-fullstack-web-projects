import React from 'react';
import Modal from 'react-modal';
import history from 'utils/history';
import CatalogService from 'services/Catalog';
import CatalogList from 'components/CatalogList';
import CatalogForm from 'components/CatalogForm';

class Catalogs extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      catalogs: [],
      modalOpen: false,
    };
  }

  componentDidMount() {
    this.fetchCatalogs();
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

  render() {
    const { catalogs } = this.state;
    return (
      <div className="container my-5">
        <div className="text-right">
          <button
            className="btn btn-light mb-4"
            onClick={this.openModal}
          >
            New catalog
          </button>
        </div>
        <div>
          {catalogs && catalogs.length > 0 &&
            <CatalogList catalogs={this.state.catalogs} />
          }
        </div>
        <CatalogForm
          isOpen={this.state.modalOpen}
          closeModal={this.closeModal}
          fetchCatalogs={this.fetchCatalogs}
        />
      </div>
    )
  }
}

export default Catalogs;
