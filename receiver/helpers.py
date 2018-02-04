import re
import argparse

personalities = {
'Sage':'The Wise',
'Mystic':["the Sorcerer","the Sorceress"],
'Tactician':"The Conniving",
'Warrior':"the Warrior",
'Rogue':"the Rogue",
'War Hero':"the Hero",
'Paladin':"the Chivalrous",
'Heretic':"the Skeptic",
'Undead':"the Undying"
}
titles = [
'Knight','Lady',
'Lord','Noble Lady',
'Baron','Baroness',
'Viscount','Viscountess',
'Count','Countess',
'Marquis','Marchioness',
'Duke','Duchess',
'Prince','Princess',
'King','Queen'
]

def pagepicker(url_):
    page = re.search(r'wol\/(\w*)\/([\w]*)', url_, re.M)
    if (page.group(1).rstrip() == 'kingdom_forum') or (page.group(1).rstrip() == 'mail'):
        pass
    else:
        urlelements = []
        for i in re.finditer(r'\/(\w*)', url_):
            if i.group(0)[1:] != '':
                urlelements.append(i.group(0)[1:])
        del urlelements[0:3]
        #print(urlelements[0])
    return urlelements[0]


def personalityfinder(data):
    for pers,title in personalities.items():
        #print(pers,title)
        if type(title) != list:
            playerpers = re.search(title, data)
            if playerpers != None:
                personality=playerpers
            #print(bar)
        else:
             for x in title:
                 playerpers = re.search(x, data)
                 if playerpers != None:
                     personality=playerpers
                 #print(bar)
    print(personality)

def titlefinder(data):
    #print(data)
    for option in titles:
        #print(option)
        playertit = re.search(option, data)
        if playertit and playertit.group(0) in titles:
            #print('Heeeeeeeey',playertit)
            title = playertit.group(0)
            if playertit.group(0) == 'Lady':
                if re.search('Noble', data):
                    title = "Noble Lady"
            return title
    if playertit == None:
        title = 'Peasant'
        return title


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
    parser = argparse.ArgumentParser(description="the URL the script would normally receive from views.py")
    parser.add_argument('teststring', type=str)
    args = parser.parse_args()
    #pagepicker(args.teststring)
    #personalityfinder(args.teststring)
    title = titlefinder(args.teststring)
    print(title)
