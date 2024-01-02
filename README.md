
---

### Image to PDF Converter

This Python script (`pic2pdf.py`) converts multiple image files into a single PDF document. Users input the folder location containing images and specify the output PDF name. It utilizes the `img2pdf` library for conversion and `os` for file handling.

#### Installation Steps:

1. **Install Python:** If not already installed, download and install Python from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries:** Use `pip` to install the necessary libraries.
    ```bash
    pip install img2pdf
    ```

#### Usage:
1. **Run the Script:** Execute `pic2pdf.py`.
2. **Input:** Provide the folder path containing images when prompted.
3. **Output:** Specify the desired name for the generated PDF file.
4. **Result:** The script merges images into a PDF, saving it in the current directory.

#### Code:
```python
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
```

#### Notes:
- Ensure the folder contains compatible image files (JPEG, PNG, etc.) for successful conversion.
- The generated PDF will be saved in the same directory as the script.

---
