from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class SmallLLM:
    def __init__(self):
        model_name = "google/flan-t5-small"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

        self.model.eval()

    def extract_entities(self, text: str) -> dict:

        prompt = (
            "Extract pizza type and size from the text.\n\n"
            "Allowed pizza types: Margherita, Pepperoni\n"
            "Allowed sizes: small, medium, large\n\n"
            "Return strictly in this format:\n"
            "pizza: <value or none>\n"
            "size: <value or none>\n\n"
            f"Text: {text}"
        )

        inputs = self.tokenizer(prompt, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=20
            )

        decoded = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        decoded = decoded.lower()

        pizza = None
        size = None

        if "margherita" in decoded:
            pizza = "Margherita"
        elif "pepperoni" in decoded:
            pizza = "Pepperoni"

        if "small" in decoded:
            size = "small"
        elif "medium" in decoded:
            size = "medium"
        elif "large" in decoded:
            size = "large"

        return {
            "pizza": pizza,
            "size": size
        }
