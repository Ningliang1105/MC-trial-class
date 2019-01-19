# 这会生成一个魔法羊毛块
# 站上去试试看？
# 修改time_gap可以改变事件触发的频率间隔

import ministack
import time

import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff

time_gap = 5
block_id = 35

mc = minecraft.Minecraft.create()

pos_wool = mc.player.getTilePos()
pos_wool.y = pos_wool.y - 1
pos_wool.z = pos_wool.z + 5
ministack.setBlock(pos_wool.x, pos_wool.y, pos_wool.z, block_id)

trigger_block = pos_wool
trigger_block.y = trigger_block.y + 1

while True:
    pos = mc.player.getTilePos()
    if pos == trigger_block:
        mc.player.setPos(pos.x, pos.y + 100, pos.z)
        ministack.say("It is a trap!")
    time.sleep(time_gap)

# 当我们站在“这个位置”的时候，陷阱就被触发了
# 我们有哪些方法让计算机知道我们站在了“这个位置”？
# 判断坐标/判断脚下方块类型/判断移动的方向和距离
# 怎么知道这里用的是哪一种？
