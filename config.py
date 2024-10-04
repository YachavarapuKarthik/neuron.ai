import os
from itsdangerous import URLSafeTimedSerializer

import app


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('neuron.ai.india@gmail.com')  # Your email here
    MAIL_PASSWORD = os.environ.get('Neuronai2024')  # Your email password here
    # Initialize URLSafeTimedSerialize

