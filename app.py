from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_session import Session
from flask import make_response
from flask_cors import CORS
from getresults import *

app = Flask(__name__, template_folder='template')
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get_recommendations', methods=['POST', 'GET'])
def get_recommendations():
    if request.method == 'POST':
        data = request.form.to_dict()
        sample = list(data.values())
        try:
            sample = [float(i) for i in sample]
        except ValueError as e:
            flash("Invalid input detected. Please ensure all inputs are numeric.")
            return render_template('index.html')  
        recommendations = get_song_recommendation(sample)
        print(recommendations)
        
        return render_template('result.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True, port=56015, host='0.0.0.0')
