#coding:utf-8
import wx

class popupMenuFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Popup Menu Test")
        self.panel = panel = wx.Panel(self)

        ##创建位图
        bmp1 = wx.Bitmap("ico/f_open.ico", wx.BITMAP_TYPE_ICO)
        bmp2 = wx.Bitmap("ico/key1.ico", wx.BITMAP_TYPE_ICO)
        bmp3 = wx.Bitmap("ico/file1.ico", wx.BITMAP_TYPE_ICO)
        ##字体样式
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.BOLD)

        menubar = wx.MenuBar() ##创建菜单栏
        menu = wx.Menu()  ##创建菜单
        item = wx.MenuItem(menu,-1,"Has Open Bitmap") ##创建菜单项
        ##菜单项使用位图
        item.SetBitmap(bmp1)
        ##菜单项使用字体样式
        item.SetFont(font)
        menu.AppendItem(item) ##菜单项增加到菜单
        
        ##增加菜单项
        item = wx.MenuItem(menu,-1,"Font Bold test")
        item.SetBitmap(bmp2)
        item.SetFont(font)
        menu.AppendItem(item)
        ##增加菜单项
        item = wx.MenuItem(menu,-1,"Font color test")
        item.SetFont(font)
        item.SetTextColour("red")
        item.SetBitmap(bmp3)
        menu.AppendItem(item)

        menu.AppendSeparator()
        iexit = menu.Append(-1,"Exit")
        self.Bind(wx.EVT_MENU,self.OnExit, iexit)

        menubar.Append(menu,"Menu")
        self.SetMenuBar(menubar)

    def OnExit(self,event):
        self.Close()
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = popupMenuFrame()
    frame.Show()
    app.MainLoop()
