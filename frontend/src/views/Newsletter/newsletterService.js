import axios from "axios";

const API_URL = "http://promotepdx.rip/api/subscribe/";

export const subscribeToNewsletter = async (email) => {
  try {
    const response = await axios.post(API_URL, { email });
    return response.data; // Success response
  } catch (error) {
    throw error.response?.data?.email?.[0] || "An error occurred"; // Handle errors
  }
};
