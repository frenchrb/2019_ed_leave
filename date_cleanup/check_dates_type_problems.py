import re
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

collection = repo.resources(6)
print('====================')
print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
for date in collection.dates:
    date_type = ''
    date_expression = ''
    date_begin = ''
    date_end = ''
    messages = []
    
    print('date_type: ' + date_type)
    print('date_expression: ' + date_expression)
    print('date_begin: ' + date_begin)
    print('date_end: ' + date_end)
    print('messages: ')
    for m in messages:
        print(m)
    print()
    
    
    try:
        date_type = date.date_type
        date_expression = date.expression
        date_begin = date.begin
        date_end = date.end
    except KeyError as e:
        print(e)
        # continue    
    print('date_type: ' + date_type)
    print('date_expression: ' + date_expression)
    print('date_begin: ' + date_begin)
    print('date_end: ' + date_end)
    print('messages: ')
    for m in messages:
        print(m)
    print()
    
    norm_string = ''
    if 'bulk' in date_type:
        norm_string += 'bulk '
    norm_string += date_begin
    if date_end:
        norm_string += '-' + date_end
    
    if re.match(r'^\d{4}$', date_expression) and date_type != 'single':
        messages.append('single date expression without single date type')
    if re.match(r'^\d{4}-\d{4}$', date_expression) and date_type =='single':
        messages.append('range of dates with single date type')
    # if 'single' in date.date_type and '-' in date_expression:
            # messages.append('single date type doesn\'t match expression')
    # if 'inclusive' in date.date_type and '-' not in date_expression:
            # messages.append('inclusive date type doesn\'t match expression')
    if norm_string not in date_expression:
            messages.append('normalized dates might not match expression')
    
    
    print(date_expression + '\t' + date_type + '\t' + date_begin + '\t' + date_end + '\t' + ';'.join(messages))
print()


'''
for collection in repo.resources:
# collection = repo.resources(66)
    for date in collection.dates:
        date_era = ''
        date_calendar = ''
        missing = []
        
        try:
            date_era = date.era
        except KeyError as e:
            missing.append('era')
        try:
            date_calendar = date.calendar
        except KeyError as e:
            missing.append('calendar')
        
        if missing:
            print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
            print('\tMissing: ' + ','.join(missing))
            print()
'''