# Project 2
# Traverse through folder tree and filter PDF files
import os

import PyPDF2

'''Function to read the PDF file and write the output to the file in text format'''


def read_pdf_write_to_text(pdf_folder, pdf_filename, output_filename):
    # Check if the folder exists
    if not os.path.exists(pdf_folder):
        print(f"Error: Folder '{pdf_folder}' not found.")
        return
    else:
        '''print("Folder Exists!")'''

    # Check if the PDF file exists
    pdf_filepath = os.path.join(pdf_folder, pdf_filename)
    if not os.path.exists(pdf_filepath):
        print("Error: PDF file '{pdf_filename}' not found in '{pdf_folder}'.")
        return
    else:
        '''print("File Exists", " ", pdf_filepath)'''

    # Read PDF and write to text file
    try:
        with open(pdf_filepath, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Check if PDF has any pages
            if len(pdf_reader.pages) == 0:
                print(f"Error: PDF file '{pdf_filename}' is empty.")
                return
            else:
                print("PDF file has ", len(pdf_reader.pages), " Pages")

            # Extract text from all pages
            text_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content += page.extract_text()
                # print(text_content)

            # Check if the output folder exists, create if not
            output_folder = os.path.join(pdf_folder)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            else:
                '''print("Output folder exists!")'''

            # Write the content to the output.txt file
            output_filepath = os.path.join(output_folder, output_filename)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(text_content)

            print("PDF content successfully written to '{}'.".format(output_filepath))

    except Exception as e:
        print(e)


'''Function to iterate given folder recursively'''


def find_pdf_files_recursive(folder):
    pdf_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))

    return pdf_files


'''Main Code to drive the program'''
# Specify the root folder to start the search
root_folder = './content'

# Get a list of PDF files with full paths
pdf_files_list = find_pdf_files_recursive(root_folder)

# Print the list of PDF files
for pdf_file in pdf_files_list:
    print(pdf_file)
    read_pdf_write_to_text(os.path.dirname(pdf_file), os.path.basename(pdf_file), 'output.txt')
