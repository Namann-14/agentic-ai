# working with file paths.
from pathlib import Path

# pretty print, self explanatory
from pprint import pp

# convert images -> arrays for ocr engine 
import numpy as np

import pdfplumber
# pillow image ??
from PIL import Image

# store extracted text and metadata
from langchain_core.documents import Document

from pypdf import PdfReader

# what's high level? 
from pdfminer.high_level import extract_pages
from pdfminer.image import ImageWriter
from pdfminer.layout import LTContainer, LTImage, LTTextContainer

from rapidocr_onnxruntime import RapidOCR

# creates a temp dir and deletes when finished. 
from tempfile import TemporaryDirectory

# path to file. 
path = Path(__file__).parent / "books" / "attention_is_all_you_need.pdf"

#checking if file exists 
print(path.exists())

# initializing ocr engine
ocr_engine = RapidOCR()


def extract_image_text(image: Image.Image) -> list[str]:
    result, _ = ocr_engine(np.array(image.convert("RGB")))
    if not result:
        return []

    return [
        item[1]
        for item in result
        if len(item) > 1 and item[1].strip()
    ]


def iter_pdfminer_images(element: LTContainer | LTImage):
    if isinstance(element, LTImage):
        yield element
    elif isinstance(element, LTContainer):
        for child in element:
            yield from iter_pdfminer_images(child)


# 1. pypdf
documents = []

with path.open("rb") as f:
    reader = PdfReader(f)
    total_pages = len(reader.pages)

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        image_texts = []

        for image_file in page.images:
            if image_file.image is None:
                raise ValueError(
                    f"Unable to decode image {image_file.name!r} "
                    f"on page {page_number}"
                )

            image_texts.extend(extract_image_text(image_file.image))

        if image_texts:
            page_text += (
                "\n\nText extracted from images:\n"
                + "\n".join(image_texts)
            )

        documents.append(
            Document(
                page_content=page_text,
                metadata={
                    "source": str(path),
                    "page": page_number,
                    "total_pages": total_pages,
                },
            )
        )

# 2. PDFMiner
page_layouts = list(extract_pages(path))
total_pages = len(page_layouts)
documents_pdfminer = []

with TemporaryDirectory() as image_dir:
    image_writer = ImageWriter(image_dir)

    for page_number, layout in enumerate(page_layouts, start=1):
        page_text = "".join(
            element.get_text()
            for element in layout
            if isinstance(element, LTTextContainer)
        )
        image_texts = []

        for image in iter_pdfminer_images(layout):
            image_path = Path(image_dir) / image_writer.export_image(image)
            with Image.open(image_path) as extracted_image:
                image_texts.extend(extract_image_text(extracted_image))

        if image_texts:
            page_text += (
                "\n\nText extracted from images:\n"
                + "\n".join(image_texts)
            )

        documents_pdfminer.append(
            Document(
                page_content=page_text,
                metadata={
                    "source": str(path),
                    "page": page_number,
                    "total_pages": total_pages,
                },
            )
        )

# 3. pdfplumber
documents_pdfplumber = []

with pdfplumber.open(path) as pdf:
    total_pages = len(pdf.pages)
 
    for page_number, page in enumerate(pdf.pages, start=1):
        page_text = page.extract_text() or ""
        image_texts = []

        for image in page.images:
            cropped_page = page.crop(
                (image["x0"], image["top"], image["x1"], image["bottom"])
            )
            with cropped_page.to_image(resolution=150).original as rendered_image:
                image_texts.extend(extract_image_text(rendered_image))

        if image_texts:
            page_text += (
                "\n\nText extracted from images:\n"
                + "\n".join(image_texts)
            )

        documents_pdfplumber.append(
            Document(
                page_content=page_text,
                metadata={
                    "source": str(path),
                    "page": page_number,
                    "total_pages": total_pages,
                },
            )
        )

print("pypdf documents:", len(documents))
print("PDFMiner documents:", len(documents_pdfminer))
pp(documents_pdfminer[0].metadata)
print("pdfplumber documents:", len(documents_pdfplumber))
pp(documents_pdfplumber[0].metadata)
