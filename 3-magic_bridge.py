# 这串代码会在你的脚下不断生成你指定的方块
# 在第12行写下你希望生成的方块类型；例子：46 TNT；7 基岩；20 玻璃；57 钻石

import ministack
import time

import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()

block_id = 1

while True:
    pos = mc.player.getTilePos()
    ministack.setBlock(pos.x, pos.y - 1, pos.z, block_id)
    time.sleep(0.5)

# 我的世界那么大，计算机怎么确定玩家的位置和该在哪里放方块呢？
# 引出坐标系。同学们也许学过二维坐标系。在我的世界里，多了一个维度，xyz分别代表东西、上下和南北
# 生活中还有哪些坐标系？（例如，经纬度；看书的时候会说第几行，第几个字）
