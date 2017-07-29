from django.views import View
from django.http import HttpResponse
import json, logging

logger = logging.getLogger(__name__)


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<html><head><title>Utopia Ponies</title></head><body><h1>WORKING ON IT!</h1></body></html>')


class IntelView(View):

    def post(self, request, *args, **kwargs):
        #print(request.POST.get('data_simple'))
        #print(request.POST)
        with open('test.txt','a+') as f:
            #for line in request.POST:
            #    f.write(json.dumps(line) + '\n')
            str_ = json.dumps(request.POST.get('data_simple'),
                    indent=4, sort_keys=True,separators=(',', ': '),
                    ensure_ascii=False)
            f.write(str_)
            f.write('\n')
        reply = {
            'success': True,
        }
        i_hate_javascript = json.JSONEncoder().encode(reply)
        return HttpResponse(i_hate_javascript)
