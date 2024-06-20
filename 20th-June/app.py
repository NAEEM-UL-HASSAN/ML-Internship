from flask import Flask, render_template, jsonify
from speech_to_text import recognize_speech_from_mic

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the main page of the web application.

    Returns
    -------
    str
        Rendered HTML content.
    """
    return render_template('index.html')

@app.route('/listen')
def listen():
    """
    Listens to the microphone input and returns the recognized text.

    Returns
    -------
    str
        JSON response containing the recognized text.
    """
    text = recognize_speech_from_mic()
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
