#!/usr/bin/env python3
"""
LLM Training Data Preparation Script
Prepares NEU curriculum dataset for both general Q&A and chain-of-thought reasoning fine-tuning.

Dataset: neu_training_dataset.csv
Output: Formatted datasets ready for training
"""

# ============================================================================
# STEP 1: Load the Dataset
# ============================================================================
print("="*80)
print("STEP 1: LOADING DATASET")
print("="*80)

import pandas as pd
from datasets import Dataset

# Load CSV file into pandas DataFrame
df = pd.read_csv('neu_training_dataset.csv')
print(f"✓ Loaded {len(df)} records from CSV")

# Convert pandas DataFrame to Hugging Face Dataset
dataset = Dataset.from_pandas(df)
print("✓ Dataset loaded and converted successfully:")
print(dataset)

# ============================================================================
# STEP 2: Define Answer Extraction Function
# ============================================================================
print("\n" + "="*80)
print("STEP 2: DEFINING EXTRACTION FUNCTION")
print("="*80)

def extract_neu_answer(answer_str):
    """
    Extract the answer from the dataset.
    For the cleaned dataset, this is straightforward.
    """
    return answer_str if answer_str else None

print("✓ Extraction function defined")

# ============================================================================
# STEP 3: Prepare for Reasoning Task (Chain-of-Thought)
# ============================================================================
print("\n" + "="*80)
print("STEP 3: PREPARING REASONING DATASET")
print("="*80)

# Define special tokens
reasoning_start = "<start_working_out>"
reasoning_end   = "<end_working_out>"
solution_start = "<SOLUTION>"
solution_end = "</SOLUTION>"

# Define system prompt
system_prompt = \
f"""You are given a problem.
Think about the problem and provide your working out.
Place it between {reasoning_start} and {reasoning_end}.
Then, provide your solution between {solution_start}{solution_end}"""

# Map dataset for reasoning task
reasoning_dataset = dataset.map(lambda x: {
    "prompt" : [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": x["prompt"]},
    ],
    "answer": f"{reasoning_start}Let's think step by step.{reasoning_end}{solution_start}{extract_neu_answer(x['answer'])}{solution_end}",
})

print("✓ Reasoning dataset prepared")
print("\nReasoning Dataset Example:")
print("-" * 80)
print("Prompt structure:")
for msg in reasoning_dataset[0]["prompt"]:
    print(f"  Role: {msg['role']}")
    print(f"  Content: {msg['content'][:100]}...")
print(f"\nAnswer preview: {reasoning_dataset[0]['answer'][:200]}...")

# ============================================================================
# STEP 4: Prepare for General Task (Direct Q&A)
# ============================================================================
print("\n" + "="*80)
print("STEP 4: PREPARING GENERAL DATASET")
print("="*80)

# Map dataset for general task
general_dataset = dataset.map(lambda x: {
    "prompt" : x["prompt"],
    "answer": extract_neu_answer(x["answer"]),
})

print("✓ General dataset prepared")
print("\nGeneral Dataset Example:")
print("-" * 80)
print(f"Prompt: {general_dataset[0]['prompt']}")
print(f"Answer: {general_dataset[0]['answer'][:200]}...")

# ============================================================================
# SUMMARY AND VALIDATION
# ============================================================================
print("\n" + "="*80)
print("DATASET PREPARATION SUMMARY")
print("="*80)
print(f"Original Dataset Size: {len(dataset)} examples")
print(f"Reasoning Dataset Size: {len(reasoning_dataset)} examples")
print(f"General Dataset Size: {len(general_dataset)} examples")
print()
print("Reasoning Format:")
print("  - Prompt: List of dicts with 'role' and 'content' (system + user)")
print("  - Answer: Formatted with reasoning tags and solution tags")
print()
print("General Format:")
print("  - Prompt: Simple string (user question)")
print("  - Answer: Simple string (direct answer)")
print()
print("✓ Both datasets ready for fine-tuning!")
print("="*80)

# ============================================================================
# VALIDATION CHECKS
# ============================================================================
print("\n" + "="*80)
print("VALIDATION CHECKS")
print("="*80)

# Check reasoning dataset structure
sample_reasoning = reasoning_dataset[0]
assert isinstance(sample_reasoning["prompt"], list), "Reasoning prompt should be a list"
assert len(sample_reasoning["prompt"]) == 2, "Reasoning prompt should have 2 messages"
assert sample_reasoning["prompt"][0]["role"] == "system", "First message should be system"
assert sample_reasoning["prompt"][1]["role"] == "user", "Second message should be user"
assert reasoning_start in sample_reasoning["answer"], "Answer should contain reasoning_start tag"
assert reasoning_end in sample_reasoning["answer"], "Answer should contain reasoning_end tag"
assert solution_start in sample_reasoning["answer"], "Answer should contain solution_start tag"
assert solution_end in sample_reasoning["answer"], "Answer should contain solution_end tag"
print("✓ Reasoning dataset structure validated")

# Check general dataset structure
sample_general = general_dataset[0]
assert isinstance(sample_general["prompt"], str), "General prompt should be a string"
assert isinstance(sample_general["answer"], str), "General answer should be a string"
print("✓ General dataset structure validated")

print("\n✓ All validation checks passed!")
print("="*80)

# ============================================================================
# SAVE PREPARED DATASETS (Optional)
# ============================================================================
print("\nSaving datasets...")
reasoning_dataset.save_to_disk("neu_reasoning_dataset")
general_dataset.save_to_disk("neu_general_dataset")
print("✓ Datasets saved to disk:")
print("  - neu_reasoning_dataset/")
print("  - neu_general_dataset/")
print("\n" + "="*80)
print("PREPARATION COMPLETE!")
print("="*80)
