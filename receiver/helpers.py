import re

def pagepicker(url_):
    page = re.search(r'game\/([^.]*(?!\?))', url_, re.M)
    return page.group(1).rstrip()

def kddetailsparser(data):
    keys = ('id','name','race','acres','networth','nwpa','title')
    allprovs = []
    nr_of_provs = re.search(r'Total Provinces\s*(\d+)', data, re.M)
    print('Number of provinces: ', nr_of_provs.group(1).rstrip())
    prov_list_raw = re.search(r'Nobility([^.]*(?!\?))', data, re.M)
    for line in prov_list_raw.group(1).splitlines()[1:3]:
        '''This regular expression filters out each line of the KD page into the columns'''
        temp = re.search(r'(\d)\s*(\S*\s?\S*)\s{2}(\S*)\s{2}(\S*\sacres)\s{2}(\S*gc)\s{2}(\S*gc)\s{2}(\S*)', line, re.M)
        oneprov = {}
        oneprov['id'] = temp.group(1)
        oneprov['name'] = temp.group(2)
        oneprov['race'] = temp.group(3)
        print(oneprov)
        print(allprovs)
        oneprov['acres'] = temp.group(4)
        oneprov['networth'] = temp.group(5)
        oneprov['nwpa'] = temp.group(6)
        oneprov['title'] = temp.group(7)
        print(oneprov)
        #allprovs.append(oneprov)
        #oneprov = ()
        #for i in range(1,8):
        #    oneprov = oneprov + (temp.group(i),)
        #allprovs.append([dict(zip(keys, elems)) for elems in oneprov])
    print(allprovs)

    return nr_of_provs.group(1).rstrip()

if __name__ == '__main__':
    pagepicker()
