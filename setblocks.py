from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
time.sleep(5)
x,y,z = mc.player.getTilePos()
mc.setBlocks(x+100,y-1,z+100,x-100,y-1,z-100,57)
