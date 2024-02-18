# Project 5
# Read contents of a PDF File and store in DB
import re

import PyPDF2
import mysql.connector
from mysql.connector import Error


# Connecting to MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Robinhood1@',
            database='questionBank'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


# Inserting questions into the database
def insert_questions(connection, questions_data):
    try:
        cursor = connection.cursor()

        for question_info in questions_data:
            insert_query = """
            INSERT INTO questions (subjectName, question, answer, chapterName)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                question_info['subjectName'],
                question_info['question'],
                question_info['answer'],
                question_info['chapterName']
            ))

        connection.commit()
        cursor.close()
        print(f"{len(questions_data)} records successfully inserted into the 'questions' table.")
    except Error as e:
        print(f"Error: {e}")


# Reading the contents of a PDF file
def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Initialize an empty list to store the lines
            pdf_lines = []

            # Loop through all pages in the PDF
            for page_num in range(len(pdf_reader.pages)):
                lines = pdf_reader.pages[page_num].extract_text().splitlines()
                pdf_lines.extend(lines)

            # Combine the lines into a single string with preserved newlines
            pdf_text = '\n'.join(pdf_lines)

            return pdf_text

    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return None


# Extracting subjectName, question, answer, and chapterName from the PDF content
def extract_subject_questions(pdf_content):
    # Define a pattern to match subjectName, question, answer, and chapterName
    pattern = r"subjectName: (.*?) question: (.*?) answer: (.*?) chapterName: (.*?)(?=(?:\s+subjectName|$))"

    # Use re.findall to find all matches in the pdf_content
    matches = re.findall(pattern, pdf_content)

    # Create a list to store dictionaries for each subject
    subject_questions = []

    for match in matches:
        subject_name, question, answer, chapter_name = match
        # Add the subject, question, answer, and chapterName to the list
        subject_questions.append({
            'subjectName': subject_name.strip(),
            'question': question.strip(),
            'answer': answer.strip(),
            'chapterName': chapter_name.strip()
        })

    return subject_questions


# Driver Code for the program
# Specify the path to your PDF file
pdf_file_path = './content/questionBank.pdf'  # Replace with your actual PDF file path

# Call the function to read the PDF file and store the text in a variable
pdf_content = read_pdf(pdf_file_path)

# Print or use the pdf_content variable as needed
if pdf_content:
    print(pdf_content)

# Call the function to extract subjectName, question, answer, and chapterName for each subject
result = extract_subject_questions(pdf_content)
print(result)
# Print the extracted information for each subject
for subject_info in result:
    print(f"\nSubject: {subject_info['subjectName']}")
    print(f"  Question: {subject_info['question']}")
    print(f"  Answer: {subject_info['answer']}")
    print(f"  ChapterName: {subject_info['chapterName']}")

connection = create_connection()
if connection:
    insert_questions(connection, result)
    # Close the connection
    connection.close()
