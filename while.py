rom mcpi.minecraft import Minecraft
import time


while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat("I am iooking you.X:"+str(x)+"Y:"+str(y)+"Z:"+str(z))
    time.sleep(0.5)