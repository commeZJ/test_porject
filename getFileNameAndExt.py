'''
根据文件的完整路径返回文件名和扩展名
'''
import os

def GetFileNameAndExt(filename):
    (filepath,tempfilename)=os.path.split(filename)
    (shortname,extension)=os.path.splitext(tempfilename)
    return shortname,extension

print(GetFileNameAndExt('D:\pydj\test_porject\datatypes.py'))