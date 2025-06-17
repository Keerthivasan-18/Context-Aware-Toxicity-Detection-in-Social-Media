import re
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import sigmoid

MODEL_NAME = "unitary/toxic-bert"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.to(DEVICE)
model.eval()

LABELS = [
    "toxic", 
    "severe_toxic", 
    "obscene", 
    "threat", 
    "insult", 
    "identity_hate"
]

def preprocess(text):
    return re.sub(r"http\S+", "", text).strip()

def predict(text, threshold=0.7):
    text = preprocess(text)
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    ).to(DEVICE)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = sigmoid(outputs.logits)[0]

    labels_above_threshold = [LABELS[i] for i, p in enumerate(probs) if p.item() > threshold]

    if labels_above_threshold:
        return f"Toxic: {', '.join(labels_above_threshold)}"
    return "Not Toxic"

if __name__ == "__main__":
    print(f"Toxicity Checker Ready! (Device: {DEVICE}) Type 'exit' to stop.\n")

    while True:
        user_input = input("Enter comment: ")
        if user_input.lower() == "exit":
            break

        result = predict(user_input)
        print(f"Prediction: {result}\n")
