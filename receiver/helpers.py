import re

def pagepicker(url_):
    page = re.search(r'game\/([^.]*(?!\?))', url_, re.M)
    return page.group(1).rstrip()

def kddetailsparser(data):
    nr_of_provs = re.search(r'Total Provinces\s*(\d+))', data, re.M)
    return nr_of_provs(1).rstrip()

if __name__ == '__main__':
    pagepicker()
