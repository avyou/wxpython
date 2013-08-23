#coding:utf-8
import wx

filenames = ["image.bmp", "image.gif", "image.jpg", "image.png" ]

bitmap_list = """ART_ERROR ART_GOTO_LAST ART_FILE_SAVE_AS ART_QUESTION ART_PRINT ART_DELETE ART_WARNING ART_HELP ART_COPY
              ART_INFORMATION ART_TIP ART_CUT ART_ADD_BOOKMARK ART_REPORT_VIEW ART_PASTE ART_DEL_BOOKMARK ART_LIST_VIEW
              ART_UNDO ART_HELP_SIDE_PANEL ART_NEW_DIR ART_REDO ART_HELP_SETTINGS ART_FOLDER ART_PLUS ART_HELP_BOOK
              ART_FOLDER_OPEN ART_MINUS ART_HELP_FOLDER ART_GO_DIR_UP ART_CLOSE ART_HELP_PAGE ART_EXECUTABLE_FILE
              ART_QUIT ART_GO_BACK ART_NORMAL_FILE ART_FIND ART_GO_FORWARD ART_TICK_MARK ART_FIND_AND_REPLACE ART_GO_UP
              ART_CROSS_MARK ART_HARDDISK ART_GO_DOWN ART_MISSING_IMAGE ART_FLOPPY ART_GO_TO_PARENT ART_NEW ART_CDROM
              ART_GO_HOME ART_FILE_OPEN ART_GOTO_FIRST ART_FILE_SAVE""".split()
class imgTestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Loading Images")
        p = wx.Panel(self)

        fgs = wx.FlexGridSizer(cols=10, hgap=10, vgap=10)

        for eachIcon in bitmap_list:
            #eachIcon = '.'.join(('wx',eachIcon))
            eachIcon = "wx"+eachIcon
            print eachIcon
            #name = str(eachIcon).split("-")[2]
            img = wx.ArtProvider.GetBitmap(eachIcon,wx.ART_OTHER,(20,20))
            sb1 = wx.StaticBitmap(p, -1, img)
            fgs.Add(sb1)

        p.SetSizerAndFit(fgs)
        self.Fit()

app = wx.App()
frm = imgTestFrame()
frm.Show()
app.MainLoop()
