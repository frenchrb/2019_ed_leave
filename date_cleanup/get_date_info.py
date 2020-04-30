from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

collection = repo.resources(6)
print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
for date in collection.dates:
    print(date)
    