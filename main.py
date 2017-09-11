from placebo.engine import init, Engine, Scene, Object, Component
from placebo.camera import Camera
from placebo.ui import Image, Animation


class CameraControllerComponent(Component):
  def update(self, obj, scene, engine):
    if engine.keyboard.code[276]:
      obj.move(5)
    elif engine.keyboard.code[275]:
      obj.move(-5)
    if engine.keyboard.code[273]:
      obj.move(0, 3)
    elif engine.keyboard.code[274]:
      obj.move(0, -3)

class GrassComponent(Component):
  def init(self, obj, scene, engine):
    self.image = Image('assets/'+self.name+'.png', obj.x, obj.y)

  def update(self, obj, scene, engine):
    self.image.setPos(obj.x, obj.y)
    self.image.render(engine)

class TreesComponent(Component):
  def init(self, obj, scene, engine):
    self.image = Image('assets/'+self.name+'.png', obj.x, obj.y)
    self.image.setSize(self.image.width*10, self.image.height*10)

  def update(self, obj, scene, engine):
    self.image.setPos(obj.x+self.image.width/2, obj.y-self.image.height)
    self.image.render(engine)

class HeroControllerComponent(Component):
  def update(self, obj, scene, engine):
    obj.data['image'].play(obj.data['lastRoute'] + 'Stay')
    if engine.keyboard.code[306]:
      obj.data['image'].play(obj.data['lastRoute'] + 'Sitdown')
    if engine.keyboard.code[276]:
      obj.move(-5)
      obj.data['lastRoute'] = 'left'
      obj.data['image'].play(obj.data['lastRoute'] + 'Run')
    elif engine.keyboard.code[275]:
      obj.move(5)
      obj.data['lastRoute'] = 'right'
      obj.data['image'].play(obj.data['lastRoute'] + 'Run')
    if engine.keyboard.code[273]:
      obj.move(0, 3)
      obj.data['image'].play(obj.data['lastRoute'] + 'Run')
    elif engine.keyboard.code[274]:
      obj.move(0, -3)
      obj.data['image'].play(obj.data['lastRoute'] + 'Run')

class HeroAnimationComponent(Component):
  def init(self, obj, scene, engine):
    obj.data['lastRoute'] = 'right'
    obj.data['image'] = Animation({
      'leftStay': {
        'delay': .1,
        'frames': ['assets/stay_left_1.png']
      },
      'rightStay': {
        'delay': .1,
        'frames': ['assets/stay_right_1.png']
      },
      'leftSitdown': {
        'delay': .1,
        'frames': ['assets/sitdown_left_1.png']
      },
      'rightSitdown': {
        'delay': .1,
        'frames': ['assets/sitdown_right_1.png']
      },
      'leftRun': {
        'delay': .1,
        'frames': ['assets/run_left_1.png', 'assets/run_left_2.png', 'assets/run_left_3.png', 'assets/run_left_4.png', 'assets/run_left_5.png', 'assets/run_left_6.png', 'assets/run_left_7.png', 'assets/run_left_8.png']
      },
      'rightRun': {
        'delay': .1,
        'frames': ['assets/run_right_1.png', 'assets/run_right_2.png', 'assets/run_right_3.png', 'assets/run_right_4.png', 'assets/run_right_5.png', 'assets/run_right_6.png', 'assets/run_right_7.png', 'assets/run_right_8.png']
      },
    }, obj.x, obj.y, 46*2, 50*2)                                                                                         
    obj.data['image'].play(obj.data['lastRoute'] + 'Stay')

  def update(self, obj, scene, engine):
    obj.data['image'].setPos(obj.x+obj.data['image'].width/2, obj.y-obj.data['image'].height)
    obj.data['image'].render(engine)


# init libraries
init()

# create app
app = Engine('Placebo Engine', 1000, 600)

# screate scene
mainScene = Scene('main')
settingsScene = Scene('settings')
gameScene = Scene('game')

# create objects

## CAMERA
cameraObject = Camera('Camera')
cameraObject.add(CameraControllerComponent('Camera Controller'))

## TREES
heroObject = Object('hero', 300, 300)
heroObject.add(HeroAnimationComponent('Hero Animation'), HeroControllerComponent('Hero Controller'))
#
grassObject = Object('grass', -200, -200)
grassObject.add(GrassComponent('grass_1'))
#
trees1Object = Object('trees1', 100, 100)
trees1Object.add(TreesComponent('trees_1'))
#
trees2Object = Object('trees2', 250, 200)
trees2Object.add(TreesComponent('trees_2'))
#
trees3Object = Object('trees3', 400, 300)
trees3Object.add(TreesComponent('trees_3'))


# add object to scene
mainScene.add(heroObject, cameraObject, grassObject, trees1Object, trees2Object, trees3Object)

# add scenes in to engine
app.add(mainScene, settingsScene, gameScene)

# go to 'main' scene
app.goTo('main')

# start application
app.start()