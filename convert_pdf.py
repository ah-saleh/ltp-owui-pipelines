# from pdfminer.high_level import extract_text

# text = extract_text(r"C:\Users\diogo.bento\Desktop\PRR\60 - ACADEMIC\Mário Amorim Lopes.pdf")
# with open("output.md", "w", encoding="utf-8") as f:
#     f.write(text)

import os
from transformers import pipeline, SummarizationPipeline
from PyPDF2 import PdfReader

class Tools:
    def __init__(self):
        try:
            # Ensure the pipeline is initialized and check the type directly
            self.summarizer = pipeline("summarization")
            if not isinstance(self.summarizer, SummarizationPipeline):
                raise TypeError("Failed to initialize a valid SummarizationPipeline.")
        except Exception as e:
            self.error = f"Error initializing summarization pipeline: {e}"

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        if not os.path.isfile(pdf_path):
            return f"File not found: {pdf_path}"

        try:
            with open(pdf_path, 'rb') as file:
                reader = PdfReader(file)
                text = []
                for page in reader.pages:
                    text.append(page.extract_text())
            return "\n".join(text)
        except Exception as e:
            return f"Error reading PDF file: {e}"

    def summarize_text(self, text: str, summary_length: int = 130) -> str:
        if not text:
            return "No text to summarize."

        try:
            summary = self.summarizer(text, max_length=summary_length, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        except Exception as e:
            return f"Error summarizing text: {e}"

    def summarize_pdf(self, pdf_path: str) -> str:
        if hasattr(self, 'error'):
            return self.error
        
        text = self.extract_text_from_pdf(pdf_path)
        if text.startswith("Error"):
            return text

        summary = self.summarize_text(text)
        return summary