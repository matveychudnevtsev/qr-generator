// Placeholder API client
export const generateQR = async (data) => {
  const response = await fetch(`/api/qr/generate?data=${encodeURIComponent(data)}`);
  return response.json();
};
