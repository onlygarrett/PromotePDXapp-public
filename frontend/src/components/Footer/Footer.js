import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import SocialsButton from "../../components/Elements/Button/Socials/Socials.js";
// import { subscribeToNewsletter } from "../../views/Newsletter/newsletterService.js";
import "./Footer.css";

function Footer() {
  const [email, setEmail] = useState("");
  const [statusMessage, setStatusMessage] = useState("");
  const [statusType, setStatusType] = useState("");
  const [loading, setLoading] = useState(false);

  const location = useLocation(); // Get the current location

  // useEffect
  //   (() => {
  //     const script = document.createElement("script");
  //     script.src = "https://substackapi.com/widget.js";
  //     script.async = true;
  //     document.getElementById("custom-substack-embed").appendChild(script);
  //
  //     window.CustomSubstackWidget = {
  //       substackUrl: "promotepdx.substack.com",
  //       placeholder: "email",
  //       buttonText: "Subscribe",
  //       theme: "custom",
  //       colors: {
  //         primary: "#CDBDA6",
  //         input: "#000000",
  //         email: "#FFFFFF",
  //         text: "#000000",
  //       },
  //     };
  //   }, []);
  // // Reset the status message when the location changes (i.e., page changes)
  // useEffect(() => {
  //   setStatusMessage("");
  //   setStatusType("");
  // }, [location]);
  //
  // // Email Validation Regex for ".com" ending
  // const isValidEmail = (email) => {
  //   const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[cC][oO][mM]$/;
  //   return emailRegex.test(email);
  // };
  //
  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  //   setLoading(true);
  //   setStatusMessage("");
  //
  //   if (!isValidEmail(email)) {
  //     setStatusMessage("Invalid email address. Must end with '.com'");
  //     setStatusType("error");
  //     setLoading(false);
  //     return;
  //   }
  //
  //   try {
  //     // Call the backend service
  //     const response = await subscribeToNewsletter(email);
  //     setStatusMessage(response.message); // Show success message
  //     setStatusType("success");
  //     setEmail(""); // Clear input field
  //   } catch (error) {
  //     setStatusMessage(error); // Show error message
  //     setStatusType("error");
  //   } finally {
  //     setLoading(false); // Stop loading
  //   }
  // };

  return (
    <>
      <div className="footer-container">
        <div className="footer-social-container">
          <div className="footer-newsletter-form-socials">
            <SocialsButton class="btn">Watch</SocialsButton>
          </div>
        </div>
        <div className="footer-sections">
          <div className="footer-newsletter-form-container">

            <form className="footer-newsletter-form" >
              {/* <header className="newsletter-form-header"> */}
              {/*   Sign up with your email address to receive news and updates. */}
              {/* </header> */}
              <div className="newsletter-form-field">
                <iframe
                  src="https://promotepdx.substack.com/embed"
                  width="480"
                  height="320"
                  style={{ padding: "12px 45px 126px 45px", background: "black" }}
                  frameborder="0"
                ></iframe>



                {/* <div id="custom-substack-embed"></div> */}
                {/*   <input */}
                {/*     type="email" */}
                {/*     className="newsletter-form-input" */}
                {/*     placeholder="Email Address" */}
                {/*     value={email} */}
                {/*     onChange={(e) => setEmail(e.target.value)} */}
                {/*     required */}
                {/*   /> */}
                {/* <button */}
                {/*   className="newsletter-form-button" */}
                {/*   type="submit" */}
                {/*   disabled={loading} // Disable button while loading */}
                {/* > */}
                {/*   <span className="button-text"> */}
                {/*     {loading ? "Signing Up..." : "Sign Up"} */}
                {/*   </span> */}
                {/* </button> */}
                {/* {statusMessage && ( */}
                {/*   <div className={`newsletter-submission-text ${statusType}`}> */}
                {/*     {statusMessage} */}
                {/*   </div> */}
                {/* )} */}
              </div>
            </form>
          </div>
          <div className="footer-bottom-divider"></div>
        </div>
      </div >
      <a target="_blank" href="https://jeedev.rip/" className="by">
        <img src="https://media.licdn.com/dms/image/v2/D5603AQGmRcOTiadMtQ/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1689440096321?e=1745452800&v=beta&t=kGGLpAvO9bk8yOoria1KZWe4z8YjP5wKx-v0yxcECts" />
        <p>by jeedev</p>
      </a>
    </>
  );
}

export default Footer;
