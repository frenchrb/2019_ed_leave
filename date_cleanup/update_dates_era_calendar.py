import os
from asnake.aspace import ASpace
from asnake.client import ASnakeClient

client = ASnakeClient()
client.authorize()

aspace = ASpace()
repo = aspace.repositories(2)

input = 'dates_missing_era_calendar_to_change_20191104.txt'
# input = 'dates_missing_era_calendar_test.txt'
file = open(input, 'r')

for coll_num in file:
    collection = repo.resources(coll_num)
    print('====================')
    print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
    collectJson = collection.json()
    
    update = False
    for date in collectJson['dates']:
        print(date)
        print()
        
        try:
            if date['era'] != 'ce':
                print('era is incorrect; will be updated to ce')
                date['era'] = 'ce'
                update = True
        except KeyError:
            print('era is missing; will be updated to ce')
            date['era'] = 'ce'
            update = True
        
        try:
            if date['calendar'] != 'gregorian':
                print('calendar is incorrect; will be updated to gregorian')
                date['calendar'] = 'gregorian'
                update = True
        except KeyError:
            print('calendar is missing; will be updated to gregorian')
            date['calendar'] = 'gregorian'
            update = True
        
        print()
        # print(date)
        # print()
    
    if update:
        update = client.post(collectJson['uri'], json=collectJson)
        print(update.status_code)
    
        collection = repo.resources(coll_num)
        for date in collection.dates:
            print(date)
        print()
    else:
        print('no changes needed')
        print()
