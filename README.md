<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vector Space Model for Information Retrieval</title>
</head>
<body>

<h1>Vector Space Model for Information Retrieval</h1>

<h2>Overview</h2>

<p>This project implements a Vector Space Model (VSM) for information retrieval using Python and Tkinter for the GUI. The Vector Space Model is a classic model for information retrieval, representing documents and queries as vectors in a high-dimensional space and calculating the similarity between them using cosine similarity.</p>

<h2>Features</h2>

<ul>
    <li>Preprocesses documents and queries by tokenizing, stemming, and removing stop words.</li>
    <li>Calculates IDF (Inverse Document Frequency) for each term in the corpus.</li>
    <li>Computes TF (Term Frequency) and TF-IDF vectors for documents and queries.</li>
    <li>Performs information retrieval using the VSM and cosine similarity.</li>
    <li>Generates inverted indexes and stores them in the inverted_index.txt file.</li>
    <li>Provides a GUI built with Tkinter for user interaction.</li>
</ul>

<h2>Alpha Value</h2>

<p>You can adjust the alpha value in the <code>vsm_retrieval</code> function to control the threshold for document relevance. This value determines the minimum similarity score required for a document to be considered relevant to the query. By default, the alpha value is set to 0.05. You can modify this value as needed in the <code>vsm_information_retrieval.py</code> file.</p>

<h2>Installation</h2>

<ol>
    <li>Clone the repository:</li>
    <code>git clone https://github.com/rahoolrathi/VSM-Information-Retrieval-Python.git</code>
    <li>Navigate to the project directory:</li>
    <code>cd VSM-Information-Retrieval-Python</code>
    <li>Install dependencies:</li>
    <code>pip install -r requirements.txt</code>
</ol>

<h2>Usage</h2>

<p>To run the GUI, execute the following command:</p>
<code>python vsm_information_retrieval.py</code>

<h2>Dependencies</h2>

<ul>
    <li>Python 3.x</li>
    <li>Tkinter</li>
    <li>NLTK</li>
</ul>

<h2>Output</h2>

<img src="https://github.com/rahoolrathi/VSM-Information-Retrieval-Python/assets/129182364/e22a8cef-c60e-4565-9607-c8f978f43626" alt="Sample Output 1">
<img src="https://github.com/rahoolrathi/VSM-Information-Retrieval-Python/assets/129182364/9b7ba950-ff00-4aa5-9fb0-5910561e6163" alt="Sample Output 2">

<h2>Contributing</h2>

<p>Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Credits</h2>

<ul>
    <li>NLTK library for text processing.</li>
    <li>Icons used in the GUI are from <a href="https://www.iconfinder.com/">Iconfinder</a>.</li>
</ul>

<h2>Additional Resources</h2>

<ul>
    <li><a href="https://github.com/rahoolrathi/VSM-Information-Retrieval-Python/docs">Documentation</a></li>
    <li><a href="https://github.com/rahoolrathi/VSM-Information-Retrieval-Python/examples">Example Usage</a></li>
</ul>

</body>
</html>
