from pypdf import PdfReader

def extract_text(path):
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages)

if __name__ == "__main__":
    path = "samples/syllabus1.pdf"   # change to match your actual file name
    text = extract_text(path)
    print(f"Characters extracted: {len(text)}")
    print(text[:1500])