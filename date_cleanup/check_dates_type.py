import re
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

for collection in repo.resources:
    print('====================')
    print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
    for date in collection.dates:
        date_type = ''
        date_expression = ''
        date_begin = ''
        date_end = ''
        messages = []
        
        try:
            date_type = date.date_type
            date_expression = date.expression
            date_begin = date.begin
            date_end = date.end
        except KeyError as e:
            print(e)
        
        if re.match(r'^\d{4}$', date_expression) and date_type != 'single':
            messages.append('single date expression without single date type')
        if re.match(r'^\d{4}-\d{4}$', date_expression) and date_type =='single':
            messages.append('range of dates with single date type')
        
        if date_type == 'single':
            if not date_begin:
                messages.append('normalized begin date missing')
            else:
                if date_begin != date_expression:
                    messages.append('normalized dates might not match expression')
        elif date_type == 'inclusive' or date_type == 'bulk':
            if not date_begin:
                messages.append('normalized begin date missing')
            if not date_end:
                messages.append('normalized end date missing')
            if date_begin and date_end:
                norm_string = ''
                if date_type == 'bulk':
                    norm_string += 'bulk '
                norm_string += date_begin
                if date_end:
                    norm_string += '-' + date_end
                if norm_string != date_expression:
                    messages.append('normalized dates might not match expression')
        
        print(date_expression + '\t' + date_type + '\t' + date_begin + '\t' + date_end + '\t' + ';'.join(messages))
    print()
