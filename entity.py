from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random
pos = mc.player.getPos()
while True:
    x = pos.x+random.uniform(-20,20)
    z = pos.z+random.uniform(-20,20)
    y = pos.y+30
    mc.spawnEntity(x,y,z,53)
    time.sleep(0.1)