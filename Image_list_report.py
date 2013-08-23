#coding:utf-8
import wx
import sys, glob, random

columns = ["Request ID", "Summary", "Date", "Submitted By"]

rows = [
    ("987441", "additions to RTTI?", "2004-07-08 10:22", "g00fy"),
    ("846368", "wxTextCtrl - disable auto-scrolling", "2003-11-20 21:25", "ryannpcs"),
    ("846367", "Less flicker when resizing a window", "2003-11-20 21:24", "ryannpcs"),
    ("846366", "Wishlist - wxDbGetConnection return value", "2003-11-20 21:23", "ryannpcs"),
    ("846364", "wxPostscriptDC with floating point coordinates", "2003-11-20 21:22", "ryannpcs"),
    ("846363", "Wishlist - Better wxString Formatting", "2003-11-20 21:22", "ryannpcs"),
    ("846362", "Wishlist - Crossplatform wxRichText Widget", "2003-11-20 21:20", "ryannpcs"),
    ("953341", "Support for paper trays when printing", "2004-05-13 08:01", "tonye"),
    ("952466", "mac menu - Window menu", "2004-05-12 03:19", "pimbuur"),
    ("928899", "FloatCanvas demo should work with numarray", "2004-04-03 08:30", "glchapman"),
    ("912714", "wxGrid: Support for Search / Replace", "2004-03-09 05:46", "rclund"),
    ("901061", "wxComboBox - add small icons as in MSW CComboBoxEx ", "2004-02-20 04:04", "tomash"),
    ("900768", "Please add more codepages support to your source built", "2004-02-19 15:49", "jsat66"),
    ("894921", "trigger on event-system creation", "2004-02-11 08:10", "g00fy"),
    ("869808", "HitTest in wxCheckListBox", "2004-01-03 01:22", "dickkniep"),
]

class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,"wx.ListCtrl in wx.LC_REPORT mode",size=(700,400))

        ##创建一个图像列表
        il = wx.ImageList(width=16,height=16, mask=True,initialCount=1)
        for name in glob.glob("icons/*.png"):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            ## Add(bitmap, mask=wx.NullBitmap) 来将一个图像添加到列表，bitmap, mask 都是wx.Bitmap 的实例
            ## 如果你有一个wx.Icon对象要添加到图像列表，可以使用方法AddIcon(icon)
            il_max = il.Add(bmp)
            ##所有这些添加方法都返回这个新加的图像在列表中的索引值，你可以保留索引值以便日后使用该图像。
            print il_max
            ## Remove(index) 可以从图像列表删除一个图像，RemoveAll()删除全部
            ## Replace(index, bitmap, mask=wx.NullBitmap) 修改特定索引的位图
            ## ReplaceIcon(index.icon) 修改项目的一个图标

        ##创建一个列表控件，wx.LC_REPORT为报告模式， wx.LC_VRULES 为列与列之间的网络线
        self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_VRULES)
        ## SetSingleStyle 动态方式改变列表控件一个样式标记
        self.list.SetSingleStyle(wx.LC_HRULES,True)
        ##SetWindowStyleFlag(style)能够重置整个窗口的样式，
        # 如SetWindowStyleFlag(LC_REPORT | LC_NO_HEADER)。这些方法对于在运行时修改列表控件的样式就有用处的。
        #self.list.SetWindowStyleFlag(wx.LC_REPORT | wx.LC_HRULES)

        ##图像列表必须被赋给一个列表控件，使用下面的方法
        self.list.AssignImageList(il, wx.IMAGE_LIST_SMALL)

        # Add some columns
        ##列标头的内容
        for col, text in enumerate(columns):
            ##创建列, InsertColumn(col, heading, format=wx.LIST_FORMAT_LEFT, width=-1)
            ##col为新列的索引，heading 是列标题，format为对齐方式，width是列初始显示宽度
            self.list.InsertColumn(col, text)

        # add the rows
        for item in rows:
            ##增加一个新行
            ##仅插入字符串使用 InsertStringItem(index,label)方法， 插入图像使用 InsertImageItem(index, imageIndex)
            ##插入既有图像又有字符串标签的项目使用 InsertImageStringItem(index, label, imageIndex)
            index = self.list.InsertStringItem(sys.maxint, item[0])
            #print index,sys.maxint,item[0]
            for col, text in enumerate(item[1:]):
                ##在列中设置字符串，SetStringItem(index,col,label,imageId=-1)
                #index是行索引，col为列索引，col为0设置第一列，它只对已有行使用。 label 显示单元格文本，
                ## imageId 是图像列表中的索引
                self.list.SetStringItem(index, col+1, text)

            # give each item a random image
            img = random.randint(0, il_max)
            ##你可以使用SetItemImage(item, image, selImage)来为一个项目设置图像item参数是该项目在列表中的索引，
            ## image和selImage都是图像列表中的索引，分别代表通常显示的图像和被选中时显示的图像。
            self.list.SetItemImage(index, img, img)
                
        # set the width of the columns in various ways
        self.list.SetColumnWidth(0, 120)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)


app = wx.App()
frame = DemoFrame()
frame.Show()
app.MainLoop()
