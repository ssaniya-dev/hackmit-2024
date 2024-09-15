import openai
import chromadb
from chromadb.config import Settings
from typing import List

# Initialize OpenAI API (replace with your actual API key)
openai.api_key = "your-openai-api-key"

# Initialize ChromaDB client
chroma_client = chromadb.Client(Settings(persist_directory="./chroma_db"))

# Create a collection for storing email and prompt embeddings
collection = chroma_client.create_collection(name="emails_and_prompts")

def add_to_database(texts: List[str], metadata: List[dict]):
    # Generate embeddings using OpenAI's API
    embeddings = openai.Embedding.create(input=texts, model="text-embedding-ada-002")["data"]
    
    # Add documents to ChromaDB
    collection.add(
        embeddings=[e["embedding"] for e in embeddings],
        documents=texts,
        metadatas=metadata,
        ids=[f"doc_{i}" for i in range(len(texts))]
    )

def retrieve_and_generate(query: str, k: int = 3):
    # Generate query embedding
    query_embedding = openai.Embedding.create(input=[query], model="text-embedding-ada-002")["data"][0]["embedding"]
    
    # Retrieve similar documents from ChromaDB
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    
    # Construct prompt with retrieved documents
    context = "\n".join(results["documents"][0])
    prompt = f"Context:\n{context}\n\nQuery: {query}\n\nResponse:"
    
    # Generate response using ChatGPT-4
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message["content"]

if __name__ == "__main__":
    # US EHTIS FOR TESTING @ASMYOK DELETE THIS LATER!!!
    # Add documents to the database
    add_to_database(emails_and_prompts, metadata)

    # Perform RAG
    query = "When is the meeting scheduled?"
    result = retrieve_and_generate(query)
    print(result)
