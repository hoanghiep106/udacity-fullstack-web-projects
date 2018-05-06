class UserInfo {
  constructor() {
    this.data = null;
    this.listeners = [];
  }

  getUserInfo() {
    return this.data;
  }

  getUserName() {
    if (this.data) {
      return `${this.data.first_name} ${this.data.last_name}`;
    }
    return '';
  }

  getLinkedInEmail() {
    if (this.data) {
      return this.data.email;
    }
    return '';
  }

  getProfileImage() {
    if (this.data) {
      return this.data.profile.profile_image;
    }
    return '';
  }

  setUserInfo(data) {
    this.data = data;
    this.listeners.forEach(listener => listener());
  }

  onChange(listener) {
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
