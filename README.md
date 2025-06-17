# 🔍 Toxic Comment Detection

This project uses the `unitary/toxic-bert` transformer model to detect toxic content in user comments. It can identify labels such as `toxic`, `insult`, `threat`, and more.

---

## 📌 Features

- Uses Hugging Face Transformers (`unitary/toxic-bert`)
- Multi-label classification (e.g., toxic, obscene, insult, threat)
- Runs on CPU or GPU (if available)
- Easy-to-use interactive command-line interface

---

## 📂 Labels Detected

- toxic  
- severe_toxic  
- obscene  
- threat  
- insult  
- identity_hate  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/toxic-comment-detector.git
cd toxic-comment-detector
```

### 2. Install Requirements

Make sure Python 3.7+ is installed.

```bash
pip install torch transformers
```

### 3. Run the Script

```bash
python main.py
```

You'll see:
```
Toxicity Checker Ready! Type 'exit' to stop.
```

### 4. Sample Interaction

```bash
Enter comment: I hate you
Prediction: Toxic: toxic, insult

Enter comment: You're a great friend!
Prediction: Not Toxic
```

---

## ⚙️ Model Details

- **Model**: [`unitary/toxic-bert`](https://huggingface.co/unitary/toxic-bert)
- **Library**: [Hugging Face Transformers](https://huggingface.co/transformers/)

---

## 📧 Contact

For any queries or suggestions, feel free to reach out:  
📩 **keerthivasang50@gmail.com**

---

## 📝 License

This project is for educational and research purposes only. Model credits to [Unitary](https://huggingface.co/unitary).
