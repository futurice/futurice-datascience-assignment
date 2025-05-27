# Futurice Data Scientist Retrieval-Augmented Generation (RAG) Assignment

Welcome! This small project is about **2-hour technical exercise** that you’ll complete on your own time and later discuss at the interview.  Aim for a *minimal but functional* prototype - polish and extra features can be discussed live.

To complete this assignment, you'll be using Microsoft Azure cloud resources. We've set up a dedicated, empty resource group for you to work within.

## Your Azure Login Details
URL:  portal.azure.com
Username and password is sent in the assignment email you recieved

## Getting Started with Azure
1. Log In: Please go to the Azure Portal URL above and sign in with your provided username and password.
2. Locate Your Resource Group: Once you're logged in, you'll have access to an empty resource group specifically created for your assignment. It is named after the applicant's firstname eg. joe-rg.

## Important Azure Information
> All resources you create for this assignment should be provisioned within this designated resource group. This helps us track your work and manage costs effectively.
> You have full control over the resources within your assigned resource group, allowing you to create, configure, and delete services as needed for the assignment.
> For this assignment, you will need to deploy Azure OpenAI Service resources within your designated resource group. Specifically, you will need to deploy instances of the embedding model and the chat model as required by the assignment. You will then use the API keys and endpoints generated from your own deployments to interact with these models.

---

## 🗂  Repo structure

| Path | Purpose |
|------|---------|

| **`app.py`**      | Streamlit app & `generate_answer()` stub |
| **`ingest.py`**   | One-off script to build an index from the PDF |
| `requirements.txt`| Python dependencies *(create this during setup)* |
| `data/Digital_Energy_40.pdf` | The source report used as context for the RAG* |

Feel free to rename / move files if your design warrants it.  
---

## 🛠  What we ask you to implement (with some hints)

### 1. `ingest.py`
1. Load the PDF (e.g. with *PyPDF*).  
2. Split into relevant sized token chunks
3. Embed each chunk with **OpenAI's** embedding model (`text-embedding-3-large`). We will give you access to Azure environment where you should deploy the embedding model yourself. 
4. Persist embeddings + metadata in a vector store (FAISS is fine).  

### 2. `generate_answer(query)` in `app.py`
1. Embed the user **query**.  
2. Find the relevant context. For example, use *k*-NN search for the store to find top-k chunks → **context**.  
3. Feed `query + context` to the **OpenAI `gpt-4o-mini` chat model** with an  
   *“answer citing sources”* prompt. We will give you access to Azure environment where you should deploy the model yourself. 
4. Return a `dict` with:
   ```python
   {
       "answer": "…",
       "sources": ["Title p. 12", "Chart p. 37", …]
   }


No need to make this automated ingestion - it can be a run once script for now.

### 3. Testing the chat 
To test the chat locally, run the provided Streamlit application:

```bash
streamlit run app.py
```
Then, you can use the chat interface to test your RAG logic.

Note: You don't need to focus on UI changes. 


### 4. Deploy the application as a docker container (optional)
When you are happy with the end result, you could deploy the application as a Docker container. This is an optional step to simulate app deployment to a real environment. 

-------
> Two focused hours should be enough time for this assignment.
> During the interview you can outline improvements and trade-offs - don’t stress about edge cases now.
