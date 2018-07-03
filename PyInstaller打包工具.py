# -*- coding: UTF-8 -*-

import os
import wx
import shutil
import threading
import subprocess
import chardet

# global fileName

# 根据路径删除文件
def DeleteFile(path):
    if os.path.exists(path):
        print("删除 --> "+path)
        if os.path.isfile(path):
            os.remove(path) #文件
        elif os.path.isdir(path):
            shutil.rmtree(path) #目录

def MoveFile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname = os.path.split(dstfile)    #分离文件名和路径
        oldPath = os.path.join(dstfile,os.path.basename(srcfile))   #旧文件路径
        if os.path.isfile(oldPath):
            print(oldPath)
            os.remove(oldPath)                     # 先删除旧文件
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #如果不存在，则创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move %s -> %s"%( srcfile,dstfile))

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
        wx.Frame.__init__(self, None, -1, 'PyInstaller打包工具', size=(350, 500))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        panel = wx.Panel(self, -1)

        self.p = None
        self.label1 = wx.StaticText(panel, -1, '文件路径', pos=(100, 60), size=wx.DefaultSize)
        self.label2 = wx.StaticText(panel, -1, '', pos=(100, 30), size=wx.DefaultSize)
        self.label3 = wx.StaticText(panel, -1, '', pos=(100, 30), size=wx.DefaultSize)

        self.textCtrl = wx.TextCtrl(panel, -1, '', pos=(200, 10), size=wx.DefaultSize)
        self.fileDrop = FileDrop(self.textCtrl)  # 第1步，创建FileDrop对象，并把grid传给初始化函数
        self.textCtrl.SetDropTarget(self.fileDrop)  # 第2步，调用grid的SetDropTarget函数，并把FileDrop对象传给它
        # textCtrl.SetHelpText("帮助")

        self.button = wx.Button(panel, -1, "生成执行文件", pos=(100, 120))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

        self.textOut = wx.TextCtrl(panel, -1, '', pos=(200, 300), size=wx.DefaultSize, style = wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_READONLY)
        self.textOut.SetEditable(False)
        self.textOut.Hide()

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs = wx.FlexGridSizer(3, 2, 10, 10)    #5行，列，垂直间距，水平间距

        fgs.AddMany([(self.label1), (self.textCtrl, 1, wx.EXPAND), self.label2, self.button, self.label3, (self.textOut, 1, wx.EXPAND) ])
        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)
        hbox.Add(fgs, proportion=2, flag=wx.ALL | wx.EXPAND, border=15)
        panel.SetSizer(hbox)

        # 将上边俩文本框用Sizer管理布局
        # sizer = wx.FlexGridSizer(cols=2, vgap=6, hgap=16)
        # listItems = [self.label1, self.textCtrl, self.label2, self.button]
        # sizer.AddMany(listItems)
        # panel.SetSizer(sizer)

    def OnClick(self, event):

        strPath = self.textCtrl.GetValue()
        fileDir = os.path.dirname(strPath)
        fileName = os.path.basename(strPath)
        if len(strPath) == 0 :
            self.ShowMessage("路径不能为空")
            # self.textCtrl.SetLabelText("E:\\PyProgramPack\\Test.py")
        elif os.path.isdir(strPath):
            self.ShowMessage("请输入文件路径")
        elif not (os.path.exists(strPath)):
            self.ShowMessage("文件不存在")
        else:
            self.button.Disable()
            self.textCtrl.Disable()
            strCommand = "pyinstaller -F -w %s"%fileName
            tDrive = strPath.split("\\")[0] # 获得磁盘盘符
            # python pyinstaller.py - -version - file = file_version_info.txt - -icon = ico.ico - -onefile - -windowed target.py
            strCommand = "cd "+tDrive+" && "+"cd "+fileDir+" && "+strCommand    # 组合命令
            # self.ExecuteCommand(strCommand)
            # self.textOut.Show(True)
            t = threading.Thread(target=self.ExecuteCommand, args=(strCommand,))
            t.start()
            # t.join(15)
    def ExecuteCommand(self, strCommand):
        return_code = os.system(strCommand)  # 执行shell命令

        # wx.CallAfter(self.UpdateUI, UI="textOut", content=True)
        # p = subprocess.Popen(strCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # print("开始任务")
        # self.p = p
        # while p.poll() == None:
        #     line = p.stdout.readline()
        #     line = line.strip()
        #     if line:
        #         # 去掉一些特殊字符
        #         tEncode = chardet.detect(line)["encoding"]
        #         if tEncode == "GB2312":
        #             s = line.decode("gbk")
        #         elif len(tEncode) > 0:
        #             s = line.decode("utf8")
        #         # print(tEncode)
        #
        #         if len(self.textOut.GetValue()) > 0 :
        #             s = "\n" + s
        #         # self.textOut.AppendText(s)
        #         if len(s) > 0:
        #             wx.CallAfter(self.UpdateUI, UI="textOut", content=s)
        #         else:
        #             wx.CallAfter(self.UpdateUI, UI="textOut", content="*****")
        #         # sleep(0.1)
        #
        # return_code = p.returncode
        # p.terminate()
        # p.kill()
        # print(os.getcwd())  #获取操作所在路径
        # print(sys.path[0])
        # print(os.path.split(os.path.realpath(__file__))[0])
        # print(strCommand)  # 输出操作所执行命令
        print("操作返回错误代号：%d" % return_code)
        wx.CallAfter(self.UpdateUI, UI="textOut", content="\n操作返回代号：%d" % return_code)
        print("结束任务")

        wx.CallAfter(self.UpdateUI, UI="button", content="Enable")

        if return_code == 0:
            wx.CallAfter(self.UpdateUI, UI="textOut", content="\n操作完成")
            wx.CallAfter(self.UpdateUI, UI="ShowMessage", content="操作完成")
        else:
            wx.CallAfter(self.UpdateUI, UI="textOut", content="\n操作失败，错误码：%d"%return_code)
            wx.CallAfter(self.UpdateUI, UI="ShowMessage", content="操作失败，错误码：%d"%return_code)

    def UpdateUI(self, **kwargs):
        sUI = kwargs["UI"]
        s = kwargs["content"]
        if sUI == "textOut" :
            if s == True:
                self.textOut.Show(True)
            else:
                self.textOut.AppendText(s)
        elif sUI == "button":
            self.button.Enable()
            self.textCtrl.Enable()
        elif sUI == "ShowMessage":
            self.ShowMessage(s)

    def ShowMessage(self, content):
        wx.MessageBox(content, "提示", wx.OK | wx.ICON_INFORMATION)
        strPath = self.textCtrl.GetValue()
        self.textOut.Disable()
        if content == "操作失败" :
            excuPath = os.getcwd()
            strPath = os.path.join( excuPath, os.path.basename(strPath) )
            f = open(file=excuPath+"\\executePath.txt", mode='w', encoding="utf-8")
            f.write(excuPath)
            f.mode = "a"
            f.write("\n" + strPath)
            f.close()
        fileDir, fileName = os.path.split(strPath)
        path1 = os.path.join(fileDir, "__pycache__")
        path2 = os.path.join(fileDir, "build")
        path3 = os.path.join(fileDir, os.path.splitext(fileName)[0] + ".spec")
        path4 = os.path.join(fileDir, "dist", os.path.splitext(fileName)[0] + ".exe")
        MoveFile(path4, fileDir)
        path4 = os.path.join(fileDir, "dist")
        listPath = [path1, path2, path3, path4]
        for i in range(len(listPath)):
            path = listPath[i]
            DeleteFile(path)

    def OnClose(self, evt):
        ret = wx.MessageBox('Do you really want to leave?', '提示', wx.OK | wx.CANCEL)
        if ret == wx.OK:
            # do something here...
            if self.p != None and self.p.poll() == None :
                self.p.terminate()
                self.p.kill()
                print("终止shell进程")
                # exit(0)
                # self.t.setDaemon(True)
            evt.Skip()
        print("终止全部进程")
        # exit(0)


if __name__ == '__main__':
    app = wx.App()
    frame = ButtonFrame()
    frame.Show()
    app.MainLoop()