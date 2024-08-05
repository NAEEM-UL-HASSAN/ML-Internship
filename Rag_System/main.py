import gradio as gr
from data_loader import load_data
from retrieval import Retrieval
from generation import Generator

# Load data
data = load_data('MayoClinic_Diseases.xlsx')
print("Data is adding in ChromaDB...")
# Initialize Retrieval
retrieval = Retrieval()
documents = data['Symptoms'].tolist()
ids = [str(index) for index in data.index]
metadatas = [{'specialist': row['Specialist Doctor']} for _, row in data.iterrows()]
retrieval.add_documents(documents, ids, metadatas)

# Initialize Generator
generator = Generator(api_key='YOUR_API_KEY')  # Replace with your OpenAI API key

def find_specialist(symptoms):
    try:
        # Perform retrieval
        results = retrieval.query(query_texts=[symptoms])
        documents = results.get('documents', [])
        metadatas = results.get('metadatas', [])

        # Debugging: Print types and contents
        print("Raw Documents:", documents)
        print("Metadatas:", metadatas)
        
        # Ensure each document is a string
        processed_documents = []
        for doc in documents:
            if isinstance(doc, str):
                processed_documents.append(doc)
            elif isinstance(doc, list):  # If a document is a list, join its elements
                processed_documents.append(" ".join(map(str, doc)))
            else:
                processed_documents.append(str(doc))  # Convert other types to string

        if processed_documents:
            context = " ".join(processed_documents)  # Combine all documents into a single string
        else:
            return "Error: No valid documents found."

        # Ensure metadatas is correctly processed
        if metadatas:
            specialists = [metadata.get('specialist') for metadata in metadatas[0] if isinstance(metadata, dict)]
        else:
            specialists = []

        # Generate a prompt based on the retrieved context
        prompt = f"Based on these symptoms: '{symptoms}', suggest a specialist doctor."

        if specialists:
            # Generate a response using the generative model
            return generator.generate_response(context, prompt)
        else:
            return "Specialist not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create Gradio interface
iface = gr.Interface(
    fn=find_specialist,
    inputs=gr.Textbox(label="Enter Symptoms"),
    outputs=gr.Textbox(label="Specialist Doctor"),
    title="Specialist Doctor Recommender",
    description="Enter symptoms to get the name of the specialist doctor."
)

# Launch the app
iface.launch()
