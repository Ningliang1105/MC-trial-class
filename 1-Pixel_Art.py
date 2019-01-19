# 这是一个用像素图切割基岩的代码文件
# 在第20行补充像素图文件
# 运行代码就可以在我的世界里看到所选择的像素图切割一大块基岩的效果

# 可供选择的像素图文件有：
# diamond.csv
# pikachu.csv
# mushroom.csv
# whale.csv
# pizza.csv


import ministack
import time

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff

pixel_art = 'whale.csv'

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getTilePos()
mc.setBlocks(x - 10, y - 7, z + 20,x + 10, y - 3 , z + 30, 7)
i = 0
while True:
    ministack.build(pixel_art, x, y, z + i)
    time.sleep(1)
    ministack.build(pixel_art, x, y, z + i, air = True)
    i = i + 1


# 背景信息
# 介绍Pixel - 像素
# 像素是计算机显示图像的方式，屏幕上显示的内容都是由一个个像素点拼成的
# 我的世界也是由一个个类似像素的方块构成的
# 在我的世界里，可以用相同的原理画出图像，比如皮卡丘……
# 告诉大家，可以自己设计csv文件，就可以快速在我的世界里复制出造型
