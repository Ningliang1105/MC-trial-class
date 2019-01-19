# 选择菜单第一项在我的世界里建造一个3D打印机
# 试着在打印机里建造一些东西
# 建造完成后，换一个地方，选择第五项 - print from duplicator to player pos


import mcpi.minecraft as minecraft
import mcpi.block as block
import glob
import time
import random

mc = minecraft.Minecraft.create()

SIZEX = 10
SIZEY = 10
SIZEZ = 10

roomx = 1
roomy = 1
roomz = 1


def buildRoom(x, y, z):
  global roomx, roomy, roomz

  roomx = x
  roomy = y
  roomz = z

  mc.setBlocks(roomx, roomy, roomz,
    roomx+SIZEX+2, roomy+SIZEY+2, roomz+SIZEZ+2, block.GLASS.id)

  mc.setBlocks(roomx+1, roomy+1, roomz,
    roomx+SIZEX+1, roomy+SIZEY+1, roomz+SIZEZ+1, block.AIR.id)


def demolishRoom():
  mc.setBlocks(roomx, roomy, roomz,
    roomx+SIZEX+2, roomy+SIZEY+2, roomz+SIZEZ+2, block.AIR.id)


def cleanRoom():
  mc.setBlocks(roomx+1, roomy+1, roomz+1,
    roomx+SIZEX+1, roomy+SIZEY+1, roomz+SIZEZ+1, block.AIR.id)


def listFiles():
  print("\nFILES:")

  files = glob.glob("*.csv")

  for filename in files:
    print(filename)

  print("\n")

def scan3D(filename, originx, originy, originz):
  f = open(filename, "w")

  f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")

  for y in range(SIZEY):
    mc.postToChat("scan:" + str(y))

    f.write("\n")

    for x in range(SIZEX):
      line = ""
      for z in range(SIZEZ):
        blockid = mc.getBlock(originx+x, originy+y, originz+z)
        if line != "":
          line = line + ","
        line = line + str(blockid)
      f.write(line + "\n")
  f.close()


def print3D(filename, originx, originy, originz):
  f = open(filename, "r")

  lines = f.readlines()

  coords = lines[0].split(",")
  sizex = int(coords[0])
  sizey = int(coords[1])
  sizez = int(coords[2])

  lineidx = 1

  for y in range(sizey):
    mc.postToChat("print:" + str(y))
    lineidx = lineidx + 1
    for x in range(sizex):
      line = lines[lineidx]
      lineidx = lineidx + 1
      data = line.split(",")
      for z in range(sizez):
        blockid = int(data[z])
        mc.setBlock(originx+x, originy+y, originz+z, blockid)

def menu():
  while True:
    print("DUPLICATOR MENU")
    print(" 1. BUILD the duplicator room")
    print(" 2. LIST files")
    print(" 3. SCAN from duplicator room to file")
    print(" 4. LOAD from file into duplicator room")
    print(" 5. PRINT from duplicator room to player.pos")
    print(" 6. CLEAN the duplicator room")
    print(" 7. DEMOLISH the duplicator room")
    print(" 8. QUIT")

    choice = int(input("please choose: "))
    if choice < 1 or choice > 8:
      print("Sorry, please choose a number between 1 and 8")
    else:
      return choice


anotherGo = True

while anotherGo:
  choice = menu()

  if choice == 1:
    pos = mc.player.getTilePos()
    buildRoom(pos.x, pos.y, pos.z)

  elif choice == 2:
    listFiles()

  elif choice == 3:
    filename = input("filename?")
    scan3D(filename, roomx+1, roomy+1, roomz+1)

  elif choice == 4:
    filename = input("filename?")
    print3D(filename, roomx+1, roomy+1, roomz+1)

  elif choice == 5:
    scan3D("scantemp", roomx+1, roomy+1, roomz+1)
    pos = mc.player.getTilePos()
    print3D("scantemp", pos.x+1, pos.y, pos.z+1)

  elif choice == 6:
    cleanRoom()

  elif choice == 7:
    demolishRoom()

  elif choice == 8:
    anotherGo = False

# 给学生2分钟自由时间在打印机里建造
# 完成后在其他地方复制出来
# 提问：复制的时候，计算机需要记录哪些信息？
# 展示并讲解csv文件存储的内容
# 告诉大家，可以自己设计csv文件，就可以快速在我的世界里复制出造型
