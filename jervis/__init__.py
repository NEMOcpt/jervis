from flask import Flask
from .views import main_views

app = Flask(__name__)
app.register_blueprint(main_views.bp)

