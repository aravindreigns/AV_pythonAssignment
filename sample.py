import re

pdf_content = '''subjectName: Chemistry question: What is Au? answer: Au is Gold chapterName: Elements  subjectName: Maths question: What is 2 + 3? answer: Answer is 5 chapterName: Addition'''


def extract_info_from_pdf_content(pdf_content):
    # Define a pattern to match subjectName, question, answer, and chapterName
    pattern = r"subjectName: (.*?) question: (.*?) answer: (.*?) chapterName: (.*?)(?=(?:\s+subjectName|$))"

    # Use re.findall to find all matches in the pdf_content
    matches = re.findall(pattern, pdf_content)

    # Create a list to store dictionaries for each entry
    extracted_data = []

    for match in matches:
        subject_name, question, answer, chapter_name = match
        # Add the information to the list
        extracted_data.append({
            'subjectName': subject_name.strip(),
            'question': question.strip(),
            'answer': answer.strip(),
            'chapterName': chapter_name.strip()
        })

    return extracted_data


# Call the function to extract information from the pdf_content
result = extract_info_from_pdf_content(pdf_content)

# Print the extracted information
for entry in result:
    print(entry)
