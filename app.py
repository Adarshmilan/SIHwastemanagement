from flask import Flask, render_template, send_from_directory
import psycopg2

conn = psycopg2.connect(host="localhost", dbname ="postgres", user="postgres", password ="1234", port="5432")

cur = conn.cursor()



conn.commit()




from citizen.routes import citizen_bp
from worker.routes import worker_bp
from admin.routes import admin_bp
import os   

app = Flask(__name__, static_folder='static', template_folder='templates')

# Register blueprints
app.register_blueprint(citizen_bp)
app.register_blueprint(worker_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
