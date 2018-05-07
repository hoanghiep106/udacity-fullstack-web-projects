export function shortenString(string) {
  if (string) {
    return string.length > 50 ? `${string.slice(0, 50)}...` : string;
  }
  return '';
}
