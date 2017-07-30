import re

def pagepicker(self, url_, *args, **kwargs):
    page = re.search(r'/game/([^.]*(?=\?))')
    print('Submitted page is: ',page.group(1).rstrip())
