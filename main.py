import img2pdf
from os import listdir, getcwd
from os.path import isfile, join

def convert_jpg_to_pdf(image_path, pdf_path):
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(image_path))

def convert_directory_jpg_to_pdf(dir_path, pdf_path):
    image_files = [join(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f)) and f.lower().endswith(('.jpg', '.jpeg'))]
    with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_files))

convert_directory_jpg_to_pdf(getcwd(),"output.pdf")