import { getJson } from 'utils/json';

class UserInfo {
  constructor() {
    this.listeners = [];
    const infoString = localStorage.getItem('user');
    this.info = infoString ? getJson(infoString) : {};
  }

  setInfo(data) {
    this.info = data;
    localStorage.setItem('user', JSON.stringify(data));
    this.listeners.forEach(listener => listener());
  }

  getInfo() {
    return this.info;
  }

  addListener(listener) {
    this.listeners.push(listener);
    return () => this.removeListener(listener);
  }

  removeListener(listener) {
    const index = this.listeners.indexOf(listener);
    if (index > -1) {
      this.listeners.splice(index, 1);
    }
  }
}

export default new UserInfo();
