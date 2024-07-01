from gtts import gTTS
import os

class TextToSpeech:
    """
    A class to handle text-to-speech conversion.

    Attributes
    ----------
    language : str
        The language for text-to-speech conversion.

    Methods
    -------
    save_audio(text: str, filename: str) -> None:
        Saves the text as an audio file.
    """

    def __init__(self, language='en'):
        self.language = language
    
    def save_audio(self, text: str, filename: str) -> None:
        """
        Saves the text as an audio file.

        Parameters
        ----------
        text : str
            The text to be converted to speech.
        filename : str
            The filename for the saved audio file.
        """
        tts = gTTS(text=text, lang=self.language)
        tts.save(filename)
