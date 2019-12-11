'''
Created on 2019年12月11日

@author: Administrator
'''
import tkinter as tk

class MainGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('TkinterEditer')
        self.geometry('600x500') #设置窗口的大小
        self._MakeMenu()
        
    def _MakeMenu(self):
        self.menubar = tk.Menu(self, tearoff=0)
        
        self.fmenu = tk.Menu(self.menubar, tearoff=0)
        for item in ['新建','打开','保存','另存为']:
            self.fmenu.add_command(label = item)
        
        self.emenu = tk.Menu(self.menubar, tearoff=0)
        for item in ['复制','粘贴','剪切']:
            self.emenu.add_command(label = item)
        
        self.vmenu = tk.Menu(self.menubar, tearoff=0)
        for item in ['默认视图','新式视图']:
            self.vmenu.add_command(label = item)
        
        self.amenu = tk.Menu(self.menubar, tearoff=0)
        for item in ['版权信息','其他说明']:
            self.amenu.add_command(label = item)
        
        self.menubar.add_cascade(label = "文件",menu = self.fmenu)
        self.menubar.add_cascade(label = "编辑",menu = self.emenu)
        self.menubar.add_cascade(label = "视图",menu = self.vmenu)
        self.menubar.add_cascade(label = "关于",menu = self.amenu)
        self['menu'] = self.menubar

if __name__ == '__main__':
    root = MainGui()
    root.mainloop()