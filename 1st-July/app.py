from flask import Flask, request, jsonify, render_template, send_from_directory
from llm_avatar import LLMAvatar
from tts import TextToSpeech
import os
import uuid

app = Flask(__name__)
avatar = LLMAvatar()
tts = TextToSpeech()

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles the chat endpoint.

    Receives the user's message, gets a response from the LLM,
    converts the response to speech, and returns the response.

    Returns
    -------
    json
        The response text and audio filename.
    """
    user_message = request.json.get('message')
    response = avatar.llm_prediction(user_message)
    response_text = response['choices'][0]['message']['content']
    
    # Generate a unique filename for the audio
    audio_filename = f"{uuid.uuid4()}.mp3"
    audio_filepath = os.path.join('static', 'audio', audio_filename)
    tts.save_audio(response_text, audio_filepath)
    
    return jsonify({'text': response_text, 'audio': audio_filename})

@app.route('/static/audio/<filename>')
def serve_audio(filename):
    """
    Serves the generated audio files.

    Parameters
    ----------
    filename : str
        The name of the audio file.

    Returns
    -------
    response
        The audio file.
    """
    return send_from_directory('static/audio', filename)

if __name__ == "__main__":
    app.run(debug=True)
