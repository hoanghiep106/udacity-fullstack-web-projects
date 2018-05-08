import React from 'react';
import { modalStyles } from 'config/app';
import Modal from 'components/Modal';


class ItemForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      item: this.props.item || {},
      error: {},
    };
  }

  handleChange = (e) => {
    const item = { ...this.state.item };
    item[e.target.name] = e.target.value.trim();
    this.setState({ item });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    if (this.validate()) {
      this.props.action(this.state.item);
    }
  }

  validate() {
    const error = { ...this.state.error };
    let errorCount = 0;
    if (!this.state.item.name) {
      error.name = 'Required';
      errorCount += 1;
    } else if (this.state.item.name.length > 50) {
      error.name = 'Over 50 characters';
      errorCount += 1;
    } else {
      error.name = '';
    }
    if (this.state.item.description && this.state.item.description.length > 120) {
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
              <div>{this.props.title}</div>
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
                  defaultValue={this.state.item.name || ''}
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
                  defaultValue={this.state.item.description || ''}
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
                {this.props.title}
              </button>
            </div>
          </form>
        </div>
      </Modal>
    );
  }
}

export default ItemForm;
