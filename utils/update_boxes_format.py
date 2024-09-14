import os

onlyfiles = sorted([f for f in os.listdir("./labeled_pdf_boxes/") if os.path.isfile(os.path.join("./labeled_pdf_boxes/", f))])
for file in onlyfiles:
    if "_page_" not in file:
        os.remove(os.path.join("./labeled_pdf_boxes/", file))
for file in onlyfiles:
    fread = open(os.path.join("./labeled_pdf_boxes/", file), "r")
    lines = [line for line in fread]
    fread.close()
    f = open(os.path.join("./labeled_pdf_boxes/", file[:-4] + "pdf.txt"), "w")
    for line in lines:
        coords = [float(x) for x in line.split("(")[-1][:-1].split(", ")]
        f.write("0 " + normalize(coords))
    if os.path.exists(os.path.join("./labeled_pdf_boxes/", file)):
        os.remove(os.path.join("./labeled_pdf_boxes/", file))
        print("deleted " + file)
    
    



