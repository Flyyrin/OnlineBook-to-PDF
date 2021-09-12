with open ("links.txt", "r") as links:
    cleaned_links = links.read().replace('	Image', '\n')

with open('output.txt', 'w') as output:
    output.write(cleaned_links)

# https://www.10bestseo.com/url-opener/
# https://pdfcandy.com/nl/png-to-pdf.html