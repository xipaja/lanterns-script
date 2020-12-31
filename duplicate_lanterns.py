import maya.cmds as cmds
import maya.mel as mel
import sys
import random

for i in range(5):
    dup = cmds.duplicate("lantern")
    lightDup = cmds.duplicate("pointLight1")
    
    # place lanterns in random positions in space
    x = random.random() * 15
    y = random.random() * 15
    z = random.random() * 15
    cmds.parent(lightDup, dup)
    cmds.move(x, y, z, dup)
    cmds.rotate(i*2, i*20, 0, dup)
