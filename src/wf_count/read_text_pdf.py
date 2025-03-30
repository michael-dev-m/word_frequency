import pypdf


def get_text_pdf(url):
    # creating a pdf reader object
    reader = pypdf.PdfReader(url)

    # print the number of pages in pdf file
    print(len(reader.pages))

    # print the text of the first page

    texts = [reader.pages[i].extract_text() for i in range(len(reader.pages))]
    return texts