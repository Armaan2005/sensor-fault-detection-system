import os
import json
from groq import Groq


  

class GroqAssistant:
      
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate_explanation(self, question: str) -> str:
        summary_path = "artifacts/prediction_summary.json"

        if not os.path.exists(summary_path):
            return "Please run prediction first."

        with open(summary_path) as f:
            summary = json.load(f)

        system_prompt = f"""
You are an AI assistant explaining wafer fault detection results.

Model Used: {summary['model_name']}
Total Samples: {summary['total_samples']}
Good Wafers: {summary['good_count']}
Bad Wafers: {summary['bad_count']}

Explain clearly in simple engineering language.
"""

        response = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    def generate_explanation(self, user_question: str) -> str:
        summary_path = "artifacts/prediction_summary.json"

        if not os.path.exists(summary_path):
            return "Prediction summary not found. Please run prediction first."

        with open(summary_path, "r") as f:
            summary = json.load(f)

        system_prompt = f"""
You are an AI assistant helping engineers understand
machine learning predictions for wafer fault detection.

Prediction Summary:
- Model Used: {summary.get("model_name")}
- Total Wafers: {summary.get("total_samples")}
- Good Wafers: {summary.get("good_count")}
- Bad Wafers: {summary.get("bad_count")}
- Generated At: {summary.get("generated_at")}

Rules:
- Explain clearly in simple engineering language
- Base explanation ONLY on the summary
- Do NOT hallucinate
"""

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()