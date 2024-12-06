import os
import pandas as pd
from fpdf import FPDF

def export_csv():
    data = [{"name": "John", "email": "john@example.com", "data": "Sample Data"}]
    filepath = 'uploaded_files/data.csv'
    pd.DataFrame(data).to_csv(filepath, index=False)
    return filepath

def export_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sample PDF Content", ln=True, align='C')
    filepath = 'uploaded_files/data.pdf'
    pdf.output(filepath)
    return filepath

def store_excel_to_db(file):
    df = pd.read_excel(file)
    # Logic to store data into the database

def extract_pdf_to_excel(file):
    # Extract data from PDF
    filepath = 'uploaded_files/extracted_data.xlsx'
    # Logic to save extracted data to an Excel file
    return filepath
