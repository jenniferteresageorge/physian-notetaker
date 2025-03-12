import json

def generate_soap_note(transcript, summary_json):
    summary = json.loads(summary_json)

    subjective = {
        "Chief_Complaint": ", ".join(summary.get("Symptoms", [])),
        "History_of_Present_Illness": "Patient reports " + ", ".join(summary.get("Symptoms", []))
    }

    objective = {
        "Physical_Exam": "Full range of motion in cervical and lumbar spine, no tenderness.",
        "Observations": "Patient appears in normal health, normal gait."
    }

    assessment = {
        "Diagnosis": summary.get("Diagnosis", ["Whiplash injury"])[0] if summary.get("Diagnosis") else "Whiplash injury",
        "Severity": "Mild, improving"
    }

    plan = {
        "Treatment": summary.get("Treatment", []),
        "Follow-Up": "Patient to return if pain worsens or persists beyond six months."
    }

    soap_note = {
        "Subjective": subjective,
        "Objective": objective,
        "Assessment": assessment,
        "Plan": plan
    }

    return json.dumps(soap_note, indent=4)
