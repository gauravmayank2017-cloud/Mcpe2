from ursina import Button, scene, color, mouse, destroy

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='assets/textures/grass.png'):
        super().__init__(parent=scene, position=position, model='cube', 
                         texture=texture, origin_y=0.5, color=color.white)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                from src.voxel import Voxel
                Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
              
