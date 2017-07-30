from django.views import View
from django.http import HttpResponse
import json, re
from receiver.helpers import pagepicker, kddetailsparser


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<html><head><title>Utopia Ponies</title></head><body><h1>WORKING ON IT!</h1></body></html>')


class IntelView(View):

    """
    The game sends the following information:
    [url] = The page in the game, for instance /throne
    [data_html] = Raw HTML content of the page, not used
    [data_simple] = Cleaned version of the page data
    [key] = A user-picked key to make sure we don't allow intel from non-Ponies
    [prov] = The province of the user sending the data
    """

    def post(self, request, *args, **kwargs):
        selfintel = False
        find_provname = ''
        dict_ = request.POST.dict()

        #print(dict_['url'])
        #print(type(dict_['url']))
        #print()
        data = dict_['data_simple']
        current_page = pagepicker(dict_['url'])
        print('Pagepicker returned:', current_page)

        if current_page == 'throne':
            find_provname = re.search(r'The Province of\s?([^.]*(?=\([0-9]))',data, re.M)
            province = find_provname.group(1).rstrip()
            if province == dict_['prov']:
                selfintel = True
            find_race = re.search(r'Race\s+([^.]*(?=Soldiers))',data, re.M)
            race = find_race.group(1)
            print('Race: ',race)
            print('Province name: ',province)
            print('Is your own? ', selfintel)
        else:
            pass

        if current_page == 'kingdom_details':
            kdpage = kddetailsparser(data)
            print('In views.py :',kdpage)


        reply = {
            'success': True,
        }
        i_hate_javascript = json.JSONEncoder().encode(reply)
        return HttpResponse(i_hate_javascript)
