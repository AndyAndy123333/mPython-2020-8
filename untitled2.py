from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random
time.sleep(5)
x,y,z = mc.player.getTilePos()
colar = random.randrange(0,16)
mc.setBlocks(x+100,y-1,z+100,x-100,y-1,z-100,95)
