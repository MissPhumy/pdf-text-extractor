# PDF Text Extractor

This project provides a script to extract text from PDF documents, including tables and images, and prepare the data for training a text detection model.

## Features
- Extract text from PDF documents using PyMuPDF
- Convert PDF pages to images using pdf2image
- Extract text from images using Tesseract OCR
- Preprocess and combine extracted text for training

## Requirements
- Python 3.x
- PyMuPDF
- pdf2image
- OpenCV
- pytesseract
- pandas

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/missphumy/pdf-text-extractor.git
   cd pdf-text-extractor
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Install Tesseract OCR:
   ```
   sudo apt-get install tesseract-ocr
   ```

## Usage
1. Place your PDF document in the project directory.
2. Run the script to extract text:
   ```
   python converter_script.py
   ```

3. The extracted text will be saved to 
```
extracted_text.txt
```

## License
```
This project is licensed under the MIT License.
```

### requirements.txt

```
PyMuPDF
pdf2image
opencv-python
pytesseract
pandas
