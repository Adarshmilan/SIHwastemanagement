from flask import Blueprint, render_template

worker_bp = Blueprint('worker', __name__, template_folder='templates')

@worker_bp.route('/worker')
def dashboard():
    return render_template('worker_dashboard.html')
