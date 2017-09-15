# Placebo-Engine
Placebo - Python library on create games or other applications

## Import Game Engine
```python
from placebo.engine import init, Engine
```
using:
```python
init()
myGame = Engine("My first game", 1200, 720)

myGame.start()
```

### Using Scenes:
import class:
```python
from placebo.engine import init, Engine, Scene
```
create new scene `nameScene = Scene(sceneName)`
```python
mainScene = Scene('main')
```
add scene to engine:
```python
myGame.add(mainScene)
```
go to scene:
```python
myGame.goTo('main') # go to other scene
```

### Using Objects
import class:
```python
from placebo.engine import init, Engine, Scene, Object
```
create new object `objectName = Object(objectName)`
```python
firstObject = Object('firstObject')
```
add object to scene:
```python
mainScene.add(firstObject)
```

### Usign Components
import class:
```python
from placebo.engine import init, Engine, Scene, Object, Component
```
create personal component:
```python
class MyFirstComponent(Component):
  # this method run only once
  def init(self, object, scene, engine):
    print("Component '%s' initialed!", % self.name)

  # this method run only one game cycle
  def update(self, object, scene, engie):
    print("'%s' → is runned!", % self.name)
    
myFirstComponent = MyFirstComponent('firstComponent')
```
add component into object:
```python
firstObject.add(myFirstComponent)
```
