# Project 3
# Read contents of a particular PDF File page
import os

import PyPDF2


def read_pdf_write_to_text(page_number, pdf_folder, pdf_filename, output_filename):
    # Check if the folder exists
    if not os.path.exists(pdf_folder):
        print(f"Error: Folder '{pdf_folder}' not found.")
        return
    else:
        print("Folder Exists!")

    # Check if the PDF file exists
    pdf_filepath = os.path.join(pdf_folder, pdf_filename)
    if not os.path.exists(pdf_filepath):
        print(f"Error: PDF file '{pdf_filename}' not found in '{pdf_folder}'.")
        return
    else:
        print("File Exists", " ", pdf_filepath)

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

            if (page_number > len(pdf_reader.pages)):
                print("Error: Page number is more than the total number of pages in the PDF file.")
                return

            # Extract text from all pages
            print("Reading page number ", page_number, " from the PDF file")
            text_content = ""
            page = pdf_reader.pages[page_number]
            text_content += page.extract_text()
            # print(text_content)

            # Check if the output folder exists, create if not
            output_folder = os.path.join(pdf_folder)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            else:
                print("Output folder exists!")

            # Write the content to the output.txt file
            output_filepath = os.path.join(output_folder, output_filename)
            with open(output_filepath, 'w', encoding='utf-8') as output_file:
                output_file.write(text_content)

            print("PDF content successfully written to '{}'.".format(output_filepath))

    except Exception as e:
        print(e)


# Specify the folder, PDF filename, and output filename
page = int(input("Enter the page number of PDF: "))
print(page)
pdf_folder = './content'
pdf_filename = 'PDFFile.pdf'
output_filename = 'output.txt'

# Call the function
read_pdf_write_to_text(page, pdf_folder, pdf_filename, output_filename)
