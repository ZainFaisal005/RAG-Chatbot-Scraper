# RAG Chatbot with Scraper

This project demonstrates a Retrieval-Augmented Generation (RAG) chatbot powered by a web scraper. The chatbot can scrape data from any public website and use that data to answer user queries. It utilizes the power of LangChain for creating RAG pipelines and the Ollama embeddings model for vector-based search. The system also includes a Streamlit frontend to interact with the chatbot.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Frontend Setup](#frontend-setup)
  - [Interacting with the Chatbot](#interacting-with-the-chatbot)
- [Project Structure](#project-structure)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Overview

The RAG Chatbot is a powerful tool that allows users to interact with a chatbot that can answer questions based on real-time, live web data. This chatbot uses a combination of web scraping, information retrieval, and generative language models to provide accurate answers to user queries. Here's how the system works:

1. **Scraping**: The chatbot scrapes data from a user-provided URL. It retrieves textual content from the website using BeautifulSoup and stores it for further processing.
2. **Indexing and Embeddings**: The scraped data is then indexed and turned into vector embeddings using the Ollama embeddings model. These embeddings are stored in a vector database (FAISS).
3. **Query Answering**: The chatbot processes user queries by using the indexed data. It finds relevant information from the vector database and generates responses using a generative model.
4. **Frontend**: A Streamlit frontend allows users to input URLs, initialize the chatbot, and interact with it by submitting questions.

## Technologies Used

- **LangChain**: A framework for building LLM (Large Language Model)-powered applications. It provides tools for managing prompt engineering, chains, and integrations with vectorstores like FAISS.
- **Streamlit**: A Python library for creating interactive web apps with minimal code. It powers the frontend of the chatbot.
- **Ollama**: The LLM provider used for embeddings and query processing.
- **BeautifulSoup**: A Python library for web scraping that extracts data from HTML and XML files.
- **FAISS**: Facebook AI Similarity Search, a library used for efficient similarity search in large datasets, which in this case, stores and retrieves the embeddings of the scraped content.
- **Requests**: A Python library for sending HTTP requests, used to fetch the contents of websites.
- **Python 3.x**: The primary programming language used for development.

## Features

- **Website Scraping**: Automatically scrapes and processes textual data from any publicly accessible website.
- **Vector-based Search**: Indexes the scraped data using vector embeddings, enabling efficient similarity search.
- **Retrieval-Augmented Generation**: Combines retrieval-based search with a generative model to answer questions based on scraped data.
- **Streamlit Frontend**: Provides an easy-to-use interface for interacting with the chatbot, including options for URL input, chatbot initialization, and question submission.
- **Persistent Chatbot State**: The chatbot retains its state (scraped data and vectorstore) between user interactions.
- **Scalability**: Capable of handling a variety of websites and large amounts of text data.

## Installation

### Prerequisites

Ensure you have the following dependencies installed before starting:

- Python 3.7 or higher
- pip (Python package manager)

### Step-by-step Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/rag-chatbot-with-scraper.git
    cd rag-chatbot-with-scraper
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    # For Windows
    venv\Scripts\activate
    # For macOS/Linux
    source venv/bin/activate
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

   The `requirements.txt` file should include:
   
   ```
   requests
   beautifulsoup4
   langchain
   langchain_ollama
   faiss-cpu
   streamlit
   ```

4. **Set up Ollama (if not already set up)**:  
   Ensure you have access to Ollama's API and the model you're using (`llama3.2` in this case). Follow their setup instructions [here](https://ollama.com).

## Usage

### Frontend Setup

1. **Run the Streamlit frontend**:

    In your terminal, from the project directory, run:

    ```bash
    streamlit run app.py
    ```

2. **Access the app**:
    - After running the above command, Streamlit will automatically open a new browser tab with the URL `http://localhost:8501`, where the chatbot interface will be available.

### Interacting with the Chatbot

1. **Enter a URL**:
    - Type in any public URL from which you want to scrape data and interact with the chatbot.

2. **Initialize the Chatbot**:
    - After entering the URL, click the "Initialize Chatbot" button. The app will scrape the website, index the data, and set up the chatbot backend.
   
3. **Ask Questions**:
    - Once the chatbot is initialized, type your query in the input box and click "Submit Question". The chatbot will process your question and provide a relevant response based on the scraped content.

4. **Exit the Chat**:
    - To stop interacting, simply close the browser window or stop the Streamlit app by pressing `Ctrl+C` in the terminal.

## Project Structure

```bash
rag-chatbot-with-scraper/
│
├── app.py                   # Streamlit frontend app to interact with the chatbot
├── chatbot_code.py          # Core functions: scraping, indexing, creating RAG chain
├── requirements.txt         # Required Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignore file to exclude unnecessary files
```

- `app.py`: Contains the Streamlit interface code for the chatbot.
- `chatbot_code.py`: Contains the functions for scraping websites, indexing the data, and creating the RAG chain.
- `requirements.txt`: Lists all Python packages required for the project.
- `README.md`: This file, containing all project details and instructions.

## Limitations

1. **Website Structure**: The scraper may not work correctly if the website has a complex structure, uses JavaScript heavily, or employs anti-scraping mechanisms.
2. **Model Limitations**: The performance and accuracy of the chatbot are dependent on the quality of the scraped data and the model's capabilities.
3. **Data Size**: Extremely large websites may require more time for scraping, indexing, and querying.

## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

Please ensure that your code follows the project style and that tests are included for new features.
