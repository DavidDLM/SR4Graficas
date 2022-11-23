from gl import Renderer, _color_, V2, V3
from textures import Texture
from obj import Obj

from shaders import greyScale

#################################

width = 1300
height = 866
depth = -10
black = _color_(0, 0, 0)
white = _color_(1, 1, 1)

rend = Renderer(width, height)
#rend.dirLight = V3(0, 0, 1)
rend.glClearBackground()

#################################
rend.active_shader = greyScale
#rend.active_texture = Texture("models/yellowTX.bmp")
rend.glLoadModel("models/Trumpet.obj",
                 translate=V3(2, -2.5, -13),
                 scale=V3(9, 9, 9),
                 rotate=V3(0, 2, 70))
#################################

rend.write("SR4.bmp")
