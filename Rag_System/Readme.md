# Specialist Doctor Recommender

This project is a Specialist Doctor Recommender that uses a Retrieval-Augmented Generation (RAG) approach to suggest specialist doctors based on user-reported symptoms. The system utilizes ChromaDB for information retrieval and OpenAI's GPT model for generating responses.

## Overview

1. **Data Loading**: Loads disease and symptoms data from an Excel file.
2. **Retrieval**: Uses ChromaDB to index symptoms and retrieve relevant documents.
3. **Generation**: Employs a generative model (OpenAI GPT) to generate a response based on the retrieved documents.
4. **Interface**: Provides a Gradio interface for user interaction.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.7 or later
- An OpenAI API key (for the generative model)

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/NAEEM-UL-HASSAN/ML-Internship.git
    cd Rag_System
    ```
## Configuration

1. **OpenAI API Key**: 
   - Replace `'your-openai-api-key'` in `main.py` with your actual OpenAI API key.

## File Structure

- `data_loader.py`: Handles loading and preparing the data from the Excel file.
- `retrieval.py`: Manages the ChromaDB setup and querying.
- `generation.py`: Interfaces with the OpenAI API to generate responses.
- `main.py`: Contains the Gradio interface and integrates all components.

## Usage

1. **Run the Application**

    ```bash
    python main.py
    ```

2. **Interact with the Interface**:
   - Once the application is running, open the provided URL in a web browser.
   - Enter symptoms in the text box and get recommendations for specialist doctors.