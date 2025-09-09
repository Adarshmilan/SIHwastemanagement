from flask import Blueprint, render_template

citizen_bp = Blueprint('citizen', __name__, template_folder='templates')

@citizen_bp.route('/citizen')
def dashboard():
    return render_template('citizen_dashboard.html')


