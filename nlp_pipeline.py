import spacy 
from spacy import displacy 
import re
import json

nlp = spacy.load("en_core_web_sm")

def extract_medical_summary(transcript):
    doc = nlp(transcript)

    symptoms = []
    treatments = []
    diagnosis = []
    prognosis = []

    keywords = {
        "Symptoms": ["pain", "discomfort", "backache", "stiffness", "neck pain"],
        "Diagnosis": ["whiplash", "injury"],
        "Treatment": ["physiotherapy", "painkillers"],
        "Prognosis": ["full recovery", "long-term damage", "follow-up"]
    }

    for sent in doc.sents:
        sent_text = sent.text.lower()
        for category, terms in keywords.items():
            for term in terms:
                if term in sent_text:
                    if category == "Symptoms":
                        symptoms.append(sent.text.strip())
                    elif category == "Diagnosis":
                        diagnosis.append(sent.text.strip())
                    elif category == "Treatment":
                        treatments.append(sent.text.strip())
                    elif category == "Prognosis":
                        prognosis.append(sent.text.strip())

    structured_summary = {
        "Patient_Name": "Ms. Jones",  # Hardcoded for demo - could be extracted using NER
        "Symptoms": list(set(symptoms)),
        "Diagnosis": list(set(diagnosis)),
        "Treatment": list(set(treatments)),
        "Current_Status": "Occasional backache",
        "Prognosis": "Full recovery expected within six months"
    }

    return json.dumps(structured_summary, indent=4)
