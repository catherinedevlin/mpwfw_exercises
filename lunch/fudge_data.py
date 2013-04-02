import csv
import BeautifulSoup
import requests

def get_usd_to_cad():
    page = requests.get('http://www.bankofcanada.ca/rates/exchange/')
    soup = BeautifulSoup.BeautifulSoup(page.text)
    rate_element = soup.find('th', text="1 CAD noon").next.text
    rate = rate_element.split()[0]
    rate = float(rate)
    return rate

def convert_currency(data, usd_to_foreign):
    foreign_data = []
    for row in data:
        foreign_row = []
        for val in row:
            try:
                foreign_val = round(val / usd_to_foreign, 2)
                foreign_row.append(foreign_val)
            except TypeError:
                foreign_row.append(val)
        foreign_data.append(foreign_row)
    return foreign_data

def read_sales_file(file_name):
    with open(file_name) as infile:
        data = []
        reader = csv.reader(infile)
        for row in reader:
            newrow = []
            for item in row:
                try:
                    newrow.append(float(item))
                except ValueError:
                    newrow.append(item)
            data.append(newrow)
    return data

def write_sales_file(file_name, data):
    with open(file_name, 'w') as outfile:
        writer = csv.writer(outfile)
        for row in data:
            writer.writerow(row)

data = read_sales_file('sales.csv')
usd_to_cad = get_usd_to_cad()
fudged_data = convert_currency(data, usd_to_cad)
write_sales_file('fudgey.csv', fudged_data)


