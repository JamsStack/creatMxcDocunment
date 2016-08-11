# -*- coding: utf-8 -*-
import os,arcpy,time,ArcToolbox
__name__ = 'test'  
def createMxdDocument(demoMXDPath,folder):  
     if os.path.exists(demoMXDPath) == False:  
        print ("mxd document it's not exist!")  
     else:  
        try:  
            print ("opening mxd document……")  
            mxd = arcpy.mapping.MapDocument(demoMXDPath)  
            print ("repair layer source")
            print(mxd)
            if os.path.isdir(folder) == False:  
                print ("invalid document path!")  
                return  
            print ("reading layer document one by one......")  
            files = os.listdir(folder)  
            #i=0  
        
            for f in files:  
               if f.endswith(".TIF"):  
                        df = arcpy.mapping.ListDataFrames(mxd, "图层")[0]#下载的为汉化版的为"图层"，英文版的为"Layer"
                        print(df)
                        print (arcpy.mapping.ListLayers(mxd, "", df)[0].name)  
                        lyr = arcpy.mapping.ListLayers(mxd, "", df)[0]
                        print(lyr)
                        print(lyr.dataSource)
                        print(folder)
                        print(f)
                        f1=f.replace(".TIF", "")
                        print(f1)
                        lyr.replaceDataSource(folder,"RASTER_WORKSPACE",f1)#需要去掉.TIF后缀才能替换成功
                        print(123456)
                        lyr.name=f.replace(".TIF", "")
                        print(lyr.name)
                        #mxdName=time.strftime("%Y_%m_%d_%H_%M_%S_", time.localtime())+".mxd" #2015_11_24样式文件名 
                        mxdName=lyr.name+".mxd"
                        newMXD=folder+"\\"+mxdName 
                        mxd.saveACopy(newMXD)                 
        except Exception as e:  
            print ("open mxd error: ", e)  
            return  
#tiffFolder="nasadata"         
#folder=r"D:\ly"+"\\"+tiffFolder 
today=time.strftime("%m.%d")
dirpath=r'E:\Data\Landsat8\wuhan\\2016\\'+today+'' 
createMxdDocument(r"D:\ly\hb\123456.mxd",dirpath)
