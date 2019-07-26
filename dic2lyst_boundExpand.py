def Dic2lyst(dic):
    lystx=[]
    lysty=[]
    lst_value=list(dic.values())             
    for i in range(0,7,2):
        lystx.append(lst_value[i])
    for i in range(1,8,2):
        lysty.append(lst_value[i])
    #print(lystx)
    #print(lysty)        
    lyst=[min(lystx),min(lysty),max(lystx),max(lysty)]        #将坐标的字典转化为矩形框四点坐标
    x_size=lyst[2]-lyst[0]
    lyst[0]-=x_size*0.1
    lyst[2]+=x_size*0.1                 #边界扩宽
    return lyst

lyst={ "x0": 662, "y0": 551, "x1": 1010, "y1": 545, "x2": 1010, "y2": 561, "x3": 662, "y3": 567, "score": 0.2729945127192481 }
lyst=Dic2lyst(lyst)
#print(lyst)

    
def OrderDict(dic) :
    import collections
    #dic={ "x0": 662, "y0": 551, "x1": 1010, "y1": 545, "x2": 1010, "y2": 561, "x3": 662, "y3": 567, "score": 0.2729945127192481 }
    dic1 = collections.OrderedDict()
    dic1["x0"] = dic["x0"]
    dic1["y0"] = dic["y0"]
    dic1["x1"] = dic["x1"]
    dic1["y1"] = dic["y1"]
    dic1["x2"] = dic["x2"]
    dic1["y2"] = dic["y2"]
    dic1["x3"] = dic["x3"]
    dic1["y3"] = dic["y3"]             #字典有序转化为无序
    #print(dic1)
    return dic1
    #print(lst_value)