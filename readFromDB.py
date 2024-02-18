# Project 6
# Read contents from DB and display
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


# Reading questions by subject
def read_questions_by_subject(connection, chapter_name):
    try:
        cursor = connection.cursor()

        select_query = "SELECT * FROM questions WHERE chapterName = %s"
        cursor.execute(select_query, (chapter_name,))

        questions_data = cursor.fetchall()

        cursor.close()
        return questions_data

    except Error as e:
        print(f"Error: {e}")
        return None


# Specify the subject for which you want to retrieve questions
print("Enter the chapter for which you want to retrieve questions:")
chapter_to_search = input();

# Call the functions to create connection and read data
connection = create_connection()

if connection:
    # Read questions for the specified subject
    questions_data = read_questions_by_subject(connection, chapter_to_search)

    # Print the retrieved data
    if questions_data:
        print(f"Questions for '{chapter_to_search}':")
        for question_info in questions_data:
            print(question_info)
    else:
        print(f"No questions found for '{chapter_to_search}'.")

    # Close the connection
    connection.close()
