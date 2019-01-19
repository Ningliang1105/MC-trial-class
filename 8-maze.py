# 读取csv文件，在我的世界里建造出一个迷宫
# 修改block_id可以改变迷宫的材料


import mcpi.minecraft as minecraft
import mcpi.block as block

block_id = 1

mc = minecraft.Minecraft.create()
ha = open("mazel.csv","r")
a = ha.readlines()
ha.close()
pos = mc.player.getTilePos()

x = pos.x + 1
y = pos.y
z = pos.z + 1

zm = z

def maze():
    global zm
    for lines in a:
        d = lines.strip().split(",")
        xm = x
        for items in d:
            if items == "1":
                mc.setBlock(xm,y,zm,block_id)
                mc.setBlock(xm,y + 1,zm,block_id)
                mc.setBlock(xm,y - 1,zm,20)
            else:
                mc.setBlock(xm,y,zm,0)
                mc.setBlock(xm,y+1,zm,0)
                mc.setBlock(xm,y-1,zm,20)
            xm += 1
        zm += 1
maze()

# 迷宫是怎么生成的？
# CSV文件记录位置、材料，我的世界里坐标系确定位置
# 思考：迷宫有几种走法？有没有一种走法一定能保证自己走出去？
