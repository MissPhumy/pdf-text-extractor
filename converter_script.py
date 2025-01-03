from pdf2image import convert_from_path
import cv2
import pytesseract
import os
import pandas as pd
import fitz  # PyMuPDF

# Step 1: Convert PDF to Images
def pdf_to_images(pdf_path, output_folder):
    pages = convert_from_path(pdf_path, dpi=300)
    os.makedirs(output_folder, exist_ok=True)
    image_paths = []
    for i, page in enumerate(pages):
        image_path = os.path.join(output_folder, f'page_{i + 1}.jpg')
        page.save(image_path, 'JPEG')
        image_paths.append(image_path)
    return image_paths

# Step 2: Preprocess Image for OCR
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return binary

# Step 3: Extract Table Data with Tesseract
def extract_table_data(image, num_columns):
    # Detect text with Tesseract
    text = pytesseract.image_to_string(image, config='--psm 6')  # PSM 6 assumes uniform block text
    lines = text.split('\n')
    rows = []
    for line in lines:
        cells = line.split()  # Split text into cells (you may need to fine-tune this for alignment)
        if len(cells) == num_columns:  # Match the expected number of columns
            rows.append(cells)
    return rows

# Step 4: Save Data to a DataFrame
def save_to_dataframe(rows, column_names):
    df = pd.DataFrame(rows, columns=column_names)
    return df

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    all_text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        all_text += page.get_text()
    return all_text

# Main Script
if __name__ == "__main__":
    pdf_path = 'scanned_document.pdf'
    output_folder = 'output_images'
    column_names = ['Column1', 'Column2', 'Column3', 'Column4']  # Define your column names
    num_columns = len(column_names)

    # Extract all text from PDF
    all_text = extract_text_from_pdf(pdf_path)
    print(all_text)

    # Convert PDF to images
    rows = []  # Initialize rows list
    image_paths = pdf_to_images(pdf_path, output_folder)

    # Process each image
    all_rows = []
    for image_path in image_paths:
        print(f"Processing: {image_path}")
        binary_image = preprocess_image(image_path)
        rows = extract_table_data(binary_image, num_columns)
        all_rows.extend(rows)  # Combine rows from all pages

    # Save to DataFrame
    df = save_to_dataframe(all_rows, column_names)
    print(df)

    # Save DataFrame to CSV
    df.to_csv('output.csv', index=False)
    print("Data saved to output.csv")
