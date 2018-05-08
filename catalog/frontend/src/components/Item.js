import React from 'react';
import auth from 'utils/auth';
import userInfo from 'utils/userInfo';
import { shortenString } from 'utils/string';
import ItemService from 'services/Item';
import ConfirmDelete from 'components/ConfirmDelete';
import ItemForm from 'components/ItemForm';

class Item extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userInfo: userInfo.getInfo(),
      isAuth: auth.isAuth(),
      confirmModal: false,
      editModal: false,
    };
  }

  componentDidMount() {
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

  openModal = (modal) => {
    this.setState({ [modal]: true });
  }

  closeModal = (modal) => {
    this.setState({ [modal]: false });
  }

  deleteItem = () => {
    ItemService.deleteItem(this.props.id).then(() => {
      this.closeModal('confirmModal');
      this.props.fetchItems();
    });
  }

  editItem = (item) => {
    ItemService.updateItem(this.props.id, item).then(() => {
      this.closeModal('editModal');
      this.props.fetchItems();
    });
  }

  render() {
    return (
      <div className="col-md-4 mb-3">
        <div className="card card-item">
          <div className="card-body">
            <h4>{shortenString(this.props.name, 15)}</h4>
            <p>{shortenString(this.props.description, 50)}</p>
          </div>
          {this.state.isAuth && this.state.userInfo.id === this.props.user_id &&
          <div className="card-footer text-right">
            <button
              className="btn btn-secondary btn-sm mr-2"
              onClick={() => this.openModal('editModal')}
            >
              <i className="fa fa-pencil" />
            </button>
            <button
              className="btn btn-danger btn-sm"
              onClick={() => this.openModal('confirmModal')}
            >
              <i className="fa fa-trash" />
            </button>
          </div>
          }
        </div>
        <ConfirmDelete
          isOpen={this.state.confirmModal}
          closeModal={() => this.closeModal('confirmModal')}
          delete={this.deleteItem}
        />
        {this.state.editModal &&
          <ItemForm
            isOpen={this.state.editModal}
            closeModal={() => this.closeModal('editModal')}
            action={this.editItem}
            item={this.props}
            title="Edit item"
          />
        }
      </div>
    );
  }
}

export default Item;
