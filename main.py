from nlp_pipeline import extract_medical_summary
from sentiment_analysis import analyze_patient_sentiment
from soap_note_generator import generate_soap_note

def main():
    with open("transcript.txt", "r") as file:
        transcript = file.read()

    # Extract structured summary
    summary = extract_medical_summary(transcript)
    print("\n📋 Medical Summary:", summary)

    # Analyze sentiment & intent
    sentiment, intent = analyze_patient_sentiment(transcript)
    print("\n😊 Sentiment & Intent Analysis:")
    print(f"Sentiment: {sentiment}")
    print(f"Intent: {intent}")

    # Generate SOAP note
    soap_note = generate_soap_note(transcript, summary)
    print("\n📄 SOAP Note:")
    print(soap_note)

if __name__ == "__main__":
    main()
