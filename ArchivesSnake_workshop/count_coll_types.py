from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

papers = 0
records = 0
scrapbooks = 0
diaries = 0
ledgers = 0
letters = 0
photos = 0
collection_count = 0
other = 0
for collection in repo.resources:
    if 'papers' in collection.title.lower():
        papers += 1
    elif 'records' in collection.title.lower():
        records += 1
    elif 'scrapbook' in collection.title.lower():
        scrapbooks += 1
    elif 'diar' in collection.title.lower():
        diaries += 1
    elif 'ledger' in collection.title.lower():
        ledgers += 1
    elif 'letter' in collection.title.lower():
        letters += 1
    elif 'photo' in collection.title.lower():
        photos += 1
    elif 'collection' in collection.title.lower():
        collection_count += 1
    else:
        other += 1
        print(collection.title)
print()
print(str(papers) + ' papers')
print(str(records) + ' records')
print(str(scrapbooks) + ' scrapbooks')
print(str(diaries) + ' diaries')
print(str(ledgers) + ' ledgers')
print(str(letters) + ' letters')
print(str(photos) + ' photograph collections')
print(str(collection_count) + ' collections')
print(str(other) + ' other')

print(papers + records + scrapbooks + diaries + ledgers + letters + photos + collection_count + other)