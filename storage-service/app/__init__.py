from flask import Flask

app = Flask(__name__)

from .routes import storage, health

app.register_blueprint(storage.bp, url_prefix='/files')
app.register_blueprint(health.bp, url_prefix='/health')
