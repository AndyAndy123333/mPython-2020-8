from mcpi.minecraft import Minecraft
mc = Minecraft.create()
Line1 = []
Line2 = []
Line3 = []
for i in range(1,4):
   Line1.append(1*i)
   Line2.append(2*i)
   Line3.append(3*i)   

x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,1,str(Line1),str(Line2),str(Line3))