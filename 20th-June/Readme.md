# Real-Time Speech-to-Text Application

## Objective
Develop a real-time speech-to-text application in Python. This application will allow users to speak into their microphone, and the spoken words will be converted into text in real-time and displayed on a web page.

## Requirements
- Integrate speech recognition
- Design a simple web interface using HTML and CSS to display the real-time converted text.

## Deliverables
- A functional real-time speech-to-text application.
- The web interface displays real-time converted text.
- Codebase organized in a clean and well-documented manner.


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/NAEEM-UL-HASSAN/ML-Internship.git
    ```

2. Navigate to the project directory:
    ```bash
    cd 20th-June
    ```

3. Install the required Python packages:
    ```bash
    pip install SpeechRecognition Flask
    ```

## Usage
1. Run the Flask Web Application:
   ```sh
   python app.py
2. Open your web browser and navigate to `http://127.0.0.1:5000`

## Code Overview

1. The `speech_to_text.py` file contains the function recognize_speech_from_mic which captures and processes audio input from the microphone.
2. The `app.py` file sets up the Flask web server and defines routes for rendering the main page and listening to the microphone input.
3. The `index.html` file in the templates folder contains the HTML and JavaScript code for displaying the recognized text and updating it in real-time.