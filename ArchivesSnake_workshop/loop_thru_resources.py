from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

count = 0
for collection in repo.resources:
    count += 1
    print(collection.id_0 + '\t' + collection.title)
print(count)