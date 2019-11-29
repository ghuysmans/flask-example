from app import app
from flask import jsonify, send_file, render_template
import time
from datetime import date

@app.route('/')
def index():
    return render_template("index.html", day=date.today().strftime("%A"))

@app.route('/api')
def api():
    return jsonify({"time": time.time()})
