from flask import render_template, request, redirect, url_for, flash, send_file
from app import app, db, mail
from app.models import UserData
from app.utils import export_csv, export_pdf, extract_pdf_to_excel, store_excel_to_db
from flask_mail import Message
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show-data')
def show_data():
    data = UserData.query.all()
    return render_template('show_data.html', data=data)

@app.route('/export-csv')
def export_csv_route():
    filepath = export_csv()
    return send_file(filepath, as_attachment=True)

@app.route('/export-pdf')
def export_pdf_route():
    filepath = export_pdf()
    return send_file(filepath, as_attachment=True)

@app.route('/upload-excel', methods=['POST'])
def upload_excel():
    if 'file' not in request.files:
        flash('No file selected!', 'danger')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename.endswith('.xlsx'):
        store_excel_to_db(file)
        flash('Excel file uploaded successfully!', 'success')
    else:
        flash('Invalid file format! Please upload an Excel file.', 'danger')
    return redirect(url_for('index'))

@app.route('/extract-pdf', methods=['POST'])
def extract_pdf():
    if 'file' not in request.files:
        flash('No file selected!', 'danger')
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename.endswith('.pdf'):
        filepath = extract_pdf_to_excel(file)
        return send_file(filepath, as_attachment=True)
    else:
        flash('Invalid file format! Please upload a PDF file.', 'danger')
    return redirect(url_for('index'))

@app.route('/send-mail', methods=['POST'])
def send_mail():
    email = request.form.get('email')
    message = request.form.get('message')
    msg = Message('Hello from Dynamic Site', sender='your-email@gmail.com', recipients=[email])
    msg.body = message
    mail.send(msg)
    flash('Email sent successfully!', 'success')
    return redirect(url_for('index'))
