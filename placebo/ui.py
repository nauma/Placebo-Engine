from pygame.draw  import rect, lines, circle
from pygame.font  import SysFont, Font
from pygame.image import load as imageLoad
from pygame.transform import scale, rotate
from pygame.mouse import set_visible
from json import loads

class Label:
  def __init__(self, text, x=0, y=0, width=0, height=0, font="arial", size=16, color=(255, 255, 255), aling="left", antialias=1):
    self.text = text
    self.x = x
    self.y = y
    self.size = size
    self.color = color
    self.font = SysFont(font, size)
    self.aling = aling
    self.antialias = antialias
    self.width = width
    self.height = height

  def setText(self, text):
    self.text = text
    return self

  def setSize(self, size):
    self.size = size
    self.font = Font(font, self.size)
    return self

  def setFont(self, font):
    self.font = Font(font, self.size)
    return self

  def setColor(self, color=(255, 255, 255)):
    self.color = color
    return self

  def setPos(self, x=None, y=None):
    self.x = x if x else self.x
    self.y = y if y else self.y
    return self

  def setAlign(self, mode):
    self.aling = mode
    return self

  def render(self, window):
    nextLine = 0
    data = self.text.split('\n')

    for line in data:
      size = self.font.size(line)
      self.height += size[1]
      self.width = size[0] if size[0] > self.width else self.width

    x = self.x

    for line in data:
      line_width = self.font.size(line)[0]
      if self.aling == "center":
        x = self.x + (self.width//2-line_width)//2
      elif self.aling == "right":
        x = self.x + (self.width//2-line_width)

      text = self.font.render(line, self.antialias, self.color)
      window.display.blit(text, (x, self.y+nextLine))
      nextLine += self.size

class Button:
  def __init__(self, text, x=0, y=0, width=None, height=None, color=(255,255,255), background=(0,0,255), font="verdana", size=16):
    self.text = text
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.background = background
    self.size = size
    self.font = SysFont(font, self.size)
    self.events = ()

  def setText(self, text):
    self.text = text
    return self

  def setColor(self, color):
    self.color = color
    return self

  def setBackground(self, background):
    if type(background) == tuple:
      self.background = background
    else:
      self.background = Image(background)
      self.background.setPos(self.x, self.y)
      self.background.setSize(self.width, self.height)
    return self

  def setPos(self,*, x=None, y=None):
    self.x = x if x else self.x
    self.y = y if y else self.y
    return self

  def setFont(self, font):
    self.font = Font(font, self.size)
    return self

  def setSize(self, width=None, height=None):
    self.width = width if width else self.width
    self.height = height if height else self.height
    return self

  def addEvent(self, *events):
    self.events += ()
    return self

  def render(self, window):
    # set button width
    if self.width == None:
      self.width = self.font.size(self.text)[0]
    if self.height == None:
      self.height = self.font.size(self.text)[1]

    shift = self.font.size(self.text[0])[0], self.font.size(self.text[0])[1]

    # draw background
    if type(background) == tuple:
      rect(window.display, (self.background), (self.x, self.y, self.width + shift[0], self.height + shift[1]//4))
    else:
      self.background.setPos(self.x, self.y)
      self.background.render(window)
    # draw text
    window.display.blit(self.font.render(self.text, 1, self.color), (self.x + shift[0]//2 + (self.width-self.font.size(self.text)[0])//2, self.y + shift[1]//8 + ((self.height-self.font.size(self.text)[1])//2)))

    # click button event
    if window.mouse.click and window.mouse.button[0]:
      if window.mouse.pos[0] >= self.x and window.mouse.pos[0] <= self.x + self.width:
        if window.mouse.pos[1] >= self.y and window.mouse.pos[1] <= self.y + self.height:
          for event in self.events:
            event()

class Image:
  def __init__(self, path, x=0, y=0):
    self.image = imageLoad(path).convert_alpha()
    self.x = x
    self.y = y
    self.width, self.height = self.image.get_rect().size

  def setPath(self, path):
    self.image = imageLoad(path).convert_alpha()
    return self

  def setPos(self, x=None, y=None):
    self.x = x if x else self.x
    self.y = y if y else self.y
    return self

  def setSize(self, width, height):
    self.image = scale(self.image, (width, height))
    self.width, self.height = self.image.get_rect().size
    return self

  def setRotate(self, radius):
    self.image = rotate(self.image, -radius)
    return self

  def render(self, window):
    window.display.blit(self.image, (self.x, self.y))

class Images:
  def __init__(self, images=[]):
    self.list = {}
    for image in images:
      try:
        self.list[image] = Image(image)
      except Exception as e:
        print('Images -> error -> error to create a ', name)

  def render(self, window, name):
    if self.list.get(name):
      self.list[name].render(window)
    else:
      print('Images -> error -> %s not found' % name)

class Animation:
  def __init__(self, frames, x=0, y=0, width=False, height=False, loop=True):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.start = False
    self.activeFrame = False
    self.frames = frames

    self.delay = 0
    self.time = .0
    self.index = 0

    self.__update()

  def __update(self):
    for name in self.frames:
      for index in range(len(self.frames[name]['frames'])):
        frame = self.frames[name]['frames'][index]
        self.frames[name]['frames'][index] = Image(frame, self.x, self.y)
        if self.width != False or self.height != False:
          self.frames[name]['frames'][index].setSize(self.width, self.height)

  def setPos(self, x=None, y=None):
    self.x = x if x else self.x
    self.y = y if y else self.y
    return self

  def setSize(self, width, height):
    self.width = width
    self.height = height
    self.__update()

  def play(self, name):
    self.start = True
    self.delay = self.frames[name]['delay']
    self.activeFrame = name
    return self

  def stop(self):
    self.start = False
    return self

  def render(self, engine):
    self.time += self.delay

    if self.time > engine.time:
      self.index += 1
      self.time = 0

    if self.index > len(self.frames[self.activeFrame]['frames'])-1:
      self.index = 0
      self.time = .0
    
    self.frames[self.activeFrame]['frames'][self.index].setPos(self.x, self.y)
    self.frames[self.activeFrame]['frames'][self.index].render(engine)
    return self.frames[self.activeFrame]['frames'][self.index]

class Cursor:
  def __init__(self, path):
    self.image = Image(path)
    set_visible(False)

  def setPath(self, path):
    self.image = Image(path)

  def render(self, window):
    self.image.setPos(x=window.mouse.pos[0], y=window.mouse.pos[1])
    self.image.render(window)

class Fill:
  def __init__(self, color=(0, 255, 0)):
    self.color = color

  def setColor(self, color=(0, 255, 0)):
    self.color = color
    return self

  def render(window):
    window.display.fill(self.color)

class Rect:
  def __init__(self, color=(255, 0, 0), x=0, y=0, width=200, height=100):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  def setColor(self, color=(0, 255, 0)):
    self.color = color
    return self

  def setPos(self, x=0, y=0):
    self.x = x
    self.y = y
    return self

  def setSize(self, width=0, height=0):
    self.width = width
    self.height = height
    return self

  def render(self, window):
    rect(window.display, self.color, (self.x, self.y, self.width, self.height))

class Circle:
  def __init__(self, radius=10, color=(255, 0, 0), x=0, y=0, border=1):
    self.color = color
    self.x = x
    self.y = y
    self.radius = radius
    self.border = border

  def setColor(self, color=(0, 255, 0)):
    self.color = color
    return self

  def setPos(self, x=0, y=0):
    self.x = x
    self.y = y
    return self

  def setRadius(self, radius=10):
    self.radius = radius
    return self

  def setBorder(self, border=1):
    self.border = border
    return self

  def render(self, window):
    circle(window.display, self.color, (self.x, self.y), self.radius, self.border)