from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

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

print('Call Number\tTitle\tURI\t# of Languages')
for collection in repo.resources:
    lang_count = 0
    for lang in collection.lang_materials:
        # print(dir(lang))
        lang_count += 1
        # print('Lang #' + str(lang_count))
    if lang_count > 1:
        print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri + '\t' + str(lang_count))
        
        # print('finding_aid_language: ' + collection.finding_aid_language)
        # print('lang_materials: ')
        '''
        print(dir(lang))
        try:
            if hasattr(lang, 'language_and_script'):
                print('\tHas language_and_script')
        except KeyError as e:
            pass
        try:
            if hasattr(lang, 'notes'):
                print('\tHas notes')
        except KeyError as e:
            pass
        '''
        
    # for date in collection.dates:
        # print('\t' + date.expression + '\t' + date.date_type)
        # # print(dir(date))
        # if 'single' in date.date_type:
            # year = date.begin
        # elif 'inclusive' in date.date_type:
            # year = date.end.split('-')[0]
        # print('Latest Year: ' + year)
        # # if int(year) > 1980:
            # # newer = True
            # # print('\t' + 'yes')
    # print()