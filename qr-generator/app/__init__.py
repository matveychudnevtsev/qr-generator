from flask import Flask

app = Flask(__name__)

from .routes import generator, health

app.register_blueprint(generator.bp, url_prefix='/generate')
app.register_blueprint(health.bp, url_prefix='/health')
