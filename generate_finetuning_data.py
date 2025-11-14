#!/usr/bin/env python3
"""
Script to generate LLM fine-tuning data from Near East University curriculum files.
Extracts academic content and generates Q&A pairs in CSV format.
"""

import os
import re
import csv
import json
from pathlib import Path

# Read all Python files and extract academic content
DATA_DIR = Path("/home/user/Neu/Data")

def extract_documents_from_file(filepath):
    """Extract the documents array content from a Python file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the documents array
        match = re.search(r'documents\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if not match:
            return []

        # Extract individual document strings
        docs_content = match.group(1)

        # Find all triple-quoted strings
        documents = []
        # Match both """ and ''' strings
        pattern = r'"""(.*?)"""|\'\'\'(.*?)\'\'\''
        matches = re.findall(pattern, docs_content, re.DOTALL)

        for match in matches:
            doc = match[0] if match[0] else match[1]
            if doc.strip():
                documents.append(doc.strip())

        return documents
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []

def get_department_name(filename):
    """Extract department name from filename."""
    name = filename.replace('.py', '').replace('_', ' ').replace('-', ' ')
    return ' '.join(word.capitalize() for word in name.split())

def parse_semester_courses(text):
    """Parse semester course information."""
    courses = []
    # Match course patterns like "MTH101, Calculus I, Credit 4, ECTS 5"
    course_pattern = r'([A-Z]{2,4}\d{3}),\s*([^,]+?)(?:,\s*(?:Credit|C:|T:).*)?(?:,\s*(?:ECTS|E:)\s*\d+)?'
    matches = re.findall(course_pattern, text)
    for match in matches:
        courses.append(f"{match[0]} ({match[1].strip()})")
    return courses

# Generate comprehensive Q&A pairs
qa_pairs = []

# Process all files
print("Processing curriculum files...")
all_department_data = {}

for py_file in sorted(DATA_DIR.glob("*.py")):
    dept_name = get_department_name(py_file.stem)
    documents = extract_documents_from_file(py_file)

    if documents:
        all_department_data[dept_name] = documents
        print(f"✓ Processed {dept_name}: {len(documents)} documents")

print(f"\nTotal departments processed: {len(all_department_data)}\n")

# Generate Q&A pairs for each department
print("Generating Q&A pairs...")

for dept_name, documents in all_department_data.items():

    # Get full document text
    full_text = "\n\n".join(documents)

    # Q1: General program information
    for doc in documents:
        if "program" in doc.lower() and ("information" in doc.lower() or "overview" in doc.lower() or "bachelor" in doc.lower() or "master" in doc.lower()):
            question = f"Tell me about the {dept_name} program at Near East University."
            answer = doc
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Program Information"
            })
            break

    # Q2: First year courses
    for doc in documents:
        if "first year" in doc.lower() and "first semester" in doc.lower():
            question = f"What courses will I take in the first year first semester of {dept_name}?"
            answer = f"In the first year first semester of {dept_name}, you will take the following courses:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Course Information"
            })
            break

    # Q3: First year second semester
    for doc in documents:
        if "first year" in doc.lower() and "second semester" in doc.lower():
            question = f"What are the courses in first year second semester for {dept_name}?"
            answer = f"The first year second semester courses for {dept_name} are:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Course Information"
            })
            break

    # Q4: Career opportunities
    for doc in documents:
        if "career" in doc.lower() and ("opportunities" in doc.lower() or "graduates" in doc.lower()):
            question = f"What career opportunities are available after graduating from {dept_name}?"
            answer = doc
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Career Information"
            })
            break

    # Q5: Mission and Vision
    for doc in documents:
        if "mission" in doc.lower() and "vision" in doc.lower():
            question = f"What are the mission and vision of the {dept_name} program?"
            answer = doc
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Program Information"
            })
            break

    # Q6: Elective courses
    for doc in documents:
        if "elective" in doc.lower() and len(doc) > 100:
            question = f"What elective courses are available in the {dept_name} program?"
            answer = f"The {dept_name} program offers the following elective courses:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Course Information"
            })
            break

    # Q7: Third year curriculum
    for doc in documents:
        if "third year" in doc.lower() and "first semester" in doc.lower():
            question = f"What subjects are studied in year 3 of {dept_name}?"
            answer = f"In the third year first semester of {dept_name}, you will study:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Curriculum"
            })
            break

    # Q8: Fourth/Final year
    for doc in documents:
        if ("fourth year" in doc.lower() or "final year" in doc.lower()) and "first semester" in doc.lower():
            question = f"What courses are in the final year of {dept_name}?"
            answer = f"The final year courses for {dept_name} include:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Course Information"
            })
            break

    # Q9: Second year courses
    for doc in documents:
        if "second year" in doc.lower() and "first semester" in doc.lower():
            question = f"What will I study in second year of {dept_name}?"
            answer = f"In the second year first semester of {dept_name}, you will study:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Curriculum"
            })
            break

    # Q10: Course descriptions
    for doc in documents:
        if "course description" in doc.lower() or ("objective" in doc.lower() and "content" in doc.lower()):
            question = f"Can you describe some key courses in {dept_name}?"
            answer = f"Here are descriptions of key courses in {dept_name}:\n\n{doc}"
            qa_pairs.append({
                "prompt": question,
                "messages": [
                    {"content": question, "role": "user"},
                    {"content": answer, "role": "assistant"}
                ],
                "category": "Course Details"
            })
            break

# Additional cross-department questions
print(f"Generated {len(qa_pairs)} department-specific Q&A pairs")

# Add general comparison questions
engineering_depts = [d for d in all_department_data.keys() if "engineering" in d.lower()]
if engineering_depts:
    question = "What engineering programs are available at Near East University?"
    answer = f"Near East University offers the following engineering programs:\n\n" + "\n".join([f"• {dept}" for dept in sorted(engineering_depts)])
    qa_pairs.append({
        "prompt": question,
        "messages": [
            {"content": question, "role": "user"},
            {"content": answer, "role": "assistant"}
        ],
        "category": "Department Listing"
    })

business_depts = [d for d in all_department_data.keys() if any(keyword in d.lower() for keyword in ["business", "economics", "management", "marketing"])]
if business_depts:
    question = "What business and economics programs does NEU offer?"
    answer = f"Near East University offers these business and economics programs:\n\n" + "\n".join([f"• {dept}" for dept in sorted(business_depts)])
    qa_pairs.append({
        "prompt": question,
        "messages": [
            {"content": question, "role": "user"},
            {"content": answer, "role": "assistant"}
        ],
        "category": "Department Listing"
    })

# Write to CSV
output_file = "/home/user/Neu/neu_llm_finetuning_data.csv"
print(f"\nWriting {len(qa_pairs)} Q&A pairs to CSV...")

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['prompt', 'messages', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for qa in qa_pairs:
        # Convert messages to JSON string
        messages_json = json.dumps(qa['messages'], ensure_ascii=False)

        writer.writerow({
            'prompt': qa['prompt'],
            'messages': messages_json,
            'category': qa['category']
        })

print(f"✓ Successfully created {output_file}")
print(f"✓ Total Q&A pairs: {len(qa_pairs)}")
print("\nCategories breakdown:")
category_counts = {}
for qa in qa_pairs:
    cat = qa['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

for cat, count in sorted(category_counts.items()):
    print(f"  • {cat}: {count}")
