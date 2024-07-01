import os
import json
import requests
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()


class LLMAvatar:
    """
    A class to interact with the LLM model.

    Attributes
    ----------
    model_name : str
        The name of the LLM model.
    url : str
        The URL for the API endpoint.
    api : str
        The API key for authentication.
    logger : logging.Logger
        Logger for the class.

    Methods
    -------
    llm_prediction(message: str) -> dict:
        Makes a prediction with the LLM model.
    """

    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME")
        self.url = os.getenv("OPEN_ROUTER_URL")
        self.api = os.getenv("OPEN_API_KEY")
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def llm_prediction(self, message: str) -> dict:
        """
        Makes a prediction with the LLM model.

        Parameters
        ----------
        message : str
            The user's input message.

        Returns
        -------
        dict
            The response from the LLM model.
        """
        self.logger.info("Making prediction with LLM")
        headers = {
            "Authorization": f'Bearer {self.api}',
            "Content-Type": "application/json"
        }
        data = json.dumps({
            "model": self.model_name,
            "messages": [{"role": "user", "content": message}]
        })
        response = requests.post(url=self.url, headers=headers, data=data)
        self.logger.debug(f"Response: {response.status_code} - {response.content}")
        return response.json()
