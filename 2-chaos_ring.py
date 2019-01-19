# 这是一个能生成随机圆环的程序
# 在第14行选择圆环的方块种类范围
# 在第15行选择圆环的大小
# 运行就可以得到一个材料随机的混乱圆环

import ministack
import random
import time

import mcpi.minecraft as minecraft
import mcpi.minecraftstuff as minecraftstuff

block_range = [0, 30]
ring_radius = 10

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()

for i in range(ring_radius):
    block_id = random.randint(block_range[0], block_range[1])
    ministack.drawCircle(pos.x, pos.y, pos.z, i, block_id)
    ministack.drawHorizontalCircle(pos.x, pos.y, pos.z, i, block_id)
    time.sleep(1)

# 背景信息
# 计算机其实并不聪明，它们只是特别擅长做重复的事情
# 混乱圆环就是使用循环生成的
# 计算机生成圆环需要获取哪些信息？大家仔细观察圆环，每次生成一个新的圆环的时候，哪些东西变了？
# 再想一想，如果计算机能快速地重复完成一件事，那么生活中哪些事情适合让计算机完成？
