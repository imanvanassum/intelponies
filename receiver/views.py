from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.files import File
import json, re
from receiver.helpers import pagepicker, kddetailsparser, personalityfinder
from receiver.models import Race, Province


units = {
'Human': {'ospec': 'Swordsmen', 'dspec': 'Archers', 'elites': 'Knights'}
}
kingdoms = {
1: {'kingdom': 6,'island': 8}
}

class HomeView(View):

    def get(self, request, *args, **kwargs):
        #return HttpResponse('<html><head><title>Utopia Ponies</title></head><body><h1>WORKING ON IT!</h1></body></html>')
        return render(request, 'receiver/index.html')


class UpoView(View):

    def get(self, request, *args, **kwargs):
        #return HttpResponse('<html><head><title>Utopia Ponies</title></head><body><h1>WORKING ON IT!</h1></body></html>')
        return render(request, 'receiver/upoguide.html')


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

        data = dict_['data_simple']
        current_page = pagepicker(dict_['url'])
        print('Pagepicker returned:', current_page)

        if current_page == 'throne':
            find_provname = re.search(r'The Province of\s?([^.]*(?=\(([0-9])\:([0-9])))',data, re.M)
            provname = find_provname.group(1).rstrip()
            kingdom = find_provname.group(2).rstrip()
            island = find_provname.group(3).rstrip()
            if provname == dict_['prov']:
                selfintel = True
            find_race = re.search(r'Race\s+([^.]*(?=Soldiers))',data, re.M)
            race = find_race.group(1)
            find_ruler = re.search(r'Ruler\s*(.*){}'.format(units[race]['ospec']),data, re.M)
            ruler = find_ruler.group(0)
            personality = personalityfinder(ruler)
            print('Race: ',race)
            print('Province name: ',provname)
            print('Is your own? ', selfintel)

        else:
            pass

        if current_page == 'kingdom_details':
            kdpage = kddetailsparser(data)
            print('In views.py :',kdpage)

        with open('test.txt', 'a') as f:
            myfile = File(f)
            myfile.write('----------------------- START OF PAGE ---------------------------' + '\n')
            myfile.write(dict_['url'] + '\n')
            myfile.write(dict_['data_simple'])
            myfile.write('----------------------- END OF PAGE ---------------------------' + '\n')

        # name,ruler,race,personality,kingdom
        Province.objects.create(provname,ruler,race,)


        reply = {
            'success': True,
        }
        fuckmunk = json.JSONEncoder().encode(reply)
        return HttpResponse(fuckmunk)
