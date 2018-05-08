export function shortenString(string, length) {
  if (string) {
    return string.length > length ? `${string.slice(0, length)}...` : string;
  }
  return '';
}
