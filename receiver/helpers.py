import re

def pagepicker(self, url_, *args, **kwargs):
    page = re.search(r'/game/([^.]*(?=\?))', url_, re.M)
    print('Submitted page is: ',page.group(1).rstrip())
