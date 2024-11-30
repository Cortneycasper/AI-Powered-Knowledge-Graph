import spacy

# Load SpaCy language model
nlp = spacy.load("en_core_web_sm")

def process_documents(documents):
    entities = []
    relationships = []

    for doc in documents:
        processed = nlp(doc)
        for ent in processed.ents:
            entities.append({"text": ent.text, "label": ent.label_})
        for token in processed:
            if token.dep_ == "ROOT" and token.head != token:
                relationships.append({"source": token.head.text, "target": token.text, "relation": token.dep_})

    return entities, relationships
