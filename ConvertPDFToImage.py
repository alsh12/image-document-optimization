from pdf2image import convert_from_path

def pdf_to_image(pdfPath):
    pages = convert_from_path(pdfPath,poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')
    print(len(pages))
    for i in range(len(pages)):
        savePath = './ConvertedImages/page' + str(i) + '.jpg'
        pages[i].save(savePath, 'JPEG')


pdf_to_image('./PDFs/sample-1.pdf')


