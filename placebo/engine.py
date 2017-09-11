from . import init, Window, MouseEvent, KeyboardEvent
from operator import attrgetter

class Engine(Window):
  def __init__(self, title='Placebo Engine', width=1000, height=600, mode=0, depth=32):
    # window data
    Window.__init__(self, title, width, height, mode, depth)

    # engine data
    self.scenes = []

    # runtime data
    self.activeScene = False

  def add(self, *scenes):
    self.scenes += [scene for scene in scenes]
    return self
  
  def remove(self, name):
    for scene in self.scenes: 
      if scene.name == name: 
        self.scenes.remove(scene)
    return self

  def goTo(self, name=False):
    self.activeScene = name
    return self

  def __renderScene(self, engine):
    for scene in self.scenes:
      if scene.name == self.activeScene:
        scene.render(self)

  def start(self):
    self.loop(self.__renderScene)
    self.run()

class Scene:
  def __init__(self, name):
    # scene data
    self.name = name
    self.objects = []

    # runtime data
    self.data = {}

  def add(self, *objects):
    self.objects += [obj for obj in objects]
    return self

  def get(self, name):
    for obj in self.objects:
      if obj.name == name:
        return obj
    return False

  def remove(self, name):
    for obj in self.objects: 
      if obj.name == name: 
        self.objects.remove(obj)
    return self

  def render(self, engine):
    self.objects.sort(key=attrgetter('priority', 'z', 'y'))
    for obj in self.objects:
      obj.render(self, engine)

class Object:
  def __init__(self, name, x=0, y=0, z=0, priority=10):
    # object data
    self.name = name
    self.priority = priority

    self._x = x
    self._y = y

    self.x = 0
    self.y = 0
    self.z = z

    self.components = []

    # runtime data
    self.data = {}

  def add(self, *components):
    self.components += [component for component in components]
    return self

  def remove(self, name):
    for component in self.components: 
      if component.name == name: 
        self.components.remove(component)
    return self

  def setName(self, name):
    self.name = name
    return self

  def setPos(self, x=False, y=False, z=False):
    self._x = x if x else self._x
    self._y = y if y else self._y
    self.z = z if z else self.z
    return self

  def move(self, x=0, y=0):
    self._x += x
    self._y -= y
    return self

  def render(self, scene, engine):
    self.x += self._x
    self.y += self._y

    for component in self.components:
      if component._alreadyStarted == False:
        component.init(self, scene, engine)
        component._alreadyStarted = True
      else:
        component.update(self, scene, engine)

class Component:
  def __init__(self, name):
    self.name = name
    self._alreadyStarted = False

  def setName(self, name):
    self.name = name
    return self

  def init(self, obj, scene, engine):
    pass

  def update(self, obj, scene, engine):
    pass