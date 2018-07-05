#! /usr/bin/env python
#coding: utf-8

import json, requests


city_list = ['стаханов','умань','бердичев','шостка','бровары','измаил','артёмовск','мукачево','ялта','дрогобыч','нежин','феодосия','свердловск','новомосковск','торез','червоноград','первомайск','смела','красноармейск','калуш','коростень','ковель','рубежное','прилуки','дружковка','харцызск','лозовая','антрацит','стрый','коломыя','шахтёрск','снежное','новоград-волынский','энергодар','изюм','димитров','брянка','чёрноморск','борисполь','нововолынск','ровеньки','жолтые воды','лубны','новая каховка','фастов','белгород-днестровский','комсомольск','краснодон','ромны','ахтырка','светловодск','марганец','шепетовка','орджоникидзе','дзержинск',
'джанкой','первомайск','миргород','вознесенск','котовск','ирпень','васильков','дубно','ингулец  2','кузнецовск','владимир-волынский','каховка','южноукраинск','борислав','ясиноватая','жмеринка','авдеевка','чугуев','самбор','токмак','боярка','глухов','доброполье','староконстантинов','кировск','вишнёвое','нетешин','славута','могилёв-подольский','обухов','первомайский','купянск','балаклия','синельниково','переяслав-хмельницкий','алушта','трускавец','красноперекопск',
]

new_city_list = []
url = "https://ws3.morpher.ru/russian/declension"
#print (city_list [504])

for i in range(len(city_list)):
    s = city_list[i]

    params = dict (
        s=str(s),
        format="json",
        #token= #Не обязателен. Подробнее: http://morpher.ru/ws3/#authentication
        )

    response = requests.get(url=url, params=params)
    data = json.loads(response.text)
    new_city_list.extend([
        data.get('Р'),
        data.get('Д'),
        data.get('В'),
        data.get('Т'),
        data.get('П'),
    ])

print(new_city_list)
