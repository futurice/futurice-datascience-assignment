import streamlit as st
import io
from pathlib import Path
from typing import Any, List

st.set_page_config(page_title="Digital Energy - 40 RAG", page_icon="🦾")
st.title("💼 Digital Energy 40 - RAG")


st.sidebar.header("Instructions")
st.sidebar.write(
    f"""
    * Implement **`generate_answer(query)`** - function. Implement a RAG function that 
    fetches relevant context related to the question from the given Digital Energy 40 - report. 
    * You should build FASS index, vector database or something else that enables you efficiently 
    extract the right context for a new question. You can implement the ingestion logic into ingest.py file.
    It can be a one-time used python-script

    * You may install and import any open-source Python packages. You can also edit the streamlit application 
    as you wish but there is no need to do that.
    """
)


def generate_answer(query: str) -> dict:  # Implement your RAG logic here
    """Return an answer to *query* using the bundled *document*.

    Parameters
    ----------
    query : str
        Natural-language question from the user.
    document : Any
        A *BytesIO* object containing the raw PDF bytes. Parse, chunk, embed,
        index … as you wish.

    Returns
    -------
    dict
        Must contain at least:
        * "answer"  - generated answer string.
        * "sources" - list of citation strings (may be empty).
    """
    placeholder_answer = "✨ Your answer here ✨"
    placeholder_sources: List[str] = ["Context for your answer"]
    return {"answer": placeholder_answer, "sources": placeholder_sources}

# ───────────────────────────── Streamlit UI ──────────────────────────────
query = st.text_input("Ask something about the document")

if st.button("Ask") and query:
    with st.spinner("Thinking …"):
        try:
            # Reset pointer to start for each read, in case generate_answer .read()s
            result = generate_answer(query)
        except Exception as e:
            st.error(f"❌ Your RAG pipeline raised an exception: {e}")
            st.stop()

    st.subheader("Answer")
    st.write(result.get("answer", "(No answer returned)"))

    if result.get("sources"):
        st.subheader("Sources")
        for i, src in enumerate(result["sources"], 1):
            st.markdown(f"**{i}.** {src}")