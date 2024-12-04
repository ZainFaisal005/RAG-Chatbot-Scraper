import streamlit as st
from urllib.parse import urlparse
from chatbot_code import scrape_website, index_data, create_rag_chain  # Import your chatbot functions

def main():
    st.title("RAG Chatbot with Scraper")
    st.write("Enter a URL to scrape and interact with the chatbot.")

    # Step 1: URL Input
    url = st.text_input("Enter URL", placeholder="https://example.com")
    if url and not urlparse(url).scheme:
        st.error("Please enter a valid URL (starting with http or https).")

    # Initialize chatbot
    if st.button("Initialize Chatbot") and url:
        with st.spinner("Scraping website and setting up chatbot..."):
            try:
                # Scrape website and index data
                data = scrape_website(url)
                if not data:
                    st.error("No data was scraped from the website. Check the URL.")
                else:
                    vectorstore = index_data(data)
                    st.session_state.rag_chain = create_rag_chain(vectorstore)
                    st.session_state.chatbot_initialized = True
                    st.success("Chatbot initialized! You can now ask questions.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Step 2: Query Input
    if "rag_chain" in st.session_state and st.session_state.chatbot_initialized:
        query = st.text_input("Ask your question:")

        # Only show the submit button if the chatbot is ready
        submit_button = st.button("Submit Question")
        if submit_button and query:
            with st.spinner("Processing your query..."):
                try:
                    response = st.session_state.rag_chain.invoke({"query": query})
                    if 'result' in response:
                        st.markdown(f"### Bot Response:\n{response['result']}")
                    else:
                        st.error("No valid response received.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
    else:
        if not st.session_state.get("chatbot_initialized", False):
            st.warning("Please initialize the chatbot by entering a URL and clicking 'Initialize Chatbot'.")

if __name__ == "__main__":
    if "chatbot_initialized" not in st.session_state:
        st.session_state.chatbot_initialized = False
    main()