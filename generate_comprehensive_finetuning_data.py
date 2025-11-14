#!/usr/bin/env python3
"""
Enhanced script to generate comprehensive LLM fine-tuning data
from Near East University curriculum files.
Creates diverse, realistic Q&A pairs with extensive coverage.
"""

import os
import re
import csv
import json
import random
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

def create_qa_pair(question, answer, category):
    """Create a standardized Q&A pair."""
    return {
        "prompt": question,
        "messages": [
            {"content": question, "role": "user"},
            {"content": answer, "role": "assistant"}
        ],
        "category": category
    }

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
print("Generating comprehensive Q&A pairs...")

for dept_name, documents in all_department_data.items():

    # Question templates for variety
    first_semester_questions = [
        f"What courses will I take in the first year first semester of {dept_name}?",
        f"Tell me about first semester courses for {dept_name}",
        f"What subjects are in Year 1 Semester 1 for {dept_name}?",
        f"List the courses for first year first semester in {dept_name}",
        f"What will I study in my first semester of {dept_name}?",
    ]

    # Q1: General program information
    for doc in documents:
        if "program" in doc.lower() and any(keyword in doc.lower() for keyword in ["information", "overview", "bachelor", "master", "degree"]):
            questions = [
                f"Tell me about the {dept_name} program at Near East University.",
                f"What is the {dept_name} program?",
                f"Can you describe the {dept_name} program at NEU?",
                f"Give me information about {dept_name}",
                f"What can you tell me about studying {dept_name} at NEU?",
            ]
            for q in questions[:2]:  # Use 2 variations
                qa_pairs.append(create_qa_pair(q, doc, "Program Information"))
            break

    # Q2-Q9: Semester-specific questions
    semester_mappings = [
        ("first year", "first semester", "1", "1"),
        ("first year", "second semester", "1", "2"),
        ("second year", "first semester", "2", "1"),
        ("second year", "second semester", "2", "2"),
        ("third year", "first semester", "3", "1"),
        ("third year", "second semester", "3", "2"),
        ("fourth year", "first semester", "4", "1"),
        ("fourth year", "second semester", "4", "2"),
    ]

    for year_name, sem_name, year_num, sem_num in semester_mappings:
        for doc in documents:
            if year_name in doc.lower() and sem_name in doc.lower():
                questions = [
                    f"What courses will I take in {year_name} {sem_name} of {dept_name}?",
                    f"List the {year_name} {sem_name} courses for {dept_name}",
                    f"What subjects are in Year {year_num} Semester {sem_num} of {dept_name}?",
                    f"Tell me about {year_name} {sem_name} curriculum in {dept_name}",
                ]
                answer = f"In the {year_name} {sem_name} of {dept_name}, you will study:\n\n{doc}"
                # Add multiple question variations
                qa_pairs.append(create_qa_pair(questions[0], answer, "Course Information"))
                if len(questions) > 1:
                    qa_pairs.append(create_qa_pair(questions[1], answer, "Curriculum"))
                break

    # Q10: Career opportunities
    for doc in documents:
        if "career" in doc.lower() and ("opportunities" in doc.lower() or "graduates" in doc.lower()):
            questions = [
                f"What career opportunities are available after graduating from {dept_name}?",
                f"What jobs can I get with a {dept_name} degree?",
                f"What can I do after graduating from {dept_name}?",
                f"Tell me about career prospects for {dept_name} graduates",
                f"What are the employment opportunities for {dept_name}?",
            ]
            for q in questions[:3]:
                qa_pairs.append(create_qa_pair(q, doc, "Career Information"))
            break

    # Q11: Mission and Vision
    for doc in documents:
        if "mission" in doc.lower() and "vision" in doc.lower():
            questions = [
                f"What are the mission and vision of the {dept_name} program?",
                f"Tell me about the mission and vision of {dept_name}",
                f"What is the mission of the {dept_name} department?",
            ]
            for q in questions[:2]:
                qa_pairs.append(create_qa_pair(q, doc, "Program Information"))
            break

    # Q12: Elective courses
    for doc in documents:
        if "elective" in doc.lower() and len(doc) > 100:
            questions = [
                f"What elective courses are available in the {dept_name} program?",
                f"Tell me about elective courses for {dept_name}",
                f"What are the optional courses in {dept_name}?",
                f"List the elective courses for {dept_name}",
            ]
            answer = f"The {dept_name} program offers the following elective courses:\n\n{doc}"
            for q in questions[:2]:
                qa_pairs.append(create_qa_pair(q, answer, "Course Information"))
            break

    # Q13: Course descriptions
    for doc in documents:
        if "course description" in doc.lower() or ("objective" in doc.lower() and "content" in doc.lower()):
            questions = [
                f"Can you describe some key courses in {dept_name}?",
                f"What are the main courses in {dept_name}?",
                f"Tell me about the core courses in {dept_name}",
                f"Describe the important courses for {dept_name}",
            ]
            answer = f"Here are descriptions of key courses in {dept_name}:\n\n{doc}"
            for q in questions[:2]:
                qa_pairs.append(create_qa_pair(q, answer, "Course Details"))
            break

    # Q14: Program summary/duration
    for doc in documents:
        if any(keyword in doc.lower() for keyword in ["total ects", "240 ects", "duration", "semesters"]):
            questions = [
                f"How long is the {dept_name} program?",
                f"What is the duration of {dept_name} studies?",
                f"How many ECTS credits are required for {dept_name}?",
                f"How many years is the {dept_name} program?",
            ]
            for q in questions[:2]:
                qa_pairs.append(create_qa_pair(q, doc, "Program Information"))
            break

    # Q15: Specialization/Focus areas
    for doc in documents:
        if "focus" in doc.lower() or "specialization" in doc.lower():
            questions = [
                f"What are the focus areas of {dept_name}?",
                f"What specializations does {dept_name} offer?",
                f"What will I specialize in if I study {dept_name}?",
            ]
            for q in questions[:2]:
                qa_pairs.append(create_qa_pair(q, doc, "Program Information"))
            break

print(f"Generated {len(qa_pairs)} department-specific Q&A pairs")

# Additional cross-department and general questions
print("Adding cross-department questions...")

# Engineering programs
engineering_depts = [d for d in all_department_data.keys() if "engineering" in d.lower()]
if engineering_depts:
    eng_list = "\n".join([f"• {dept}" for dept in sorted(engineering_depts)])
    questions = [
        "What engineering programs are available at Near East University?",
        "List all engineering departments at NEU",
        "What engineering fields can I study at NEU?",
        "Tell me about engineering programs at Near East University",
    ]
    answer = f"Near East University offers the following engineering programs:\n\n{eng_list}"
    for q in questions[:2]:
        qa_pairs.append(create_qa_pair(q, answer, "Department Listing"))

# Business programs
business_depts = [d for d in all_department_data.keys() if any(keyword in d.lower() for keyword in ["business", "economics", "management", "marketing", "accounting"])]
if business_depts:
    bus_list = "\n".join([f"• {dept}" for dept in sorted(business_depts)])
    questions = [
        "What business and economics programs does NEU offer?",
        "List business programs at Near East University",
        "What can I study in the business field at NEU?",
        "Tell me about business administration programs at NEU",
    ]
    answer = f"Near East University offers these business and economics programs:\n\n{bus_list}"
    for q in questions[:2]:
        qa_pairs.append(create_qa_pair(q, answer, "Department Listing"))

# Communication programs
comm_depts = [d for d in all_department_data.keys() if any(keyword in d.lower() for keyword in ["communication", "journalism", "media", "cinema", "radio", "television"])]
if comm_depts:
    comm_list = "\n".join([f"• {dept}" for dept in sorted(comm_depts)])
    questions = [
        "What communication programs are available at NEU?",
        "List media and communication departments",
        "What can I study in communication at Near East University?",
    ]
    answer = f"Near East University offers these communication and media programs:\n\n{comm_list}"
    for q in questions[:2]:
        qa_pairs.append(create_qa_pair(q, answer, "Department Listing"))

# Architecture programs
arch_depts = [d for d in all_department_data.keys() if "architecture" in d.lower()]
if arch_depts:
    arch_list = "\n".join([f"• {dept}" for dept in sorted(arch_depts)])
    questions = [
        "What architecture programs does NEU have?",
        "Tell me about architecture programs at Near East University",
    ]
    answer = f"Near East University offers these architecture programs:\n\n{arch_list}"
    qa_pairs.append(create_qa_pair(questions[0], answer, "Department Listing"))

# Health Sciences programs
health_depts = [d for d in all_department_data.keys() if any(keyword in d.lower() for keyword in ["medicine", "nutrition", "dietetics", "audiology", "health", "bioengineering"])]
if health_depts:
    health_list = "\n".join([f"• {dept}" for dept in sorted(health_depts)])
    questions = [
        "What health sciences programs are available at NEU?",
        "List medical and health programs at Near East University",
    ]
    answer = f"Near East University offers these health sciences programs:\n\n{health_list}"
    qa_pairs.append(create_qa_pair(questions[0], answer, "Department Listing"))

# Computer Science / IT programs
cs_depts = [d for d in all_department_data.keys() if any(keyword in d.lower() for keyword in ["computer", "software", "information", "ai", "artificial intelligence", "cyber"])]
if cs_depts:
    cs_list = "\n".join([f"• {dept}" for dept in sorted(cs_depts)])
    questions = [
        "What computer science and IT programs does NEU offer?",
        "List computer and software programs at Near East University",
        "What can I study in computer science at NEU?",
    ]
    answer = f"Near East University offers these computer science and IT programs:\n\n{cs_list}"
    for q in questions[:2]:
        qa_pairs.append(create_qa_pair(q, answer, "Department Listing"))

# Add some general informational questions
all_depts_list = "\n".join([f"• {dept}" for dept in sorted(all_department_data.keys())])
qa_pairs.append(create_qa_pair(
    "What programs are available at Near East University?",
    f"Near East University offers the following programs:\n\n{all_depts_list}",
    "Department Listing"
))

qa_pairs.append(create_qa_pair(
    "How many departments does NEU have?",
    f"Near East University has {len(all_department_data)} different academic programs across various faculties including engineering, business, communication, health sciences, architecture, and more.",
    "General Information"
))

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
print(f"\n{'='*60}")
print("DATASET SUMMARY")
print('='*60)
print(f"Total Departments Covered: {len(all_department_data)}")
print(f"Total Q&A Pairs Generated: {len(qa_pairs)}")
print(f"\nCategories Breakdown:")
category_counts = {}
for qa in qa_pairs:
    cat = qa['category']
    category_counts[cat] = category_counts.get(cat, 0) + 1

for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"  • {cat}: {count} pairs")
print('='*60)
