import openai

class Generator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, context, prompt):
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Based on the following information: {context}, answer the query: {prompt}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
