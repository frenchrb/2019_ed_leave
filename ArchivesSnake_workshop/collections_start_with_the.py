from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

count = 0
for collection in repo.resources:
    if collection.title.lower().strip().startswith('the'):
        count += 1
        print(collection.title)
print(count)
