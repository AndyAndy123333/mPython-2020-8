from mcpi.minecraft import Minecraft
x,y,z, = mc.player.getTliPos()
mc = Minecraft.create()
mc.setblock(x+1,y,z,15)
mc.setblock(x-1,y,z,15)
mc.setblock(x,y,z+1,15)
mc.setblock(x,y,z-1,15)