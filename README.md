Vector Space Model for Information Retrieval
Overview
This project implements a Vector Space Model (VSM) for information retrieval using Python and Tkinter for the GUI. The Vector Space Model is a classic model for information retrieval, representing documents and queries as vectors in a high-dimensional space and calculating the similarity between them using cosine similarity.

Features
Preprocesses documents and queries by tokenizing, stemming, and removing stop words.
Calculates IDF (Inverse Document Frequency) for each term in the corpus.
Computes TF (Term Frequency) and TF-IDF vectors for documents and queries.
Performs information retrieval using the VSM and cosine similarity.
Generates inverted indexes and stores them in the inverted_index.txt file.
Provides a GUI built with Tkinter for user interaction.


Alpha Value
You can adjust the alpha value in the vsm_retrieval function to control the threshold for document relevance. This value determines the minimum similarity score required for a document to be considered relevant to the query. By default, the alpha value is set to 0.05. You can modify this value as needed in the vsm_information_retrieval.py file.

Dependencies
Python 3.0
Tkinter
NLTK

Output
![image](https://github.com/rahoolrathi/VSM-Information-Retrieval-Python/assets/129182364/a5f9ce17-3cbf-4c66-ba10-6601521cee33)
![image](https://github.com/rahoolrathi/VSM-Information-Retrieval-Python/assets/129182364/82baa13c-a4b5-47ef-a029-1b275e0e0b03)
