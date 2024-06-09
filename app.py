from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import secrets
from dotenv import load_dotenv
import os


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)  # Required for flash messages

# Load environment variables from .env file
load_dotenv()

# Configuring Flask-Mail

app.config.update(
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=os.getenv('MAIL_PORT'),
    MAIL_USE_TLS=os.getenv('MAIL_USE_TLS') == 'True',
    MAIL_USE_SSL=os.getenv('MAIL_USE_SSL') == 'True',
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
)


mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        name = request.form['Name']
        email = request.form['email']
        message = request.form['Message']

        # Send email to yourself
        msg = Message(
            subject="New message from your website",
            body=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            sender='rajkr8369@gmail.com',  # Use a valid sender email address
            recipients=['rajkr8369@gmail.com']  # Specify your email address here
        )
        mail.send(msg)

        # Send confirmation email to the sender
        confirmation_msg = Message(
            subject="Thank you for contacting me",
            body=f"Thanks for contacting me, {name}! I will be happy to respond to you soon. Stay connected!",
            sender='rajkr8369@gmail.com',  # Use a valid sender email address
            recipients=[email]  # Send confirmation to the sender's email
        )
        mail.send(confirmation_msg)

        flash('Your message has been sent successfully!')
        return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)
