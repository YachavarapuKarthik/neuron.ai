from flask import Flask
from flask_mail import Mail, Message
import secrets

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'neuron.ai.india@gmail.com'
app.config['MAIL_PASSWORD'] = 'jpsxejblmkzccclg'  # Use your app-specific password here
app.config['MAIL_DEFAULT_SENDER'] = 'neuron.ai.india@gmail.com'

mail = Mail(app)

# Generate a secure random key
app.secret_key = secrets.token_hex(16)

def send_email(recipient, subject, body):
    with app.app_context():  # Ensure Flask's app context is available
        # Create the email message
        msg = Message(subject=subject,
                      recipients=[recipient],
                      body=body)
        try:
            # Send the email
            mail.send(msg)
            print('Email sent successfully!')
        except Exception as e:
            print(f'An error occurred: {e}')

if __name__ == '__main__':
    # Test email details
    recipient = 'karthikluckily@gmail.com'
    subject = "Hi Karthik"
    body = "This is your sample email."

    send_email(recipient, subject, body)
