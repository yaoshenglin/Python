# _*_ coding: UTF-8 _*_

__author__ = 'pc'

import wx
import os
import py2exe

# ASCII字符串转整数
def ASCIIStringConvertInter(s) :
    l = len(s) - 1
    if l != 3 :
        return 0

    value = 0
    for i in range(0,4) :
        s1 = s[i:i+1]
        value = ord(s1) * pow(256,l-i) + value
    return value

# 整数转ASCII字符串
def InterConvertASCIIString(num) :
    if num <= 0 :
        return null

    s = ""
    sub = num
    for i in range(0,4) :
        n = sub / pow(256, 3-i)
        sub = sub % pow(256,3-i)
        s = s + chr(int(n))

    return s

class ButtonFrame(wx.Frame):
    def __init__(self,master=None):
        wx.Frame.__init__(self, None, -1, 'Button Test',
                          size=(350, 500))
        panel = wx.Panel(self, -1)

        self.IDType = 1

        self.label1 = wx.StaticText(panel, -1, '1', size=wx.DefaultSize)
        self.label2 = wx.StaticText(panel, -1, '2', size=wx.DefaultSize)
        self.label3 = wx.StaticText(panel, -1, '3', size=wx.DefaultSize)

        self.button = wx.Button(panel, -1, "转换", pos=(100, 120))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        self.labelA = wx.StaticText(panel, -1, '整数地址', pos=(100, 60),
                      size=wx.DefaultSize)
        self.labelB = wx.StaticText(panel, -1, '字符串地址', pos=(100, 60),
                                   size=wx.DefaultSize)

        self.textCtrlA = wx.TextCtrl(panel, -1, '', pos=(100, 10),
                      size=wx.DefaultSize)
        self.Bind(wx.EVT_TEXT, self.TextEvents, self.textCtrlA)    # 文本输入框字符串变化事件
        self.textCtrlB = wx.TextCtrl(panel, -1, '', pos=(100, 10),
                                     size=wx.DefaultSize)
        self.Bind(wx.EVT_TEXT, self.TextEvents, self.textCtrlB)

        # textCtrl.SetHelpText("帮助")

        # 将上边俩文本框用Sizer管理布局
        sizer = wx.FlexGridSizer(cols=3, vgap=6, hgap=16)
        listItems = [self.label1, self.labelA, self.textCtrlA, self.label2, self.labelB, self.textCtrlB, self.label3, self.button]
        sizer.AddMany(listItems)
        panel.SetSizer(sizer)

    def OnClick(self, event):

        if self.IDType == 1:
            print(self.textCtrlA.GetValue())
            value = int(self.textCtrlA.GetValue())
            if value >= 88 :
                s = InterConvertASCIIString(value)
                self.textCtrlB.SetLabelText(s)
            else:
                print("输入不合法")
                self.ShowMessage("输入不合法")
        else:
            print(self.textCtrlB.GetValue())
            content = self.textCtrlB.GetValue()
            if len(content) == 4:
                value = ASCIIStringConvertInter(content)
                self.textCtrlA.SetLabelText(str(value))
            else:
                print("输入不合法")
                self.ShowMessage("输入不合法")


    def TextEvents(self, event):
        # self.textCtrl.SetLabelText(self.textCtrl.GetValue())
        if event.EventObject == self.textCtrlA :
            self.IDType = 1
        else:
            self.IDType = 2

    def ShowMessage(self, content):
        wx.MessageBox(content, "提示", wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    app = wx.App()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()