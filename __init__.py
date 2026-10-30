
from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Configure Talisman security headers
    Talisman(
        app,
        force_https=True,
        strict_transport_security=True,
        content_security_policy={
            "default-src": "'self'",
            "style-src": ["'self'", "'unsafe-inline'"],
            "script-src": ["'self'"]
        }
    )

    return app
