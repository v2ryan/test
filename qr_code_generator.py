import os
import qrcode
from PIL import Image
import pandas as pd

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Change this to the path of your Excel file
excel_file = 'qr.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file)

# Assuming the links are in the 'Link' column; change this if needed
links = df['Link'].tolist()

# Create a directory to store the generated QR codes
output_dir = "qr_codes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate QR codes for each link
for index, link in enumerate(links):
    output_filename = os.path.join(output_dir, f'qr_code_{index}.png')
    generate_qr_code(link, output_filename)
    print(f'Generated QR code for {link} and saved as {output_filename}')
