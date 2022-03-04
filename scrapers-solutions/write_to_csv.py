import csv
from fetch_page import fetch_page
from parse_page import parse_page

def write_to_csv(data, outfile):
    f = open(outfile, "w")
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    f.close


if __name__=="__main__":
    html = fetch_page("https://nicar22-scraping.herokuapp.com/simpletable/")
    data = parse_page(html)
    write_to_csv(data, "data/senate_results.csv")