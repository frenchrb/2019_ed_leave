These scripts represent experiments in using the ArchivesSpace API and ArchivesSnake. Use at your own risk! Various things may be hardcoded, like repository number and resource ID.

For scripts using ArchivesSnake, see [https://github.com/archivesspace-labs/ArchivesSnake/wiki/Getting-Started-Guide](https://github.com/archivesspace-labs/ArchivesSnake/wiki/Getting-Started-Guide) for ArchivesSnake setup.

Scripts using configparser require a config file (config.ini) in the same directory. Example of config.ini:
```
[ArchivesSpace]
baseURL:http://localhost:8089
repository:2
user:user
password:pw
```

Scripts using secrets require secrets.py file.
```
baseURL='http://localhost:8089'
user='user'
password='pw'
```

