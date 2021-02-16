# Toml-DB

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

#### Update 1.1a has added in some more new functions. The new list of functions is given below:

- `db.insert()`
- `db.get()`
- `db.update()`
- `db.add()`
- `db.subtract()`
- `db.delete()`

- `db.search()`
- `db.insert_multiple()`
- `db.contains()`
- `db.count()`
- `db.all()`

#### Queries have also been added, their implementation is given at the [end](https://github.com/multi-yt76/toml-db/blob/main/README.md#the-queries-make-the-syntax-easier-to-follow-and-add-a-few-more-features).

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
```

The `add()` and `sub()` functions can now be used within `db.update()` to add or subtract values. However, the `db.add()` and `db.subtract()` functions can still be used, although they are not recommended

```py
from tomldb.operations import add, sub

db.update(add("age", 5), "id", 1)
#Age is now 30

db.update(sub("age", 10), "id", 1)
#Age is now 20
```

### Add and Subtract are used to add and subtract certain values to or from the values of a field

```py
db.add({"age": 5}, "id", 1)
#Age is now 25

db.subtract({"age": 10}, "id", 1)
#Age is now 15
```

### Delete is used to delete a doc or the entire DB

```py
db.delete()

#Deletes the whole DB
```

```py
db.delete("id", 1)

#Deletes this "{"id": 1, "name": "Test", "age": 15}" doc
```

### The Queries make the syntax easier to follow and add a few more features.

```py
from tomldb import TomlDB, Query

db = TomlDB('db.toml')
User = Query()

db.insert({"id": 1, "name": "Test", "age": 20})

db.get(User.id == 1) """ It can be also written as: db.get(User["id"] == 1) """

#Returns: {"id": 1, "name": "Test", "age": 20}
```

### Insert_Multiple is used to insert multiple dicts from a list

### Search is used to get matching data in a list

```py
db.insert_multiple([{"id": 1, "name": "Test1", "age": 20}, {"id": 2, "name": "Test2", "age": 35}, {"id": 3, "name": "Test3", "age": 12}])

db.search(User.age > 12) """ Operators other than == can also be used with Queries """

#Returns: [{"id": 1, "name": "Test1", "age": 20}, {"id": 2, "name": "Test2", "age": 35}]
```

### Contains checks if a key:value pair is present in a db, and returns the bool response

```py
db.contains(User.id == 4)

#Returns: False
```
### Count gets the number of matching dicts 

```py
db.count(User.id == 1)

#Returns: 1
```

### All gets all the dicts in a list

```py
db.all()

#Returns: [{"id": 1, "name": "Test1", "age": 20}, {"id": 2, "name": "Test2", "age": 35}, {"id": 3, "name": "Test3", "age": 12}]
```

