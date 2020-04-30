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
        
        try:
            date_type = date.date_type
            date_expression = date.expression
            date_begin = date.begin
            date_end = date.end
            messages = []
            
            norm_string = ''
            if 'bulk' in date_type:
                norm_string += 'bulk '
            norm_string += date_begin
            if date_end:
                norm_string += '-' + date_end
            
            if re.match(r'^\d{4}$', date_expression) and 'single' not in date_type:
                messages.append('single date expression without single date type')
            if re.match(r'^\d{4}-\d{4}$', date_expression) and 'single' in date_type:
                messages.append('range of dates with single date type')
            # if 'single' in date.date_type and '-' in date_expression:
                    # messages.append('single date type doesn\'t match expression')
            # if 'inclusive' in date.date_type and '-' not in date_expression:
                    # messages.append('inclusive date type doesn\'t match expression')
            if norm_string not in date_expression:
                messages.append('normalized dates might not match expression')
        except KeyError as e:
            print(e)
            # continue
        
        print(date_expression + '\t' + date_type + '\t' + date_begin + '\t' + date_end + '\t' + ';'.join(messages))
    print()
