import React from 'react';
import { modalStyles } from 'config/app';
import CatalogService from 'services/Catalog';
import Modal from 'components/Modal';


class CatalogForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      catalog: this.props.catalog || {},
      error: {},
    };
  }

  handleChange = (e) => {
    const catalog = { ...this.state.catalog };
    catalog[e.target.name] = e.target.value.trim();
    this.setState({ catalog });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    if (this.validate()) {
      CatalogService.createCatalog(this.state.catalog).then((res) => {
        this.props.fetchCatalogs();
        this.setState({ catalog: {} });
        this.props.closeModal();
      });
    }
  }

  validate() {
    const error = { ...this.state.error };
    let errorCount = 0;
    if (!this.state.catalog.name) {
      error.name = 'Required';
      errorCount += 1;
    } else if (this.state.catalog.name.length > 50) {
      error.name = 'Over 50 characters';
      errorCount += 1;
    } else {
      error.name = '';
    }
    if (this.state.catalog.description && this.state.catalog.description.length > 120) {
      error.description = 'Over 120 characters';
      errorCount += 1;
    } else {
      error.description = '';
    }
    this.setState({ error });
    if (errorCount > 0) return false;
    return true;
  }

  render() {
    return (
      <Modal
        isOpen={this.props.isOpen}
        onRequestClose={this.props.closeModal}
        style={modalStyles}
      >
        <div className="card">
          <form onSubmit={this.handleSubmit}>
            <div className="card-header">
              <div>{this.props.title || 'Catalog'}</div>
              <div
                className="btn-close"
                onClick={() => this.props.closeModal()}
              >
                <i className="fa fa-times" />
              </div>
            </div>
            <div className="card-body">
              <div className="form-group">
                <div className="row">
                  <div className="col-sm-4">
                    <label>Name</label>
                  </div>
                  <div className="col-sm-8 text-right">
                    {this.state.error.name &&
                      <div className="text-danger">{this.state.error.name}</div>}
                  </div>
                </div>
                <input
                  className="form-control"
                  type="text"
                  name="name"
                  defaultValue={this.state.catalog.name || ''}
                  onChange={this.handleChange}
                />
              </div>
              <div className="form-group">
                <div className="row">
                  <div className="col-sm-4">
                    <label>Description</label>
                  </div>
                  <div className="col-sm-8 text-right">
                    {this.state.error.description &&
                      <div className="text-danger">{this.state.error.description}</div>}
                  </div>
                </div>
                <input
                  className="form-control"
                  type="text"
                  name="description"
                  defaultValue={this.state.catalog.description || ''}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="card-footer text-right">
              <button
                className="btn btn-secondary btn-sm mr-2"
                type="button"
                onClick={() => this.props.closeModal()}
              >
                Cancel
              </button>
              <button
                className="btn btn-success btn-sm"
                type="submit"
              >
                {this.props.action || 'OK'}
              </button>
            </div>
          </form>
        </div>
      </Modal>
    );
  }
}

export default CatalogForm;
