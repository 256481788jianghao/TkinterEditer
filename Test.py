'''
Created on 2019年12月11日

@author: Administrator
'''

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tree=ttk.Treeview(root)
 
#         #参数:parent, index, iid=None, **kw (父节点，插入的位置，id，显示出的文本)
myid=tree.insert("",0,"中国",text="中国China",values=("1"))  # ""表示父节点是根
myidx1=tree.insert(myid,0,"广东",text="中国广东",values=("2"))  # text表示显示出的文本，values是隐藏的值
myidx2=tree.insert(myid,1,"江苏",text="中国江苏",values=("3"))
myidy=tree.insert("",1,"美国",text="美国USA",values=("4"))    
myidy1=tree.insert(myidy,0,"加州",text="美国加州",values=("5"))
 
tree.pack(fill='both',expand='yes')

root.mainloop()
