import toml
import ast

class TomlDB:

  def __init__(self, db):
    self.db = db
    self.i = 1
    self.json = {}

    with open(db, "r"):
      pass
 
  def insert(self, var):
   if type(var) == dict:
    self.json = var

    with open(self.db, "a+", newline = "\n") as db2:

      self.i = len(toml.load(self.db)['_default']) + 1 if bool(toml.load(self.db)) == True else 1
      db2.write(toml.dumps({"_default": {f"{self.i}": self.json}}) + "\n")

   else:
     raise TypeError("Value specified for the insert function was not a dict")

  def update(self, var, k, v):
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
        self.add(ast.literal_eval(var[3::]), k, int(v))

       elif var[0:3] == "sub":
        self.subtract(ast.literal_eval(var[3::]), k, int(v))

     else:
       raise TypeError("Value specified for the update function was not a dict")
 
  def add(self, var, k, v):
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

  def subtract(self, var, k, v):
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
  
  def get(self, k = None, v = None):
   if not k and not v:
     return toml.load(self.db)

   else:
    t = False
    arr = toml.load(self.db)

    if bool(arr) == True:

     for i in arr["_default"]:
      if k in arr["_default"][i] and v == arr["_default"][i][k]:
       return arr["_default"][i]
       t = True

    if t == False:
      return {}

  def delete(self, k = None, v = None):
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
