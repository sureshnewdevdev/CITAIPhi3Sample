# -------------------------------
# IMPORT REQUIRED MODULES
# -------------------------------

# dataclass is used to create simple data-holding classes
from dataclasses import dataclass

# List is used for type hinting (better readability & tooling support)
from typing import List

# numpy is used for numerical operations like sorting similarity scores
import numpy as np

# ollama is used to communicate with the Phi-3 language model locally
import ollama

# TF-IDF converts text into numerical vectors
from sklearn.feature_extraction.text import TfidfVectorizer

# cosine_similarity measures similarity between vectors
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# DOCUMENT STRUCTURE
# -------------------------------

# @dataclass automatically creates constructor and helpers
@dataclass
class Document:
    id: str          # unique id for each text chunk
    text: str        # actual text content
    source: str = "" # optional source file name


# -------------------------------
# LOAD AND SPLIT TEXT FILE
# -------------------------------

def load_text_file(filepath):
    # Open the text file in read mode using UTF-8 encoding
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split content into chunks based on blank lines
    # Ignore very small chunks (less than 20 characters)
    chunks = [c.strip() for c in content.split("\n\n") if len(c.strip()) > 20]

    # List to store Document objects
    docs = []

    # Convert each chunk into a Document object
    for i, chunk in enumerate(chunks):
        docs.append(Document(
            id=f"text_chunk_{i}",   # auto-generated chunk id
            text=chunk,             # actual text
            source="Templesofondipudur.txt"  # source file name
        ))

    # Return list of documents
    return docs


# -------------------------------
# SIMPLE TF-IDF RETRIEVER (NO LLM)
# -------------------------------

class SimpleTfidfRAG:

    def __init__(self, docs: List[Document]):
        # Store the documents
        self.docs = docs

        # Create TF-IDF vectorizer
        # stop_words="english" removes common words like "the", "is"
        # ngram_range=(1,2) means unigrams + bigrams
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2)
        )

        # Convert all documents into TF-IDF vectors
        self.doc_matrix = self.vectorizer.fit_transform(
            [d.text for d in docs]
        )

    def retrieve(self, query, top_k=3):
        # Convert user query into TF-IDF vector
        q_vec = self.vectorizer.transform([query])

        # Compute cosine similarity between query and documents
        sims = cosine_similarity(q_vec, self.doc_matrix).flatten()

        # Get indexes of top matching documents (highest score first)
        idx = np.argsort(sims)[::-1][:top_k]

        # Return documents with similarity score > 0
        return [
            (self.docs[i], float(sims[i]))
            for i in idx
            if sims[i] > 0
        ]


# -------------------------------
# SEND CONTEXT TO PHI-3 MODEL
# -------------------------------

def ask_phi3(context, question):
    # Prompt strictly instructs model to use only retrieved context
    prompt = f"""
You are a temple knowledge assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

    # Call Phi-3 model via Ollama
    response = ollama.chat(
        model="phi3:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract and return model response text
    return response["message"]["content"]


# -------------------------------
# MAIN APPLICATION FLOW
# -------------------------------

def main():
    # Display application banner
    print("=== RAG + Phi-3 Temple Search ===")

    # Load temple text file and split into chunks
    docs = load_text_file("Templesofondipudur.txt")

    # Initialize TF-IDF retriever
    rag = SimpleTfidfRAG(docs)

    # Infinite loop for asking questions
    while True:
        query = input("\nAsk Question (type exit to quit): ")

        # Exit condition
        if query.lower() == "exit":
            break

        # Retrieve relevant documents
        results = rag.retrieve(query)

        # If nothing matches, inform user
        if not results:
            print("No matching context found.")
            continue

        # Combine retrieved document texts into one context
        context = "\n\n".join([doc.text for doc, _ in results])

        # Show retrieved context (for transparency)
        print("\n--- Retrieved Context ---")
        print(context[:500])

        # Ask Phi-3 to generate final answer
        print("\n--- Phi-3 Answer ---")
        answer = ask_phi3(context, query)
        print(answer)


# -------------------------------
# ENTRY POINT
# -------------------------------

# Ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
