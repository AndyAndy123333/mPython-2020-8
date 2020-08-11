from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,1,"1","1","1","1")

