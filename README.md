# Medical Transcription & NLP Pipeline

## Objective
This project builds an AI system for:
- Medical transcription summarization
- NLP-based key information extraction
- Patient sentiment and intent analysis
- SOAP note generation

## Features
- Named Entity Recognition (NER) for symptoms, diagnosis, treatment, prognosis
- Text summarization into structured JSON report
- Sentiment & intent detection using Transformer-based models
- SOAP note generation from transcript using rule-based mapping

## Setup

# Medical NLP Pipeline

This project is an **AI-powered medical transcription and analysis system** designed to:

1. Extract key medical details from doctor-patient conversations.  
2. Perform **sentiment analysis** and **intent detection**.  
3. Generate structured **SOAP notes** for clinical documentation.  

---

##  Features

###  **Medical Summary Extraction**
- Extracts essential information like:
  - **Patient Name**
  - **Symptoms**
  - **Diagnosis**
  - **Treatment Details**
  - **Current Status**
  - **Prognosis**

###  **Sentiment & Intent Analysis**
- Classifies patient sentiment as:
  - **Anxious**, **Neutral**, or **Reassured**
- Identifies patient intent (e.g., "Seeking reassurance," "Reporting symptoms").


##  Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/jenniferteresageorge/physian-notetaker.git
```

### 2. **Create a Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Download SpaCy Model**
Install the English NLP model for `spaCy`(do this if it does not work even after pip install -r requirements):
```bash
python -m spacy download en_core_web_sm
```

---

##  Usage Instructions

### 1. **Prepare a Text File**
Create a `.txt` file with doctor-patient conversation text. For example:
```
Doctor: How are you feeling today?
Patient: I had a car accident. My neck and back hurt a lot for four weeks.
Doctor: Did you receive treatment?
Patient: Yes, I had ten physiotherapy sessions, and now I only have occasional back pain.
```

### 2. **Run the Main Script**
```bash
python main.py
```

### 3. **Expected Output**
```
 Medical Summary:
{
    "Patient_Name": "Ms. Jones",
    "Symptoms": ["Neck pain", "Back pain"],
    "Diagnosis": ["Whiplash injury"],
    "Treatment": ["10 physiotherapy sessions", "Painkillers"],
    "Current_Status": "Occasional backache",
    "Prognosis": "Full recovery expected within six months"
}

 Sentiment & Intent Analysis:
Sentiment: Anxious
Intent: Seeking reassurance

 SOAP Note:
{
    "Subjective": {
        "Chief_Complaint": "Neck pain and back pain",
        "History_of_Present_Illness": "Patient had a car accident, experienced pain for four weeks, now occasional back pain."
    },
    "Objective": {
        "Physical_Exam": "Full range of motion in cervical and lumbar spine, no tenderness.",
        "Observations": "Patient appears in normal health, normal gait."
    },
    "Assessment": {
        "Diagnosis": "Whiplash injury",
        "Severity": "Mild, improving"
    },
    "Plan": {
        "Treatment": "Continue physiotherapy as needed, use analgesics for pain relief.",
        "Follow-Up": "Patient to return if pain worsens or persists beyond six months."
    }
}
```

---

## 🔍 Project Structure
```
.
├── main.py                  # Main script to run the pipeline
├── nlp_pipeline.py          # Medical NLP functions for summarization
├── sentiment_analysis.py    # Sentiment & intent analysis logic
├── soap_note_generator.py   # SOAP note generation logic
├── requirements.txt         # Dependencies for the project
├── README.md                # Project documentation
```

---


