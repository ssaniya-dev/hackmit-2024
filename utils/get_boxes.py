import os
import fitz

onlyfiles = sorted([f for f in os.listdir("./irs_pdfs/") if os.path.isfile(os.path.join("./irs_pdfs/", f))])
folder_location = r'./labeled_pdf_boxes'
if not os.path.exists(folder_location):
    os.mkdir(folder_location)

for file in onlyfiles:
    pdfDoc = fitz.open(os.path.join("./irs_pdfs/", file))
    for pageNum in range(pdfDoc.page_count):
        page = pdfDoc.load_page(pageNum)
        
        width = page.rect.width
        height = page.rect.height
        outputPath = os.path.join(folder_location, f"{file[:-4]}_page_{pageNum + 1}.txt")

        with open(outputPath, "w") as f:
            for field in page.widgets():
                rect = field.rect

                normalized_x0 = rect.x0 / width
                normalized_y0 = rect.y0 / height
                normalized_x1 = rect.x1 / width
                normalized_y1 = rect.y1 / height
                
                f.write(f"0 {normalized_x0:.6f} {normalized_y0:.6f} {normalized_x1:.6f} {normalized_y1:.6f}\n")
        
    pdfDoc.close()
