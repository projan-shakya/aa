from flask import Flask, render_template, request, jsonify
#from logic import synthesize_voice, plot_data, plot_waveforms

app = Flask(__name__)


# You need to replace the placeholders above with the actual URLs for the models.

@app.route('/')
def index():
    return render_template('index.html')