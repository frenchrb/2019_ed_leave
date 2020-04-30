from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

# print(repo)

repo_name = repo.name
print('Repository Name: ' + repo_name)
print()

collection = repo.resources(66)
# print(collection)
print(collection.title)
print(collection.ead_id)
print(collection.id_0)
print(type(collection.id_0))
print(collection.extents)
print(type(collection.extents))
print(collection.extents[0])
print(collection.extents[0].number) # this is the quantity (number of linear ft.)
print()

# Lists all attributes of collection (title, ead_id, etc.)
# print(dir(collection))

# print(collection.json())
# print(type(collection))
# print(type(collection.title))

data = collection.json()
print(type(data))
print(data['title'])
data['description'] = 'here\'s some info'
print(data['description'])

print(data['extents'][0])