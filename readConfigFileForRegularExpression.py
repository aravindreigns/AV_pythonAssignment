# Project 4
# Read contents of a config file and execute the regex

import configparser
import os
import re

import PyPDF2


def read_pdf_write_to_text(pdf_folder, pdf_filename, output_filename, config_filename):
    # Check if the folder exists
    if not os.path.exists(pdf_folder):
        print("Error: Folder '{pdf_folder}' not found.")
        return

    # Check if the PDF file exists
    pdf_filepath = os.path.join(pdf_folder, pdf_filename)
    if not os.path.exists(pdf_filepath):
        print(f"Error: PDF file '{pdf_filename}' not found in '{pdf_folder}'.")
        return

    # Read configuration from the file
    config = configparser.ConfigParser()
    try:
        config.read(config_filename)
        regex_pattern = config.get('config', 'regex')
    except configparser.Error as e:
        print(f"Error reading configuration file: {e}")
        return

    # Check if regex is provided in the configuration
    if not regex_pattern:
        print("Error: Regular expression not found in the configuration file.")
        return

    # Read PDF and write to text file
    try:
        with open(pdf_filepath, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Check if PDF has any pages
            if len(pdf_reader.pages) == 0:
                print(f"Error: PDF file '{pdf_filename}' is empty.")
                return

            # Extract text matching the regex pattern
            text_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content += page.extract_text()
                print(text_content)

            # Apply the regular expression to extract specific content
            match = re.search(regex_pattern, text_content)
            if match:
                extracted_content = match.group()
                print("----")
                print(extracted_content)
            else:
                extracted_content = "No matching content found with the provided regular expression."

            # Check if the output folder exists, create if not
            output_folder = os.path.join(pdf_folder, 'output')
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Write the extracted content to the output.txt file
            output_filepath = os.path.join(output_folder, output_filename)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(extracted_content)

            print(f"Extracted content successfully written to '{output_filepath}'.")

    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")


# Specify the folder, PDF filename, output filename, and config filename
pdf_folder = './content'
pdf_filename = 'PDFFile.pdf'  # Change this to your PDF file name
output_filename = 'output.txt'
config_filename = './content/config.ini'  # Change this to your configuration file name

# Call the function
read_pdf_write_to_text(pdf_folder, pdf_filename, output_filename, config_filename)
