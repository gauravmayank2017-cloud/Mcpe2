from ursina import Ursina
from src.world import World
from src.player import Player

app = Ursina()
world = World()
player = Player()

if __name__ == "__main__":
    app.run()
  
