import os
from docx import Document

def convert_docx_to_txt(docx_file, txt_file):
    # Open the .docx file
    doc = Document(docx_file)

    # Extract text from the document
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'

    # Write the extracted text to a .txt file with UTF-8 encoding
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(text)

def batch_convert_folder(folder_path):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):

        docx_file = os.path.join(folder_path, filename)

        # Define the corresponding .txt file name
        txt_file = os.path.splitext(docx_file)[0] + '.txt'
        convert_docx_to_txt(docx_file, txt_file)

# Example usage:
folder_path = '/Users/filepath/'
batch_convert_folder(folder_path)
