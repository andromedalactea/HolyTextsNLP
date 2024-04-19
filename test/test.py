import PyPDF2
from nltk.tokenize import word_tokenize
from nltk import download

download('punkt')  # Download the required NLTK models and corpora (if not already installed)

def count_tokens_in_pdf(pdf_path):
    """
    Counts the number of tokens in a PDF file.
    
    Args:
        pdf_path (str): The path to the PDF file.
    
    Returns:
        int: The number of tokens in the PDF.
    """
    token_count = 0
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:  # Check if text extraction is not None
                tokens = word_tokenize(text)
                token_count += len(tokens)
    return token_count

# Example usage
pdf_path = 'path_to_your_modified_pdf.pdf'
total_tokens = count_tokens_in_pdf(pdf_path)
print(f'The total number of tokens in the PDF is: {total_tokens}')
