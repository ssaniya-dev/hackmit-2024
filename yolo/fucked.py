import os
import random

import fitz
import tqdm
from PIL import Image, ImageFilter, ImageDraw


def tilt_image(input_path, output_path, angle):
    if os.path.exists(output_path):
        return
    with Image.open(input_path) as img:
        rotated_img = img.rotate(angle, expand=True)
        rotated_img.save(output_path)


def blur_image(input_path, output_path, blur_radius=10):
    if os.path.exists(output_path):
        return
    # Open the image
    with Image.open(input_path) as img:
        # Apply Gaussian blur
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))

        # Save the blurred image
        blurred_img.save(output_path)
        print(f"Blurred image saved as {output_path}")


def expand_image_randomly(input_path, output_path, max_horizontal=6, max_vertical=3, dpi=300):
    if os.path.exists(output_path):
        return
    # Open the image
    with Image.open(input_path) as img:
        # Get the current size
        width, height = img.size

        # Calculate random expansion in inches
        expand_horizontal_inches = random.uniform(0, max_horizontal)
        expand_vertical_inches = random.uniform(0, max_vertical)

        # Convert inches to pixels
        expand_horizontal_pixels = int(expand_horizontal_inches * dpi)
        expand_vertical_pixels = int(expand_vertical_inches * dpi)

        # Calculate new dimensions
        new_width = width + expand_horizontal_pixels
        new_height = height + expand_vertical_pixels

        # Create a new image with the expanded size
        new_img = Image.new(img.mode, (new_width, new_height), (255, 255, 255))  # White background

        # Paste the original image onto the new image at (0,0)
        new_img.paste(img, (0, 0))

        # Save the expanded image
        new_img.save(output_path, dpi=(dpi, dpi))
        print(f"Expanded image saved as {output_path}")
        print(
            f"Expanded by {expand_horizontal_inches:.2f} in horizontally and {expand_vertical_inches:.2f} in vertically")

        return width / new_width, height / new_height


def draw_rectangles(input_path, output_path, rectangles, outline_color="red", outline_width=2):
    if os.path.exists(output_path):
        return
    # Open the image
    with Image.open(input_path) as img:
        # Create a drawing object
        draw = ImageDraw.Draw(img)

        # Draw each rectangle
        for rect in rectangles:
            (x1, y1), (x2, y2) = rect
            draw.rectangle([x1, y1, x2, y2], outline=outline_color, width=outline_width)

        # Save the image with the rectangles
        img.save(output_path)
        print(f"Image with {len(rectangles)} rectangles saved as {output_path}")


def pdf_to_png(pdf_path, output_folder, dpi=300):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document[page_number]

        # Set the resolution for rendering
        zoom = dpi / 72  # 72 is the default DPI for PDF
        matrix = fitz.Matrix(zoom, zoom)

        # Render page to an image
        pix = page.get_pixmap(matrix=matrix)

        filename = pdf_path.split("/")[-1].split(".")[-2]

        # Define output image path
        output_file = os.path.join(output_folder, f"{filename}_page_{page_number + 1}.png")

        # Save the image
        pix.save(output_file)

        print(f"Saved page {page_number + 1} as {output_file}")

    print(f"Conversion completed. {len(pdf_document)} pages converted to PNG.")

    # Close the PDF file
    pdf_document.close()


def parseTxtFile(file):
    with open(file) as f:
        lines = f.readlines()

    return [list(map(float, line.split(" "))) for line in lines]


def divideWH(lines, mw, mh):
    res = []
    for line in lines:
        [id, x1, y1, x2, y2] = line
        res.append([id, x1 * mw, y1 * mh, x2 * mw, y2 * mh])

    return res


def restore_lines(lines):
    return "\n".join([" ".join([str(w) for w in line]) for line in lines])


def main():
    for file in tqdm.tqdm(os.listdir("../utils/irs_pdfs")):
        pdf_to_png("../utils/irs_pdfs/" + file, "../images")

    # take images in "images/",

"""

    for file in tqdm.tqdm(os.listdir("../images/")):
        ofile = "../images/" + file

        tfile = "../utils/labeled_pdf_boxes/" + file.replace(".png", ".txt")
        lines = parseTxtFile(tfile)
        tfname = file.replace(".png", ".txt")

        blur_image(ofile, "fucked/blur_" + file, blur_radius=2)
        with open("labels/blur_" + tfname, 'w') as ff:
            ff.write(restore_lines(lines))

        mult = expand_image_randomly(ofile, "fucked/expanded_" + file)
        if mult is not None:
            mw, mh = mult
            newlines = divideWH(lines, mw, mh)
            with open("labels/expanded_" + tfname, 'w') as ff:
                ff.write(restore_lines(newlines))

        tilt_image(ofile, "fucked/tilt_" + file, random.random() * 10 - 5)
        with open("labels/tilt_" + tfname, 'w') as ff:
            ff.write(restore_lines(lines))

        tilt_image("fucked/expanded_" + file, "fucked/tilt_expanded_" + file, random.random() * 10 - 5)
        with open("labels/tilt_expanded_" + tfname, 'w') as ff:
            ff.write(restore_lines(newlines))

        blur_image("fucked/tilt_expanded_" + file, "fucked/tilt_expanded_blur_" + file, blur_radius=2)
        with open("labels/tilt_expanded_blur_" + tfname, 'w') as ff:
            ff.write(restore_lines(newlines))

        with open("labels/" + tfname, "w") as ff:
            ff.write(restore_lines(lines))

"""
if __name__ == "__main__":
    main()

