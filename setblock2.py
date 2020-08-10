from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z, = mc.player.getTilePos()
mc.setblock(x+1,y,z,15)
mc.setblock(x-1,y,z,15)
mc.setblock(x,y,z+1,15)
mc.setblock(x,y,z-1,15)