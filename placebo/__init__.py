from pygame           import init as pygameInit
from pygame.font      import init as fontInit, SysFont, Font
from pygame.display   import init as displayInit, set_mode, set_caption, flip
from pygame.event     import get
from pygame.time      import Clock
from pygame.mouse     import get_pos, get_pressed as get_mouse_pressed
from pygame.key       import get_pressed as get_key_pressed
from pygame.mixer     import init as mixerInit
from pygame.locals    import *

def init():
  pygameInit()
  displayInit()
  fontInit()
  mixerInit()

class Window: 
  def __init__(self, title='Placebo App', width=800, height=600, mode=0, depth=32):
    self.title = title
    self.size = (width, height)
    self.mode = mode
    self.depth = depth
    self.clearColor = (255,255,255)
    self.fps = 120
    self.time = .0
    self.running = True
    self.display = set_mode((1,1), 32, self.depth)

    self.methods = []
    self.keyboard = KeyboardEvent()
    self.mouse = MouseEvent()
    self.events = ()

    # debug
    self.getFPS = False


  def setTitle(self, title='Placebo App'):
    self.title = title
    return self

  def setFPS(self, fps=60):
    self.fps = fps
    return self

  def setClearColor(self, color=(255,255,255)):
    self.clearColor = color
    return self

  def loop(self, *events):
    for event in events:
      self.methods.append(event)
    return self

  def exit(self):
    self.running = False

  def run(self):
    self.display = set_mode(self.size, self.mode, self.depth)
    set_caption(self.title)
    self.clock = Clock()

    while self.running:
      self.display.fill(self.clearColor)
      self.time = self.clock.tick(self.fps) / 20
      for event in get():
        self.events = event
        if event.type == QUIT:
          self.exit()

        self.mouse.event(event)
        self.keyboard.event(event)

      for method in self.methods:
        method(self)

      self.mouse.clear()
      self.keyboard.clear()
      flip()
      if self.getFPS: set_caption('%s %s FPS' % (self.title, int(self.clock.get_fps())))


class KeyboardEvent:
  def __init__(self):
    self.code = get_key_pressed()
    self.data = ''
    self.press = False
    self.key = 0

  def event(self, event):
    if event.type == KEYDOWN:
      self.press = True
      self.data += event.unicode
      self.code = get_key_pressed()
      self.key = event.key
    if event.type == KEYUP:
      self.press = False
      self.data = ''
      self.code = get_key_pressed()
      self.key = event.key

  def clear(self):
    self.data = ''
    self.press = False
    self.key = 0

class MouseEvent:
  def __init__(self):
    self.pos = (0,0)
    self.button = get_mouse_pressed()
    self.click = False

  def event(self, event):
    if event.type == MOUSEMOTION:
      self.pos = event.pos
    if event.type == MOUSEBUTTONDOWN:
      self.click = True
    if event.type == MOUSEBUTTONUP:
      self.click = False
    self.button = get_mouse_pressed()

  def clear(self):
    self.click = False