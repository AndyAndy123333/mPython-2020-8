from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    a = mc.getBlock(x+2,y-1,z)
    b = mc.getBlock(x-2,y-1,z)
    c = mc.getBlock(x,y-1,z+2)
    d = mc.getBlock(x,y-1,z-2)
    if a==8 or a==9 or b==8 or b==9 or c==8  or c==9  or d==8 or d==9:
        mc.setBlocks(x+2,y-1,z+2,x-2,y-1,z-2,79)
        