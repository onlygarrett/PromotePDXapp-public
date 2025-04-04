import emailjs from "emailjs-com";
import {
  Button,
  Form,
  FormGroup,
  FormInput,
  Input,
  TextArea,
} from "semantic-ui-react";
import Swal from "sweetalert2";
import "../../../components/Footer/Footer.css";
import { BlurText } from "../../../components/Header/BlurText/BlurText.js";
import "./ContactBody.css";

const SERVICE_ID = process.env.EMAIL_SERVICE_ID;
const TEMPLATE_ID = process.env.EMAIL_TEMPLATE_ID;
const USER_ID = process.env.EMAIL_USER_ID;
const ContactBody = () => {
  const handleOnSubmit = (e) => {
    e.preventDefault();
    emailjs.sendForm(SERVICE_ID, TEMPLATE_ID, e.target, USER_ID).then(
      (result) => {
        console.log(result.text);
        Swal.fire({
          icon: "success",
          title: "Message Sent Successfully",
        });
      },
      (error) => {
        console.log(error.text);
        Swal.fire({
          icon: "error",
          title: "Ooops, something went wrong",
          text: error.text,
        });
      }
    );
    e.target.reset();
  };

  return (
    <div className="pdx-contact-body">
      <div class="contact-info-container">
        <div class="contact-info-header">
          <BlurText
            text={"Contact Us"}
            className="contact-card-header"
            delay={100}
            type="word"
          />
        </div>
        <div class="contact-info-item">
          We’d love to hear from you! Any questions? Drop a line here or via
          email and we will get back to you soon!
        </div>
        <div class="contact-info-item">
          Please use the submission button below to feature your show on our
          calendar.
        </div>
        <div class="contact-info-item">
          info@promotepdx.com Based in Portland, OR
        </div>
      </div>
      <div class="content-container">
        <Form onSubmit={handleOnSubmit}>
          <Form.Field
            id="form-input-control-email"
            control={Input}
            label="Email"
            name="from_name"
            placeholder="Email…"
            required
            icon="mail"
            iconPosition="left"
          />
          <FormGroup widths="equal">
            <FormInput
              id="form-input-control-first-name"
              control={Input}
              label="First Name"
              name="first_name"
              placeholder="First Name…"
              required
              icon="user circle"
              iconPosition="left"
            />
            <FormInput
              id="form-input-control-last-name"
              control={Input}
              label="Last Name"
              name="last_name"
              placeholder="Last Name..."
              required
              icon="user circle"
              iconPosition="left"
            />
          </FormGroup>

          <Form.Field
            id="form-textarea-control-opinion"
            control={TextArea}
            label="Message"
            name="message"
            placeholder="Message…"
            required
          />
          <div class="contact-content">
            <Button type="submit" color="green">
              Submit
            </Button>
          </div>
        </Form>
      </div>
    </div>
  );
};

export default ContactBody;
