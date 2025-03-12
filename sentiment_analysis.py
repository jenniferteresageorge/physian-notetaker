from transformers import pipeline

# Load sentiment analysis pipeline (can be fine-tuned for medical domain if needed)
sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_patient_sentiment(transcript):
    patient_lines = []
    for line in transcript.split("\n"):
        if "Patient:" in line:
            patient_lines.append(line.replace("Patient:", "").strip())

    patient_text = " ".join(patient_lines)

    # Sentiment
    sentiment_result = sentiment_pipeline(patient_text)[0]
    sentiment_label = sentiment_result["label"]

    if sentiment_label == "NEGATIVE":
        sentiment = "Anxious"
        intent = "Seeking reassurance"
    elif sentiment_label == "POSITIVE":
        sentiment = "Reassured"
        intent = "Expressing gratitude"
    else:
        sentiment = "Neutral"
        intent = "Reporting symptoms"

    return sentiment, intent
