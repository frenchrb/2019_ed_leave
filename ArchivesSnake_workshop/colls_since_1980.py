from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

newer = False

'''
for collection in repo.resources:
    print('----------------------------------------')
    print(collection.id_0 + '\t\t' + collection.title)
    
    for date in collection.dates:
        print(date.expression)
        print(dir(date))
        beginDate = date.begin
        endDate = date.end
        print('\t' + beginDate)
        print('\t' + endDate)  
    print('----------------------------------------')
'''

for collection in repo.resources:
    print(collection.id_0 + '\t\t' + collection.title + '\t' + collection.uri)
    # print(collection.finding_aid_language)
    for date in collection.dates:
        print('\t' + date.expression + '\t' + date.date_type)
        # print(dir(date))
        if 'single' in date.date_type:
            year = date.begin
        elif 'inclusive' in date.date_type:
            year = date.end.split('-')[0]
        print('Latest Year: ' + year)
        # if int(year) > 1980:
            # newer = True
            # print('\t' + 'yes')
    print()