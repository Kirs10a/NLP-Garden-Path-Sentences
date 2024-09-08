# NLP Garden Path Sentences Project

## Overview

This project demonstrates the use of Natural Language Processing (NLP) 
with spaCy to analyze garden path sentences. These are sentences that 
begin in such a way that a reader's most likely interpretation will be 
incorrect; they are a type of syntactic ambiguity.

## Project Structure

- `garden.py`: The main Python script that processes the garden path 
sentences using spaCy, performs tokenization, and named entity 
recognition (NER).

- `requirements.txt`: Lists the Python dependencies required to 
run this project.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/NLP-Garden-Path-Sentences.git
   cd NLP-Garden-Path-Sentences

2. **Set up a virtual environment (optional but recommended):**
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the required packages:**
   pip install -r requirements.txt

4. **Download the spaCy language model:**.
   python -m spacy download en_core_web_sm

## Usage
To run the script, use the following command:
python garden.py

The script will process a list of garden path sentences, tokenize them,
and perform named entity recognition.


Example Output
Here’s what the output might look like:
Sentence: Mary gave the child a Band-Aid.
Entities: [('Mary', 'PERSON')]
Mary: PERSON - People, including fictional

Sentence: The cotton clothing is made of grows in Mississippi.
Entities: [('Mississippi', 'GPE')]
Mississippi: GPE - Countries, cities, states

This project is licensed under the MIT License. See the LICENSE file for details.