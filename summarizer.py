"""
title: PDF Text Extractor Tool
author: Your Name
author_url: https://github.com/yourusername
funding_url: https://github.com/yourusername
version: 0.1.0
requirements: PyPDF2
"""

import os
from PyPDF2 import PdfReader


class Tools:
    def __init__(self):
        pass  # No initialization needed for text extraction

    def extract_text_from_pdf(self, pdf_content: bytes) -> str:
        """
        Extract text from the provided PDF content.
        :param pdf_content: The byte content of the PDF file.
        :return: Extracted text from the PDF or an error message.
        """
        try:
            reader = PdfReader(pdf_content)
            text = []
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
            return "\n".join(text)
        except Exception as e:
            return f"Error reading PDF file: {e}"




tool = Tools()
pdf_path = r"C:\Users\diogo.bento\Desktop\PRR\60 - ACADEMIC\Mário Amorim Lopes.pdf"  # Update this with your PDF's path
extracted_text = tool.extract_text_from_pdf(pdf_path)
print("Extracted Text:", extracted_text)


# test_pdf_text_extraction()