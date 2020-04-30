import re
from asnake.aspace import ASpace
from asnake.client import ASnakeClient

client = ASnakeClient()
client.authorize()

aspace = ASpace()
repo = aspace.repositories(2)

collection = repo.resources(189)
for date in collection.dates:
    date_type = ''
    date_expression = ''
    date_begin = ''
    date_end = ''
    
    try:
        date_type = date.date_type
        date_expression = date.expression
        date_begin = date.begin
        date_end = date.end
    except KeyError:
        pass
    
    if re.match(r'^\d{4}$', date_expression) and date_type == 'inclusive':
        print('====================')
        print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
        print(date_expression + '\t' + date_type + '\t' + date_begin + '\t' + date_end)
        # print('single date expression without single date type')
        
        update = False
        collectJson = collection.json()
        for date in collectJson['dates']:
            if re.match(r'^\d{4}$', date['expression']) and date['date_type'] == 'inclusive':
                # print(date)
                print()
                
                # Change date type to single
                try:
                    if date['date_type'] != 'single':
                        print('date_type is incorrect; will be updated to single')
                        date['date_type'] = 'single'
                        update = True
                except KeyError:
                    print('date_type is missing')
                
                
                # Change normalized begin date
                '''
                try:
                    if date['expression'] != date['begin']:
                        print('expression doesn\'t match normalized begin date; normalized date will be updated')
                        date['begin'] = date['expression']
                        update = True
                except KeyError:
                    print('expression or begin is missing')
                '''
                
                # Remove normalized end date
                try:
                    if date['end']:
                        print('normalized end date exists; will be removed')
                        date.pop('end')
                        update = True
                except KeyError:
                    print('no normalized end date')
                
                print()
                print('Dates will be updated to:')
                print(date)
                print()
        
        if update:
            update = client.post(collectJson['uri'], json=collectJson)
            print(update.status_code)
            
            # Print all dates
            num = collectJson['uri'].replace('/repositories/2/resources/', '')
            collection = repo.resources(num)
            for date in collection.dates:
                date_type = ''
                date_expression = ''
                date_begin = ''
                date_end = ''
                
                try:
                    date_type = date.date_type
                    date_expression = date.expression
                    date_begin = date.begin
                    date_end = date.end
                except KeyError:
                    pass
                
                print(date_expression + '\t' + date_type + '\t' + date_begin + '\t' + date_end)
            
            print()
