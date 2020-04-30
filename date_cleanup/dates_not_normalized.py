import re
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

for collection in repo.resources:
# collection = repo.resources(66)
    for date in collection.dates:
        date_type = ''
        date_expression = ''
        date_begin = ''
        date_end = ''
        missing = []
        
        try:
            date_type = date.date_type
            date_expression = date.expression
        except:
            pass
        try:
            date_begin = date.begin
        except KeyError:
            missing.append('begin')
        try:
            date_end = date.end
        except KeyError:
            if date_type != 'single':
                missing.append('end')
        
        if missing:
            print('====================')
            print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
            print(date_expression + '\t' + date_type + '\t' + date_begin + '\t' + date_end)
            # print('\tMissing: ' + ','.join(missing))
            
            if 'begin' in missing:
                if date_type == 'single':
                    if re.match(r'^\d{4}$', date_expression):
                        date_begin = re.sub(r'^(\d{4})$', r'\g<1>', date_expression)
                        print('Missing begin; new begin: ' + date_begin)
                    else:
                        print('Missing begin; evaluate manually')
                else:
                
                    if re.match(r'(\d{4})\-(\d{4})', date_expression):
                        date_begin = re.sub(r'(\d{4})\-(\d{4})', r'\g<1>', date_expression)
                        print('Missing begin; new begin: ' + date_begin)
                    else:
                        print('Missing begin; evaluate manually')
                
            if 'end' in missing and date_type != 'single':
                if re.match(r'(\d{4})\-(\d{4})', date_expression):
                    date_end = re.sub(r'(\d{4})\-(\d{4})', r'\g<2>', date_expression)
                    print('Missing end; new end: ' + date_end)
                else:
                    print('Missing end; evaluate manually')
                
            print()
