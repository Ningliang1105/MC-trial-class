# 用这个代码来建造充能火车铁轨吧！
# distance这个参数能改变火车铁轨的大小（高度）

import ministack
import time

import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff

distance = 10

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

ministack.drawLine(pos.x, pos.y, pos.z, pos.x + distance, pos.y + distance, pos.z, 152)
ministack.drawLine(pos.x, pos.y + 1, pos.z, pos.x + distance, pos.y + distance + 1, pos.z, 27)

# 计算机需要知道哪些信息去画出这两条线？
# 两点确定一条直线/线段
#
