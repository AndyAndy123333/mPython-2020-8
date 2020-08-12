from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

for u in range(3):
    for i in range(50000):
      mc.setBlock(x+i,y-1,z+i+u,46)
    