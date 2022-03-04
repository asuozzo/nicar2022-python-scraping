from fetch_page import fetch_page
from bs4 import BeautifulSoup

def parse_page(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    table = soup.find("table")

    data = []

    rows = table.find_all("tr")

    for row in rows:
        data_row = []
        cells = row.find_all("td")
        for cell in cells:
            data_row.append(cell.text)
        data.append(data_row)

    return data
        

if __name__=="__main__":
    html_doc = fetch_page("https://nicar22-scraping.herokuapp.com/simpletable/")

    # soup = BeautifulSoup(html_doc, 'html.parser')
    
    # print header
    # header = soup.find('h2')
    # print(header.text)

    # print table contents
    # table = soup.find("table")
    # rows = table.find_all("tr")

    # for row in rows:
    #     cells = row.find_all("td")
    #     for cell in cells:
    #         print(cell)

    print(parse_page(html_doc))