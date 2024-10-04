from flask import Flask, send_from_directory, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
import secrets
import datetime
#from flask import jsonify

app = Flask(__name__, static_folder='', template_folder='')

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://karthik:Karthik@cluster0.v7xzk.mongodb.net/neuronairegistrations?retryWrites=true&w=majority"

mongo = PyMongo(app)

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

# Define routes to serve static files from custom folders
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

@app.route('/img/<path:filename>')
def serve_img(filename):
    return send_from_directory('img', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

# Define routes to serve HTML files
@app.route('/')
def home():
    return send_from_directory('', 'home.html')

@app.route('/about')
def about():
    return send_from_directory('html', 'about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        phone = request.form['phone']

        # Save the contact details to MongoDB
        mongo.db.contacts.insert_one({
            "name": name,
            "email": email,
            "phone": phone,
            "message": message,
            "created_at": datetime.datetime.now(datetime.timezone.utc)
        })

        # Create email messages
        msg1 = Message(subject="Contact Form Submission",
                       recipients=['neuron.ai.india@gmail.com'],
                       body=f"New message from {name} ({email}):\n\n{message}\nPhone Number:\n\n{phone}")

        msg2 = Message(subject="Contact Form Submission Successful",
                       recipients=[email],
                       body=f"Soon you'll receive mail or call, your message:\n\n{message}")

        try:
            # Send emails
            mail.send(msg1)
            mail.send(msg2)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')

    return send_from_directory('html', 'contact.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Save the user details to MongoDB
        mongo.db.users.insert_one({
            "username": username,
            "email": email,
            "password": password,
            "created_at": datetime.datetime.now(datetime.timezone.utc)

        })

        # Email to admin
        msg1 = Message(subject="New Neuron.ai Registration",
                       recipients=["neuronaihelpdesk@gmail.com"],
                       body=f"New Neuron.ai registration from {username} ({email}):")

        # Confirmation email to user
        msg2 = Message(subject="Neuron.ai Registration Successful",
                       recipients=[email],
                       body=f"Thank you for registering at Neuron.ai, {username}!\n\nWe will contact you soon with more details.")

        try:
            # Send emails
            mail.send(msg1)
            mail.send(msg2)
            flash('Registration successful! A confirmation email has been sent.', 'success')
        except Exception as e:
            flash(f'An error occurred while sending emails: {e}', 'error')

        return redirect(url_for('home'))

    return send_from_directory('html', 'register.html')

@app.route('/register_courses', methods=['GET', 'POST'])
def register_courses():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course-title']

        # Save the course registration details to MongoDB
        mongo.db.course_registrations.insert_one({
            "username": username,
            "email": email,
            "phone": phone,
            "course": course,
            "created_at": datetime.datetime.now(datetime.timezone.utc),
            "status": "pending"
        })

        msg1 = Message(subject="New Course Registration",
                       recipients=["neuronaihelpdesk@gmail.com"],
                       body=f"New registration from {username} ({email}):\n\nPhone Number: {phone}\nCourse: {course}")

        # Confirmation email to user
        msg2 = Message(subject="Course Registration Successful",
                       recipients=[email],
                       body=f"Thank you for registering for the {course} course, {username}!\n\nWe will contact you soon with more details.")

        try:
            # Send emails
            mail.send(msg1)
            mail.send(msg2)
            flash('Registration successful! A confirmation email has been sent.', 'success')
        except Exception as e:
            flash(f'An error occurred while sending emails: {e}', 'error')

        print("registration is also done")
        return redirect(url_for('home'))

    return send_from_directory('html', 'home.html')

if __name__ == "__main__":
    app.run()
