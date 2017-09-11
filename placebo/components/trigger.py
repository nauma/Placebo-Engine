from placebo.engine import Component

class Trigger(Component):
  def __init__(self, name, width, height):
    Component.__init__(self, name)
    self.width = width
    self.height = height

  def update(self, obj, scene, engine):
    pass

  def on(self, obj, scene, engine):
    pass

  def out(self, obj, scene, engine):
    pass