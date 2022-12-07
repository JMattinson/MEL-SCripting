import maya.cmds as cmds

def Shape_Color(color):
    try:
        sels = cmds.ls(sl=True)
        for sel in sels:
            shape = cmds.listRelatives(sel)
            cmds.setAttr(shape[0] + ".overrideEnabled", 1)
            cmds.setAttr(shape[0] + ".overrideColor", color)

    except:
        print("Invalid color. Please input a color between 0 & 31")
#Change this INT to change the selected wireframe's color.
Shape_Color(3)

