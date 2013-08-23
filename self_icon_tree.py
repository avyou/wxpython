import wx


bitmap_list = """ART_ERROR ART_GOTO_LAST ART_FILE_SAVE_AS ART_QUESTION ART_PRINT ART_DELETE ART_WARNING ART_HELP ART_COPY
              ART_INFORMATION ART_TIP ART_CUT ART_ADD_BOOKMARK ART_REPORT_VIEW ART_PASTE ART_DEL_BOOKMARK ART_LIST_VIEW
              ART_UNDO ART_HELP_SIDE_PANEL ART_NEW_DIR ART_REDO ART_HELP_SETTINGS ART_FOLDER ART_PLUS ART_HELP_BOOK
              ART_FOLDER_OPEN ART_MINUS ART_HELP_FOLDER ART_GO_DIR_UP ART_CLOSE ART_HELP_PAGE ART_EXECUTABLE_FILE
              ART_QUIT ART_GO_BACK ART_NORMAL_FILE ART_FIND ART_GO_FORWARD ART_TICK_MARK ART_FIND_AND_REPLACE ART_GO_UP
              ART_CROSS_MARK ART_HARDDISK ART_GO_DOWN ART_MISSING_IMAGE ART_FLOPPY ART_GO_TO_PARENT ART_NEW ART_CDROM
              ART_GO_HOME ART_FILE_OPEN ART_GOTO_FIRST ART_FILE_SAVE""".split()
class myTestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
        title="simple tree with icons", size=(400,500))

# Initail all wx_ART_XX images
        text_imglist = self.InitialImageList()
# Create an image list 
        il = wx.ImageList(16,16)
        text_intImglist = []
        cant_add_text = []
        for text,img in text_imglist:
            try:
                text_intImglist.append( (text,il.Add(img)))
                print text
            except:cant_add_text.append(cant_add_text)

# Get some standard images from the art provider and add them
# to the image list
        self.fldridx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER,wx.ART_OTHER, (16,16)))
        self.fldropenidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,wx.ART_OTHER, (16,16)))
        self.fileidx = il.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE,wx.ART_OTHER, (16,16)))

# Create the tree
        self.tree = wx.TreeCtrl(self)
# Give it the image list
        self.tree.AssignImageList(il)
        root = self.tree.AddRoot("wx.ART_xx images")
        self.tree.SetItemImage(root, self.fldridx,
        wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.fldropenidx,
        wx.TreeItemIcon_Expanded)

        for text,imgindex in text_intImglist:
            if text in cant_add_text:
                continue
            item = self.tree.AppendItem(root,text)
            self.tree.SetItemImage(item, imgindex, wx.TreeItemIcon_Normal)
            self.tree.Expand(root)

    def InitialImageList(self):
        text_imglist = []
        cimg = wx.ArtProvider.GetBitmap(wx.ART_ADD_BOOKMARK,wx.ART_OTHER,(16,16))
# cimg = wx.ArtProvider.GetBitmap(wx.ART_ADD_BOOKMARK,wx.ART_ADD_BOOKMARK,(16,16)) 
        try:
            #print bitmap_list
            for eachIcon in bitmap_list:
                #eachIcon = '.'.join(('wx',eachIcon))
                eachIcon = "wx"+eachIcon
                print eachIcon
                #name = str(eachIcon).split("-")[2]
                text_imglist.append((eachIcon[2:],wx.ArtProvider.GetBitmap(eachIcon,wx.ART_OTHER,(16,16))))

        except:
            pass
        return text_imglist


app = wx.App()
frame = myTestFrame()
frame.Show()
app.MainLoop()
