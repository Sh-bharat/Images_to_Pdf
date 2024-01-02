import os
import img2pdf

directory_path = input("Enter folder location containing images: ")

if os.path.exists(directory_path):
    print("Folder Found.")
    image_files = os.listdir(directory_path)
    image_bytes = []

    for file_name in image_files:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "rb") as file:
            image_bytes.append(file.read())

    output_name = input("Enter output name for PDF: ")
    pdf_data = img2pdf.convert(image_bytes)

    with open(output_name + ".pdf", "wb") as file:
        file.write(pdf_data)

    print("PDF is generated and saved in the current directory.")
else:
    print("Folder doesn't exist.")

