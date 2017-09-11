from zipfile import ZipFile
from io import BytesIO
from json import loads

class Assets:
  def __init__(self, path):
    # locales
    self.files = [];

    # open archive
    self.zip = ZipFile(path, 'r');
    self.update()

  def update(self):
    self.files = [];
    for filename in self.zip.namelist():
      if filename[-1:] != '/':
        self.files.append(filename)

  def text(self, name):
    if type(name) == str:
      return self.zip.read(name)
    elif type(name) == list:
      data = {}
      for item in name:
        data[item] = self.zip.read(item)
      return data

  def cfg(self, name):
    if type(name) == str:
      return loads(self.zip.read(name))
    elif type(name) == list:
      data = {}
      for item in name:
        data[item] = loads(self.zip.read(item))
      return data

  def res(self, name):
    if type(name) == str:
      return BytesIO(self.zip.read(name))
    elif type(name) == list:
      data = {}
      for item in name:
        data[item] = BytesIO(self.zip.read(item))
      return data

  def close(self):
    self.zip.close()
    return True
