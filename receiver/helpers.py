import re

def pagepicker(url_):
    #page = re.search(r'game\/([^.]*(?!\?))', url_, re.M)
    page = re.search(r'wol\/(\w*)\/([\D]*)\/?\?mb', url_, re.M)
    if page.group(1).rstrip() == 'kingdom_forum':
        pass
    else:
        return page.group(1).rstrip()

def kddetailsparser(data):
    keys = ('id','name','race','acres','networth','nwpa','title')
    allprovs = []
    nr_of_provs = re.search(r'Total Provinces\s*(\d+)', data, re.M)
    online_provs = re.search(r'\s{2}(\S*)\*', data, re.M)
    print('Number of provinces: ', nr_of_provs.group(1).rstrip())
    print('Online provinces: ', online_provs.group(1).rstrip())
    prov_list_raw = re.search(r'Nobility([^.]*(?!\?))', data, re.M)
    for line in prov_list_raw.group(1).splitlines()[1:]:
        '''This regular expression filters out each line of the KD page into the columns'''
        temp = re.search(r'(\d+)\s{2}(.*)\s{2}(\S*)\s{2}(\S*\sacres)\s{2}(\S*gc)\s{2}(\S*gc)\s{2}(\S*)', line, re.M)
        if temp is None:
            pass
        else:
            oneprov = {}
            oneprov['id'] = temp.group(1)
            oneprov['name'] = temp.group(2)
            oneprov['race'] = temp.group(3)
            oneprov['acres'] = temp.group(4)
            oneprov['networth'] = temp.group(5)
            oneprov['nwpa'] = temp.group(6)
            oneprov['title'] = temp.group(7)
            allprovs.append(oneprov)
    print(allprovs)

    return nr_of_provs.group(1).rstrip()

if __name__ == '__main__':
    pagepicker()
