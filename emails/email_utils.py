from flask_mail import Mail, Message

def send_contact_emails(mail, name, email, message):
    # Create email messages
    msg1 = Message(subject="Contact Form Submission",
                   recipients=['recipient1@example.com'],
                   body=f"New message from {name} ({email}):\n\n{message}")

    msg2 = Message(subject="Contact Form Submission",
                   recipients=['recipient2@example.com'],
                   body=f"New message from {name} ({email}):\n\n{message}")

    try:
        # Send emails
        mail.send(msg1)
        mail.send(msg2)
        return True
    except Exception as e:
        return False, str(e)
