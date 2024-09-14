import os
import fitz

onlyfiles = sorted([f for f in os.listdir("./irs_pdfs/") if os.path.isfile(os.path.join("./irs_pdfs/", f))])
folder_location = r'./labeled_pdf_boxes'
if not os.path.exists(folder_location):os.mkdir(folder_location)

for file in onlyfiles:
    pdfDoc = fitz.open(os.path.join("./irs_pdfs/", file))
    with open(os.path.join("./labeled_pdf_boxes/", file[:-4] + ".txt"), "w") as f:
        for pageNum in range(pdfDoc.page_count):
            page = pdfDoc.load_page(pageNum)
            for field in page.widgets():
                rect = field.rect 
                f.write(f"{field.field_name}: {rect}\n")
    pdfDoc.close()
        
