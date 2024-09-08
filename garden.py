gardenpathSentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",
    "The old man the boats.",
    "The horse raced past the barn fell."
]
import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Tokenize and perform NER on each sentence
for sentence in gardenpathSentences:
    
    # Loop through each sentence
    doc = nlp(sentence)
    
    print(f"\nSentence: {sentence}")
    print("Tokens:", [token.text for token in doc])
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])

    # Explain each entity label
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_} - {spacy.explain(ent.label_)}")
        
# Entity: Band-Aid (ORG - Companies, agencies, institutions, etc.)
# The entity 'Band-Aid' is correctly identified as an organization. 
# This makes sense as Band-Aid is a brand name.

# Entity: Mississippi (GPE - Countries, cities, states)
# The entity 'Mississippi' is correctly identified as a geopolitical 
# entity, 
# which is appropriate because Mississippi is a state in the United 
# States.

# Gardenn path sentences are ambigious and not rare for SpaCy to not 
# find any entities as it does not contain any common patterns for named 
# entities.