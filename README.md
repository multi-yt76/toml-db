# toml-db

Toml-DB is an attempt at a No-SQL DB, which works similar to tiny-db, but uses Toml for storing data. 

Note: (This is a simple package, a work in progress as well as my first Python Package.. also there are no docs yet.)

## Installation:

Installation is done through git:

```py
python -m pip install -U git+https://github.com/multi-yt76/toml-db
```

## Introduction:

To get started, you need to create on object of the TomlDB class, with the .toml file as the argument

```py
from tomldb import TomlDB

db = TomlDB('db.toml')
```

For now, the functions available are:

- `db.insert()`
- `db.get()`
- `db.update()`
- `db.add()`
- `db.subtract()`
- `db.delete()`

### Insert is used to create a new document

```py
db.insert({"id": 1, "name": "Test", "age": 20})
```

### Get is used to retrieve data

```py
db.get()

#Gets the whole db in JSON Format
```

```py
db.get("id", 1)

#Returns: {"id": 1, "name": "Test", "age": 20}
```

### Update is used to add a new field or update an existing field in a doc

```py
db.update({"age": 25}, "id", 1)

#Age is now 25
```

### Add and Subtract are used to add and subtract certain values to or from the values of a field

```py
db.add({"age": 5}, "id", 1)
#Age is now 30

db.subtract({"age": 10}, "id", 1)
#Age is now 20
```

### Delete is used to delete a doc or the entire DB

```py
db.delete()

#Deletes the whole DB
```

```py
db.delete("id", 1)

#Deletes this "{"id": 1, "name": "Test", "age": 20}" doc
```
