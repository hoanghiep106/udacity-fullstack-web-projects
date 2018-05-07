export const getJson = (string) => {
  try {
    return JSON.parse(string);
  } catch (error) {
    return string;
  }
};
