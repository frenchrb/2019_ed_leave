import re
from asnake.aspace import ASpace

aspace = ASpace()
repo = aspace.repositories(2)

for collection in repo.resources:
# collection = repo.resources(66)
    for date in collection.dates:
        date_era = ''
        date_calendar = ''
        missing = []
        
        try:
            date_era = date.era
        except KeyError as e:
            missing.append('era')
        try:
            date_calendar = date.calendar
        except KeyError as e:
            missing.append('calendar')
        
        if missing:
            print(collection.id_0 + '\t' + collection.title + '\t' + collection.uri)
            print('\tMissing: ' + ','.join(missing))
            print()
