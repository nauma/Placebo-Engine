from .engine import Object

class Camera(Object):
  def __init__(self, name, x=0, y=0):
    Object.__init__(self, name, x, y, priority=0)

  def set(self, x=False, y=False):
    self.x = x if x else self.x
    self.y = y if y else self.y
    return self

  def move(self, x=0, y=0):
    self.x += x
    self.y += y
    return self

  def render(self, scene, engine):
    for component in self.components:
      if component._alreadyStarted == False:
        component.init(self, scene, engine)
        component._alreadyStarted = True
      else:
        component.update(self, scene, engine)

    for i in range(len(scene.objects)):
      if scene.objects[i].name == self.name: continue
      scene.objects[i].x = self.x
      scene.objects[i].y = self.y