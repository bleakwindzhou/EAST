def imageclip(text_lines,img_name):
    from PIL import Image
    from dic2lyst_boundExpand import Dic2lyst
    import os
    n=len(text_lines)
    for i in range(n):
        lyst=text_lines[i]
        box=Dic2lyst(lyst)
        path="./original/"+img_name
        img = Image.open(path)
        #print(img.size)
        #print(box)
        dir=str("./"+img_name+"_outPut")
        isExists=os.path.exists(dir)
        if not isExists:
            os.makedirs(dir)                          #粘合路径，名称为图像名+_output。
        cropped = img.crop(box)  # (left, upper, right, lower)
        m=str(i)               # m为剪裁框的下标
        ext=os.path.splitext(img_name)[1]
        cropped.save(dir+"/"+m+ext)
'''
from dic2lyst_boundExpand import OrderDict
Dict1={ "x0": 173, "y0": 114, "x1": 574, "y1": 111, "x2": 574, "y2": 160, "x3": 173, "y3": 163, "score": 0.35490876604912774 }
Dict2={ "x0": 112, "y0": 926, "x1": 267, "y1": 926, "x2": 267, "y2": 941, "x3": 112, "y3": 941, "score": 0.2587779170111197 }
Dict1=OrderDict(Dict1)
Dict2=OrderDict(Dict2)
Dict=[Dict1,Dict2]
imageclip(Dict)
'''