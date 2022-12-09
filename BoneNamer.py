import string

import maya.cmds as cmds
import re

def NameSetup():
        num = 0
        sels = cmds.ls(sl=True)

        while(True):

                while(True):
                        name = raw_input("Please define your name setup EX: Name_##_NodeType")
                        errorHashCheck = re.findall(r'[#]', name)
                        print(errorHashCheck)
                        errorUndCheck = re.findall(r'[_]', name)
                        if len(errorHashCheck) != 0 and errorUndCheck == [u'_', u'_']:
                                break
                        else:
                                if len(errorHashCheck) == 0:
                                        print("ERROR: Number spacing needs at least 1 # and no other characters.")
                                elif errorUndCheck != [u'_', u'_']:
                                        print("ERROR: Number spacing can only contain exactly 2 underlines")



                splitName = name.split("_")
                checker = re.findall(r'[^#]', splitName[1])



                underChecker = re.findall(r'[_]', name)


                if len(checker) == 0 and underChecker ==[u'_', u'_'] :
                        break
                else:
                        if len(checker)!=0:
                                print("ERROR: Number spacing can only contain #s.")
                        elif underChecker !=[u'_', u'_']:
                                print("ERROR: Number spacing can only contain exactly 2 underlines")
                        else:
                                print("UNKNOWN ERROR, WHAT THE HECK DID YOU DO?!?!?")


                numberPadding = 0





        for x in range(len(splitName[1])+1):
                numberPadding = x+1




        for sel in sels:

                num = num +1
                splitName[1] = str(num)
                splitName[1] =splitName[1].zfill(numberPadding-1)
                result = '_'.join(splitName)
                shape = cmds.listRelatives(sel)
                cmds.rename(result)


NameSetup()



