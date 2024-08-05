import chromadb

class Retrieval:
    def __init__(self, collection_name='disease_symptoms'):
        self.client = chromadb.Client()
        self.collection_name = collection_name
        self.collection = self.client.create_collection(name=self.collection_name)

    def add_documents(self, documents, ids, metadatas):
        self.collection.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )

    def query(self, query_texts):
        return self.collection.query(query_texts=query_texts)
