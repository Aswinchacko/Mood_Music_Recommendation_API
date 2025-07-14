import os
import re

dataset_folder = "dataset"
input_file = "train.txt"
output_file = "train_cleaned.txt"

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s']", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def clean_file():
    os.makedirs(dataset_folder, exist_ok=True)
    with open(os.path.join(dataset_folder, input_file), "r", encoding="utf-8") as infile, \
         open(os.path.join(dataset_folder, output_file), "w", encoding="utf-8") as outfile:
        for line in infile:
            if ";" not in line:
                continue
            text, label = line.strip().split(";", 1)
            cleaned = f"{clean_text(text)};{label.strip().lower()}"
            outfile.write(cleaned + "\n")

clean_file()
print("✅ Dataset cleaned and saved as train_cleaned.txt")
