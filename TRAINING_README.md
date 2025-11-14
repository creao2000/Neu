# NEU Curriculum LLM Fine-tuning Dataset

## 📊 Dataset Overview

This repository contains a clean, formatted dataset for fine-tuning Large Language Models on Near East University curriculum information.

**Dataset File:** `neu_training_dataset.csv`
**Total Examples:** 1,101 Q&A pairs
**Departments Covered:** 49 academic programs
**Format:** Simple prompt-answer pairs

## 📁 Files Description

### Core Dataset Files

1. **`neu_training_dataset.csv`** - Clean Q&A dataset
   - Columns: `prompt`, `answer`
   - No unnecessary metadata
   - Ready for direct training use

2. **`neu_llm_finetuning_data.csv`** - Original dataset
   - Contains raw data with categories
   - Includes JSON message format
   - Source for generating training data

### Preparation Scripts

3. **`prepare_training_dataset.py`** - Data cleaning script
   - Extracts prompts and answers
   - Removes unnecessary fields
   - Validates data quality

4. **`load_and_prepare_for_training.py`** - Training preparation script
   - Loads dataset into Hugging Face format
   - Prepares data for both training modes:
     - **General Q&A** - Direct question-answer pairs
     - **Chain-of-Thought Reasoning** - With reasoning tags

### Generation Scripts

5. **`generate_finetuning_data.py`** - Initial generation script
6. **`generate_comprehensive_finetuning_data.py`** - Enhanced generation script

## 🚀 Quick Start

### Step 1: Load the Dataset

```python
import pandas as pd
from datasets import Dataset

# Load CSV file
df = pd.read_csv('neu_training_dataset.csv')

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(df)
print(f"Loaded {len(dataset)} examples")
```

### Step 2: Choose Your Training Format

#### Option A: General Q&A Format (Direct Answers)

```python
# Dataset is already in general format
# Each example has:
# - prompt: "What courses are in first year of AI Engineering?"
# - answer: "In the first year of AI Engineering, you will study..."

general_dataset = dataset.map(lambda x: {
    "prompt": x["prompt"],
    "answer": x["answer"]
})

print(general_dataset[0])
```

**Output:**
```python
{
  'prompt': 'What courses will I take in first year first semester of Ai Engineering?',
  'answer': 'In the first year first semester of Ai Engineering, you will study:\n\nMTH113, Linear Algebra...'
}
```

#### Option B: Chain-of-Thought Reasoning Format

```python
# Define reasoning tags
reasoning_start = "<start_working_out>"
reasoning_end = "<end_working_out>"
solution_start = "<SOLUTION>"
solution_end = "</SOLUTION>"

# System prompt for reasoning
system_prompt = f"""You are given a problem.
Think about the problem and provide your working out.
Place it between {reasoning_start} and {reasoning_end}.
Then, provide your solution between {solution_start}{solution_end}"""

# Format dataset for reasoning
reasoning_dataset = dataset.map(lambda x: {
    "prompt": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": x["prompt"]},
    ],
    "answer": f"{reasoning_start}Let's think step by step.{reasoning_end}{solution_start}{x['answer']}{solution_end}",
})

print(reasoning_dataset[0])
```

**Output:**
```python
{
  'prompt': [
    {'role': 'system', 'content': 'You are given a problem...'},
    {'role': 'user', 'content': 'What courses will I take in first year...'}
  ],
  'answer': '<start_working_out>Let\'s think step by step.<end_working_out><SOLUTION>In the first year...'
}
```

### Step 3: Run Complete Preparation (Optional)

```bash
# Run the comprehensive preparation script
python3 load_and_prepare_for_training.py
```

This script will:
- Load the dataset
- Create both general and reasoning formats
- Validate data structure
- Save prepared datasets to disk

## 📋 Dataset Format Details

### Simple CSV Format

```csv
"prompt","answer"
"Tell me about the AI Engineering program","Near East University Faculty of..."
"What courses are in Year 1 Semester 1?","In the first year first semester..."
```

### Dataset Statistics

- **Total Examples:** 1,101
- **Average Prompt Length:** 66 characters
- **Average Answer Length:** 758 characters
- **Minimum Answer Length:** 130 characters
- **Maximum Answer Length:** 3,718 characters

## 🎯 Training Use Cases

### 1. General Question-Answering
Fine-tune models for direct curriculum questions:
- Course listings
- Program information
- Career opportunities
- Admission requirements

### 2. Chain-of-Thought Reasoning
Train models to:
- Explain reasoning process
- Provide step-by-step answers
- Demonstrate logical thinking
- Validate structured outputs

## 🔧 Requirements

### Python Packages
```bash
pip install pandas datasets
```

### Optional (for advanced training)
```bash
pip install transformers torch accelerate
```

## 📊 Content Coverage

### Engineering Programs (17)
AI Engineering, Automotive, Bioengineering, Civil, Computer, Cyber Security, Electrical, Environmental, Food, Industrial, Information Systems, Mechanical, Mechatronics, Nanotechnology, Petroleum, Software, Traffic & Transportation

### Business & Economics (8)
Business Administration, Banking & Accounting, Economics, EU Relations, HR Management, International Business, MIS, Marketing

### Communication (5)
Journalism, Filmmaking & Broadcasting, Public Relations, Radio/TV/Cinema, Visual Communication Design

### Architecture (3)
Architecture, Architecture (English), Landscape Architecture

### Health Sciences (4)
Medicine, Nutrition & Dietetics, Audiology, Sports Sciences

### Other Programs (12)
Analytics Engineering, Cartoon & Animation, CIS, Construction Technology, International Relations, MBA, PhD Business Admin, Political Science, Theology (2), Tourism

## 🎓 Question Types

- **Program Information:** Duration, ECTS, degree type, focus areas
- **Course Information:** Semester listings, course codes, credits
- **Curriculum:** Year-by-year breakdown, prerequisites
- **Career Information:** Job opportunities, career paths
- **Course Details:** Descriptions, objectives, content
- **Department Listings:** Available programs by field

## ⚠️ Important Notes

### For GRPO Training
When using the GRPOTrainer:
- **Reasoning Format:** Reward functions must validate:
  - Structural integrity of reasoning tags
  - Correctness of final solution
  - Proper tag placement

- **General Format:** Reward functions should focus on:
  - Correctness of answer
  - Relevance to question
  - Completeness of information

### Data Quality
- All data extracted from official curriculum documents
- No code or implementation details included
- Pure academic content only
- Validated 100% success rate

## 📝 Example Training Code

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load dataset
dataset = load_dataset('csv', data_files='neu_training_dataset.csv')

# Load model and tokenizer
model_name = "your-base-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Format for training
def format_instruction(example):
    return {
        "text": f"### Question:\n{example['prompt']}\n\n### Answer:\n{example['answer']}"
    }

formatted_dataset = dataset.map(format_instruction)

# Continue with your training pipeline...
```

## 🔄 Updating the Dataset

To regenerate or update the dataset:

```bash
# 1. Clean and prepare from original data
python3 prepare_training_dataset.py

# 2. Format for training
python3 load_and_prepare_for_training.py
```

## 📄 License

This dataset contains public curriculum information from Near East University.

## 🤝 Contributing

To add more departments or update information:
1. Add curriculum data to the `Data/` folder
2. Run generation scripts
3. Validate output
4. Submit pull request

---

**Last Updated:** 2025-11-14
**Version:** 1.0
**Maintainer:** NEU AI Training Data Project
