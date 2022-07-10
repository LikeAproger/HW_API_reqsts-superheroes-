import requests

TOKEN = '100586072728312'
HEROES = ['Hulk', 'Thanos', 'Captain America']
MASK = f'https://www.superheroapi.com/api.php/{TOKEN}/search'


def make_urls(mask, heroes):  
    urls = ((f'{mask}/{hero}') for hero in heroes)
    return urls


def get_requests(urls):    
    reqs = (requests.get(url) for url in urls)
    return reqs


def parser():
    finded_heroes = []
    urls = make_urls(MASK, HEROES)    
    reqsts = get_requests(urls)
    for req in reqsts:
        req_reslt = req.json()
        try:
            for hero in req_reslt['results']:
                if hero['name'] in HEROES:
                    finded_heroes.append({
                        'name': hero['name'],
                        'intelligence': hero['powerstats']['intelligence'],
                    })
        except KeyError:
            print(f"Check URLs: {urls}")
    max_intelligence = 0
    name_max_intelligence = ''
    for hero in finded_heroes:
        if max_intelligence < int(hero['intelligence']):
            max_intelligence = int(hero['intelligence'])
            name_max_intelligence = hero['name']

    print(f"The most intelligence is {name_max_intelligence}, his intelligence is: {max_intelligence}")


parser()