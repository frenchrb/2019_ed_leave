from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

# 59, 72
# collection = repo.resources(74)

for collection in repo.resources:
    lang_count = 0
    lang_list = []
    dup_count = 0
    und_flag = False
    print('====================')
    print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
    print('finding_aid_language: ' + collection.finding_aid_language)
    
    for lang in collection.lang_materials:
        # print(dir(lang))
        lang_count += 1
        print('Lang #' + str(lang_count))
        # print(lang)
        
        try:
            if hasattr(lang, 'language_and_script'):
                content = lang.language_and_script.language
                print('Type: language_and_script\t' + content)
                if 'und' in content:
                    und_flag = True
        except KeyError as e:
            pass
        try:
            if hasattr(lang, 'notes'):
                notes = lang.notes
                for n in notes:
                    if len(n.content) == 1:
                        content = n.content[0]
                        print('Type: notes\t\t\t\t\t' + content)
                    else:
                        print('Type: notes\t[list not printed]')
        except KeyError as e:
            pass
        
        if content in lang_list:
            dup_count += 1
            print('Language "' + content + '" is a duplicate. Please delete.')
        else:
            lang_list.append(content)
    
    print()
    print('There are currently ' + str(lang_count) + ' languages. ' + str(dup_count) + ' duplicate(s) should be deleted.')
    print('Desired languages with duplicates removed: ')
    print(lang_list)
    
    if und_flag:
        print('One or more languages is "und" and should be removed.')
    
    # print(str(lang_count))
    print()

'''
count total number of language things (as in check_language.py)
for each lang
    is it language_and_script or a note?
    what is the language/note content?
which ones are und?
which ones are dups?
'''