from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

api_url = 'https://api.nasa.gov/planetary/apod?api_key=Vym6NI5mGW5NL63iYEqJcCqddREjQOf4On9bFGJ5'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/facts')
def facts():
    data = requests.get(api_url).json()
    t = data["title"]
    i = data["hdurl"]
    e = data["explanation"]
    return render_template('facts.html', title = t, imageLink = i, explanation = e)

if __name__ == "__main__":
	port = int(os.environ.get("PORT",5000))
	app.run(host="0.0.0.0", port=port, threaded=True)
