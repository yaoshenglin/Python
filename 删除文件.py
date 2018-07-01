# -*- coding: UTF-8 -*-
import os
import wx

dirPath = "E:\\PyProgramPack"

# 文件拖动操作
class FileDrop(wx.FileDropTarget):
    def __init__(self, object):
        wx.FileDropTarget.__init__(self)
        self.textCtrl = object

    def OnDropFiles(self, x, y, filePath):  # 当文件被拖入后，会调用此方法
        # print(filePath)
        if len(filePath) > 0:
            strPath = filePath[0]
            self.textCtrl.SetLabelText(strPath)
        else:
            print("文件路径不存在")

        return 0

class ButtonFrame(wx.Frame):
    def __init__(self,master=None):
        wx.Frame.__init__(self, None, -1, '删除文件', size=(350, 500))
        # self.Bind(wx.EVT_CLOSE, self.OnClose)

        panel = wx.Panel(self, -1)
        self.label1 = wx.StaticText(panel, -1, '文件路径', pos=(100, 60), size=wx.DefaultSize)
        self.label2 = wx.StaticText(panel, -1, '', pos=(100, 60), size=wx.DefaultSize)

        self.textCtrl1 = wx.TextCtrl(panel, -1, '', pos=(200, 10), size=wx.DefaultSize)
        self.textCtrl1.SetDropTarget(FileDrop(self.textCtrl1))  # 事件

        self.button1 = wx.Button(panel, -1, "删除", pos=(100, 20))
        self.Bind(wx.EVT_BUTTON, lambda evt: self.OnClick(evt, 1), self.button1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(2, 2, 10, 10)

        fgs.AddMany([self.label1, (self.textCtrl1, 1, wx.EXPAND), self.label2, self.button1 ])
        fgs.AddGrowableRow(1, 1)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

    def OnClick(self, event, mark):
        strPath = self.textCtrl1.GetValue()
        if os.path.exists(strPath):
            os.remove(strPath)
        else:
            self.ShowMessage("文件不存在")

    def ShowMessage(self, content):
        wx.MessageBox(content, "提示", wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()
