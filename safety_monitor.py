import json

class MemorySafety:
    @staticmethod
    def detect_poisoning(memory_text):
        # Logic to detect adversarial injections or prompt leaks
        suspicious_terms = ["IGNORE ALL PREVIOUS INSTRUCTIONS", "SYSTEM_PROMPT_LEAK"]
        return any(term in memory_text.upper() for term in suspicious_terms)

    @staticmethod
    def export_report(stats):
        with open("safety_report.json", "w") as f:
            json.dump(stats, f, indent=4)