import speech_recognition as sr

def recognize_speech_from_mic():
    """
    Recognizes speech from the microphone and returns it as text.

    Returns
    -------
    str
        The text converted from the spoken words.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech was unintelligible"
    except sr.RequestError:
        return "API unavailable"

if __name__ == "__main__":
    print(recognize_speech_from_mic())
