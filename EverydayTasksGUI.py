# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:55:43 2019

@author: Umaima
"""

import wx
from os import system
import wx.grid as gridlib
import json
import time

#--------Amazon product display frame------------------
class AmazonData(wx.Frame):
    
    #----------------------------------------------------------------------
    def __init__(self, parent, title):
         
        super(AmazonData, self).__init__(parent, title=title)
        panel = wx.Panel(self)
 
        myGrid = gridlib.Grid(panel)
        myGrid.CreateGrid(5, 6)
        
        myGrid.SetColLabelValue(0, "NAME")
        myGrid.SetColLabelValue(1, "SALE_PRICE")
        myGrid.SetColLabelValue(2, "CATEGORY")
        myGrid.SetColLabelValue(3, "ORIGINAL_PRICE")
        myGrid.SetColLabelValue(4, "AVAILABILITY")
        myGrid.SetColLabelValue(5, "URL")
        
        with open("amazondata.json", "r") as read_file:
            data = json.load(read_file)
            
        for i in range(0, 5):
            myGrid.SetCellValue(i,0, data[i]["NAME"])
            myGrid.SetCellValue(i,1, data[i]["SALE_PRICE"])
            myGrid.SetCellValue(i,2, data[i]["CATEGORY"])
            myGrid.SetCellValue(i,3, data[i]["ORIGINAL_PRICE"])
            myGrid.SetCellValue(i,4, data[i]["AVAILABILITY"])
            myGrid.SetCellValue(i,5, data[i]["URL"])
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, wx.ALL|wx.EXPAND)
        panel.SetSizer(sizer)
        #sizer.Fit(self)
        
#-------Main Frame------------------------------------------
class EverydayTasks(wx.Frame):

    def __init__(self, parent, title):
        super(EverydayTasks, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
    
    def InitUI(self):

        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('images\everyday01.png'))
        sizer.Add(icon, pos=(0, 0), flag=wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
            border=5)
        
        text1 = wx.StaticText(panel, label="Everyday Task Automation")
        font1 = wx.Font(18, wx.DECORATIVE, wx.SLANT , wx.BOLD)
        text1.SetFont(font1)
        
        sizer.Add(text1, pos=(0, 1), flag=wx.TOP|wx.RIGHT|wx.BOTTOM,
            border=15)
        
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)
        
        font2 = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        
        text2 = wx.StaticText(panel, label="Check new mails in Inbox")
        text2.SetFont(font2)
        sizer.Add(text2, pos=(2, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)
        
        
        #button3 = wx.Button(panel, label='Gmail')
        sBitMap1 = wx.StaticBitmap(panel, bitmap=wx.Bitmap('images\\gmail.png'))
        sBitMap1.Bind(wx.EVT_LEFT_DOWN, self.onclickGmail)
        sizer.Add(sBitMap1, pos=(2, 1), flag=wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT|wx.BOTTOM, border=10)

        text3 = wx.StaticText(panel, label="Check price drop over products")
        text3.SetFont(font2)
        sizer.Add(text3, pos=(3, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)
        
        sBitMap2 = wx.StaticBitmap(panel, -1, wx.Bitmap("images\\amazon.png", wx.BITMAP_TYPE_ANY))
        sBitMap2.Bind(wx.EVT_LEFT_DOWN, self.onclickAmazon)
        sizer.Add(sBitMap2, pos=(3, 1), flag=wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT|wx.BOTTOM, border=10)

        text4 = wx.StaticText(panel, label="Send birthday greetings to friends")
        text4.SetFont(font2)
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)
        
        sBitMap3 = wx.StaticBitmap(panel, -1, wx.Bitmap("images\\facebook.png", wx.BITMAP_TYPE_ANY))
        sBitMap3.Bind(wx.EVT_LEFT_DOWN, self.onclickFacebook)
        sizer.Add(sBitMap3, pos=(4, 1), flag=wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.LEFT|wx.BOTTOM, border=10)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)
        
    def onclickGmail(self, event):
        
        print("Gmail automation")
        system("python GmailBot.py 1")
        time.sleep(5)
        
        
    def onclickAmazon(self, event):
        
        print("Amazon automation")
        system("python AmazonBot.py 1")
        table = AmazonData(None, title="Amazon Product Details")
        table.Show()
        
    def onclickFacebook(self, event):
        
        print("Facebook automation")
        system("python FacebookBot.py 1")
        
def main():

    app = wx.App()
    ex = EverydayTasks(None, title="Automation")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()