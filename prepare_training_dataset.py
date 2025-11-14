#!/usr/bin/env python3
"""
Prepare NEU curriculum data for LLM fine-tuning.
Creates clean Q&A format suitable for both general and reasoning tasks.
"""

import json
import csv

# Function to extract the assistant's answer from messages JSON
def extract_neu_answer(messages_str):
    """Extract assistant's response from messages JSON string"""
    try:
        messages = json.loads(messages_str)
        if messages and messages[-1]['role'] == 'assistant':
            return messages[-1]['content']
        else:
            return None
    except (json.JSONDecodeError, KeyError, IndexError):
        return None

# Function to clean and validate data
def clean_answer(answer):
    """Clean the answer text"""
    if answer is None:
        return None
    # Strip whitespace
    answer = answer.strip()
    return answer if answer else None

# Load and process the dataset
print("Loading dataset...")
input_file = '/home/user/Neu/neu_llm_finetuning_data.csv'
output_file = '/home/user/Neu/neu_training_dataset.csv'

training_data = []
total_count = 0
valid_count = 0
prompt_lengths = []
answer_lengths = []

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        total_count += 1
        prompt = row['prompt'].strip()
        answer = extract_neu_answer(row['messages'])
        answer = clean_answer(answer)

        if answer and prompt:
            training_data.append({
                'prompt': prompt,
                'answer': answer
            })
            valid_count += 1
            prompt_lengths.append(len(prompt))
            answer_lengths.append(len(answer))

print(f"Loaded {total_count} records")
print(f"Valid records: {valid_count}")

# Save the cleaned dataset
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['prompt', 'answer']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    writer.writeheader()
    for item in training_data:
        writer.writerow(item)

print(f"\n✓ Cleaned dataset saved to: {output_file}")
print(f"✓ Total training examples: {valid_count}")

# Show sample
print("\n" + "="*80)
print("SAMPLE TRAINING EXAMPLES")
print("="*80)
for i in range(min(3, len(training_data))):
    print(f"\n--- Example {i+1} ---")
    print(f"Prompt: {training_data[i]['prompt'][:100]}...")
    print(f"Answer: {training_data[i]['answer'][:150]}...")

# Statistics
if answer_lengths:
    print("\n" + "="*80)
    print("DATASET STATISTICS")
    print("="*80)
    print(f"Total examples: {valid_count}")
    print(f"Avg prompt length: {sum(prompt_lengths)/len(prompt_lengths):.0f} chars")
    print(f"Avg answer length: {sum(answer_lengths)/len(answer_lengths):.0f} chars")
    print(f"Min answer length: {min(answer_lengths)} chars")
    print(f"Max answer length: {max(answer_lengths)} chars")
    print("="*80)
