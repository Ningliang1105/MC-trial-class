# 这串代码会让你身边的方块都着火
# 试着修改block id，把火变成其他的东西
# 修改size，改变生成的区域

import ministack
import time

import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff

mc = minecraft.Minecraft.create()

block_id = 51
size = 5

while True:
    pos = mc.player.getTilePos()
    ministack.setBlocks(pos.x - size, pos.y, pos.z - size, pos.x + size, pos.y, pos.z + size, block_id)
    time.sleep(0.5)

# 生成的区域是怎么确定的？
# 两点确定一个长方形（正方形是特殊的长方形）
# 活动：在黑板上画2个点，让学生以这两个点为【【对角顶点】】，画一个长方形，看看有没有人能画出不一样的
