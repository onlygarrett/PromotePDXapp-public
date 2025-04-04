import axios from "axios";

const INSTA_URL = process.env.REACT_APP_INSTAGRAM_URL;
const INSTA_TOKEN = process.env.REACT_APP_INSTAGRAM_TOKEN;

const FetchPostIds = async () => {
  try {
    const response = await axios.get(
      `${INSTA_URL}9691190014242778/media?access_token=${INSTA_TOKEN}`
    );
    const successfulIds = response.data.data.map((item) => item.id).slice(0, 6);

    return successfulIds;
  } catch (error) {
    console.error(
      "Error fetching post IDs:",
      // error.response.data.error.message
    );
    return []; // Return an empty array on error
  }
};

const fetchPostsData = async () => {
  const ids = await FetchPostIds();
  try {
    // Use Promise.all to fetch all URLs concurrently
    const responses = await Promise.all(
      ids.map((postId) =>
        axios
          .get(
            `${INSTA_URL}${postId}?access_token=${INSTA_TOKEN}&fields=media_url,permalink`
          )
          .then((res) => res.data)
          .catch((err) => ({ error: err.message }))
      )
    );

    // Filter out any failed responses and return only successful data
    const successfulData = responses.filter((res) => !res.error);

    return successfulData; // Return the list of data
  } catch (err) {
    console.error("Error while fetching posts:", err);
    return []; // Return an empty list on failure
  }
};

export default fetchPostsData;
