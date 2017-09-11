from pygame.mixer     import Sound

class Sounds:
  def __init__(self, sounds=[]):
    self.list = {}
    for sound in sounds:
      try:
        self.list[sound] = Sound(sound)
      except Exception as e:
        print('Sounds → error → fail load', name)

  def play(self, name):
    if self.list.get(name):
      self.list[name].play()
    else:
      print('Sounds → error → %s not found' % name)

  def pause(self, name):
    if self.list.get(name):
      self.list[name].pause()
    else:
      print('Sounds → error → %s not found' % name)

  def stop(self, name):
    if self.list.get(name):
      self.list[name].stop()
    else:
      print('Sounds → error → %s not found' % name)