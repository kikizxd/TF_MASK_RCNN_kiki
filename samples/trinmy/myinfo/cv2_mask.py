# -*- coding: utf-8 -*-

import os,shutil

#在labelme_json里面的每个文件夹下复制label.png并命名为labelx.png
def copy_files():
    ##用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
    for foldName, subfolders, filenames in os.walk(path):
        #遍历列表下的所有文件名
        for filename in filenames:
            if filename.endswith('bel.png'):
                #为文件赋予新名字
                new_name=filename.replace('bel.png','belx.png')
                #复制并重命名文件
                shutil.copyfile(os.path.join(foldName,filename), os.path.join(foldName,new_name))
                #输出提示
                print(filename,"copied as",new_name)

#将labelx.png复制到cv2_mask文件夹并且按照原始图片命名
def rename_files():
    files=os.listdir(path)
    for file in files:
        jpath=os.listdir(os.path.join(path,file))
        #去除子文件夹中的'_json'，用以之后的label.png文件命名
        new=file[:-5]
        newnames=os.path.join('cv2_mask',new)
        filename=os.path.join(path,file,jpath[3])   #labelx.png在每个文件夹里为3，注意修改
        print(filename)
        os.rename(filename,newnames+'.png')   

if __name__ == '__main__':
    path = 'labelme_json'
    copy_files()
    rename_files() 



