from fetch_page import fetch_page
from parse_page import parse_page
from write_to_csv import write_to_csv
from bs4 import BeautifulSoup

def get_dropdown_options(html):
    soup = BeautifulSoup(html,'html.parser')

    office_dropdown = soup.find("select",id="office")
    office_choices = office_dropdown.find_all("option")

    office_list = []

    for choice in office_choices:
        office_list.append(choice.text)

    return office_list


if __name__=="__main__":
    url = "https://nicar22-scraping.herokuapp.com/form/"
    selection_page = fetch_page(url)
    
    office_list = get_dropdown_options(selection_page)

    results_list = []
    for office in office_list:
        print(office)
        page = fetch_page(url, params={
            "office":office
        })
        if page != None:
            results = parse_page(page)
            
            for result in results:
                result.append(office)
                results_list.append(result)
    
    write_to_csv(results_list, "data/all_results.csv")


