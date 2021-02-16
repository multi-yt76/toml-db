import toml
import ast
from typing import Any, MutableMapping, Union

class Query:
  def __init__(self):
    self._path = ()

  def __repr__(self):
    return '{}()'.format(type(self).__name__)

  def __getattr__(self, item: str):
    query = type(self)()
    query._path = self._path + (item,)

    return query

  def __getitem__(self, item: str):
    return self.__getattr__(item)


  def __eq__(self, rhs: Any):
       if isinstance(rhs, str) or isinstance(rhs, int):
         return self._path[0], rhs, "=="

  def __ne__(self, rhs: Any):
       if isinstance(rhs, str) or isinstance(rhs, int):
         return self._path[0], rhs, "!="

  def __lt__(self, rhs: Any):
       if isinstance(rhs, str) or isinstance(rhs, int):
         return self._path[0], rhs, ">"

  def __le__(self, rhs: Any):
       if isinstance(rhs, str) or isinstance(rhs, int):
         return self._path[0], rhs, "<="

  def __gt__(self, rhs: Any):
       if isinstance(rhs, str) or isinstance(rhs, int):
         return self._path[0], rhs, "<"

  def __ge__(self, rhs: Any):
       if isinstance(rhs, str) or isinstance(rhs, int):
         return self._path[0], rhs, ">="

class TomlDB:

  def __init__(self, db) -> None:
    self.db = db
    self.cur = 0
    self.i = 1
    self.json = {}

  def __iter__(self) -> Any:
    return self

  def __next__(self) -> Any:
    self.cur += 1

    if self.cur < len(self.get()['_default'].keys()) + 1:
      return self.get()['_default'][str(self.cur)]
    raise StopIteration
 
  def insert(self, var) -> None:
   if type(var) == dict:
    self.json = var

    with open(self.db, "a+", newline = "\n") as db2:

      self.i = len(toml.load(self.db)['_default']) + 1 if bool(toml.load(self.db)) == True else 1
      db2.write(toml.dumps({"_default": {f"{self.i}": self.json}}) + "\n")

   else:
     raise TypeError("Value specified for the insert function was not a dict")

  def insert_multiple(self, var) -> None:
    for i in var:
      self.insert(i)

  def update(self, var, k, v) -> None:
    if type(var) == dict:

      arr = self.get()

      key_list = list(self.get()["_default"].keys())
      val_list = list(self.get()["_default"].values())

      position = val_list.index(self.get(k, v))

      arrr = self.get()["_default"][key_list[position]]

      arrr.update({list(var.keys())[0]: list(var.values())[0]})

      arr["_default"][key_list[val_list.index(arr["_default"][key_list[position]])]] = arrr

      with open(self.db, "w+", newline = "\n") as db2:
        db2.write(toml.dumps(arr))

    else:
     if type(var) == str and type(ast.literal_eval(var[3:])) == dict:

       if var[0:3] == "add":
        self.add(ast.literal_eval(var[3:]), k, int(v))

       elif var[0:3] == "sub":
        self.subtract(ast.literal_eval(var[3:]), k, int(v))

     else:
       raise TypeError("Value specified for the update function was not a dict")
 
  def add(self, var, k, v) -> None:
    if type(var) == dict:
     if type(list(var.values())[0]) == int:

      key_list = list(self.get()["_default"].keys())
      val_list = list(self.get()["_default"].values())

      position = val_list.index(self.get(k, v))

      arrr = self.get()["_default"][key_list[position]][list(var.keys())[0]]

      self.update({list(var.keys())[0]: arrr + list(var.values())[0]}, k, v)
     
     else:
       raise TypeError("Value specified in the dict for the add function was not an int")

    else:
      raise TypeError("Value specified for the add function was not a dict")

  def subtract(self, var, k, v) -> None:
    if type(var) == dict:
     if type(list(var.values())[0]) == int:

      key_list = list(self.get()["_default"].keys())
      val_list = list(self.get()["_default"].values())

      position = val_list.index(self.get(k, v))

      arrr = self.get()["_default"][key_list[position]][list(var.keys())[0]]

      self.update({list(var.keys())[0]: arrr - list(var.values())[0]}, k, v)

     else:
       raise TypeError("Value specified in the dict for the subtract function was not an int")

    else:
      raise TypeError("Value specified for the subtract function was not a dict")
  
  def get(self, k = None, v = None, e = "==") -> Union[MutableMapping, Any, dict, None]:
   if not k and not v:
     return toml.load(self.db)

   else:
    if type(k) == tuple:
      k, v, e = k

    t = False
    arr = toml.load(self.db)

    if bool(arr) == True:

     for i in arr["_default"]:
      if k in arr["_default"][i] and eval(str(v) + e + str(arr["_default"][i][k])):
         t = True
         return arr["_default"][i]

    if t == False:
      return {}

  def search(self, k = None, v = None) -> list:
    if not k and not v:
      raise ValueError("Not enough arguments were provided. Atleast the key or both key and value have to be provided")

    if k and not v and type(k) != tuple:
      arr = []
      for _ in self:
        if k in _.keys():
          arr.append(_)

    else:
      if k and not v and type(k) == tuple:
        k, v, e = k
      arr = []
      for _ in self:
        if eval(str(_[k]) + e + str(v)):
          arr.append(_)

    return arr

  def contains(self, k = None, v = None) -> bool:
    if k:
      if not v:
        k, v, e = k
      ans = False
      if len(self.get(k, v, e)) != 0:
        ans = True

      return ans

    else:
      raise ValueError("Both key and value have to be provided")
  
  def count(self, k = None, v = None) -> int:
    if k and not v and type(k) == tuple:
      return len(self.search(k))

    elif k and v:
      return len(self.search(k, v))

    else:
      raise ValueError("Both key and value have to be provided")

  def all(self) -> list:
    arr = []
    for _ in self:
        arr.append(_)

    return arr

  def delete(self, k = None, v = None) -> Union[bool, None]:
   if not k and not v:
     with open(self.db, "w+", newline = "\n") as db2:
       arr2 = toml.load(self.db)
       arr2["_default"] = None

       db2.write(toml.dumps(arr2))

   else:
    t = False
    arr = toml.load(self.db)

    if bool(arr) == True:

     for i in arr["_default"]:
      if k in arr["_default"][i] and v == arr["_default"][i][k]:
       with open(self.db, "w+", newline = "\n") as db2:

        arr["_default"][i] = None
        db2.write(toml.dumps(arr))

        t = True
        return True

    if t == False:
      return False
