import React from 'react';
import { modalStyles } from 'config/app';
import Modal from 'components/Modal';


const ConfirmDelete = props => (
  <Modal
    isOpen={props.isOpen}
    onRequestClose={props.closeModal}
    style={modalStyles}
  >
    <div className="card">
      <div className="card-header">
        <div>Delete</div>
        <div
          className="btn-close"
          onClick={() => props.closeModal()}
        >
          <i className="fa fa-times" />
        </div>
      </div>
      <div className="card-body">
        Are you sure you want to delete this?
      </div>
      <div className="card-footer text-right">
        <button
          className="btn btn-secondary btn-sm mr-2"
          type="button"
          onClick={() => props.closeModal()}
        >
          No
        </button>
        <button
          className="btn btn-danger btn-sm"
          type="submit"
          onClick={() => props.delete()}
        >
          Yes
        </button>
      </div>
    </div>
  </Modal>
);

export default ConfirmDelete;
