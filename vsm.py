import os
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import numpy as np

inverted_index = {}
# Adding custom stop words to NLTK's stopwords list
stop_words = {"a", "is", "the", "of", "all", "and", "to", "can", "be", "as", "once", "for", "at", "am", "are", "has", "have", "had", "up", "his", "her", "in", "on", "no", "we"}


# Setting up Porter Stemmer
stemmer = PorterStemmer()

# Directory path for research papers
dir_path = "ResearchPapers"

# Function to get file names from a directory
def get_filenames(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Function to preprocess text
#Preprocessing Done
def preprocess(text):
    words = word_tokenize(text.lower())  # Tokenize text
    words = [stemmer.stem(word) for word in words if word.isalnum() and word not in stop_words]  # Stemming and removing stop words
    return words

# Function to read a file and preprocess its content
def read_file(filename):
    full_path = os.path.join(dir_path, filename)
    with open(full_path, "r") as f:
        return preprocess(f.read())

# Function to read all files and preprocess them
def read_all_files(filenames):
    preprocessed_documents = []
    for filename in filenames:
        document = read_file(filename)
        preprocessed_documents.append(document)
    return preprocessed_documents

# Function to preprocess a query
#Query processing Done
def preprocess_query(query):
    return preprocess(query)

# Function to calculate IDF for each term
def calculate_idf(documents):
    N = len(documents)
    word_doc_freq = {}  # Dictionary to store document frequency for each word
    for document in documents:
        words = set(document)
        for word in words:
            word_doc_freq[word] = word_doc_freq.get(word, 0) + 1
    
    idf = {}
    for word, freq in word_doc_freq.items():
        idf[word] = np.log(N / freq)
    return idf

# Function to compute term frequency (TF) for a document
def compute_tf(words):
    tf = {}
    for word in words:
        tf[word] = np.log(tf.get(word,0)) + 1


    return tf

# Function to compute TF-IDF vector for a document
def compute_tf_idf(tf, idf):
    tf_idf = {}
    for word, tf_value in tf.items():
        tf_idf[word] = tf_value * idf.get(word, 0)
    return tf_idf

# Function to perform information retrieval using VSM and storing inverted index

#Formation of Index done
def creating_posting_list(word,documentid):
    if word not in inverted_index:
        inverted_index[word] = []
        inverted_index[word].append((documentid, 1))  
    else:
        doc_ids = [doc_id for doc_id, _ in inverted_index[word]]
        if documentid not in doc_ids:
                inverted_index[word].append((documentid, 1))  
        else:
            for idx, (doc_id, freq) in enumerate(inverted_index[word]):
                if doc_id == documentid:
                    inverted_index[word][idx] = (doc_id, freq + 1)
                    break

#Vector Space Model Done           
# Function to perform information retrieval using VSM
def vsm_retrieval(documents, query, idf, alpha=0.05):
    # Compute IDF including terms in the query
    documents.append(query)  # Add query to the documents list temporarily
    idf = calculate_idf(documents)
    documents.pop()  # Remove query from the documents list
    
    # Compute TF for the query
    query_tf = compute_tf(query)
    query_terms = set(query_tf.keys())  # Get unique terms in the query
    query_vector = compute_tf_idf(query_tf, idf)  # Compute TF-IDF vector for the query
    
    document_vectors = []
    
    
    
    for documentid, document in enumerate(documents):
        tf = compute_tf(document)
        tf_idf = compute_tf_idf(tf, idf)
        document_vectors.append(tf_idf)
        for word in tf.keys():
            creating_posting_list(word, documentid)
    
    # Saving the inverted index to a file
    with open("inverted_index.txt", "w") as f:
        for word, posting_list in inverted_index.items():
            f.write(word + ": ")
            for doc_id, freq in posting_list:
                f.write(f"({doc_id}, {freq}) ")
            f.write("\n")
    
    similarities = []
    for i,doc_vector in enumerate(document_vectors):
        # Consider only terms present in the query for similarity computation
        dot_product = sum(query_vector.get(word, 0) * doc_vector.get(word, 0) for word in query_terms)
        query_norm = np.linalg.norm([query_vector[word] for word in query_terms])
        doc_norm = np.linalg.norm([doc_vector[word] for word in doc_vector])  # Only consider terms present in the document vector
        similarity = dot_product / (query_norm * doc_norm)
        similarities.append(similarity)
    # Sorting document IDs based on relevance to the query
    result_set = [i for i, sim in enumerate(similarities) if sim > alpha]
    return result_set


#creating inverted index




# Function to open dialog box with search results
def open_dialog(entry, documents, idf):
    # Retrieve the query from the text field
    query = entry.get()

    # Preprocess the query
    preprocessed_query = preprocess_query(query)
    print( preprocessed_query)

    # Perform retrieval using the VSM model
    result_set = vsm_retrieval(documents, preprocessed_query, idf)

    # Display the result set in a dialog box
    if result_set:
        message = "Result-Set: " + ", ".join(map(str, result_set))
    else:
        message = "No documents found."

    messagebox.showinfo("Results", message)

# Function to create the GUI
#GUI done
def create_gui(documents, idf):
    root = tk.Tk()
    root.title("VSM Model (21k4580 Rahool)")

    window_width = 300
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position for centering
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set geometry
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Set background color for the window
    root.configure(bg="#f0f0f0")

    # Create frame
    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(pady=10, padx=10)

    # Create label
    label = tk.Label(frame, text="Enter Query:", bg="#f0f0f0", fg="black")
    label.grid(row=0, column=0, pady=10, padx=(0, 10))

    # Create text field with increased size and border
    entry = tk.Entry(frame, width=30, bd=1, relief="solid")
    entry.grid(row=0, column=1, pady=10)

    # Create button to open dialog box with search emoji
    search_emoji = "\U0001F50E"  # Unicode for magnifying glass emoji
    open_button = ttk.Button(root, text=f"{search_emoji} Search", command=lambda: open_dialog(entry, documents, idf), style='TButton')
    open_button.pack(pady=10)

    # Create style for the button with custom colors
    style = ttk.Style()
    style.configure('TButton', background='#007bff', foreground='black')

    return root, entry




# Main function
def main():
    # Retrieve all documents and calculate IDF
    filenames = get_filenames(dir_path)
    documents = read_all_files(filenames)
    idf = calculate_idf(documents)

    # Create GUI
    root, entry = create_gui(documents, idf)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
