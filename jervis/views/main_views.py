from flask import Blueprint, render_template

bp = Blueprint('main_views', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('mainpage.html')

@bp.route('/test')
def test():
    return render_template('testpage.html')