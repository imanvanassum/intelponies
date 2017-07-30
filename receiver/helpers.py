import re

def pagepicker(url_):
    page = re.search(r'game\/([^.]*(?=\?))', url_, re.M)
    # print('Submitted page is: ',page.group(1).rstrip())
    return page.group(1).rstrip()

if __name__ == '__main__':
    pagepicker()
