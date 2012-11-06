import wx
from interfazSistema2x2 import ISistema2
from interfazSistema3x3 import ISistema3
class IMenuS(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        self.b=False
        self.cadena=""
        wx.Frame.__init__(self, parent, title="Menu"+" "+title, size=(400, 400))
        self.pos=0 
        self.size=35
        self.stCredito=wx.StaticText(self,label="------Sistemas de Ecuaciones-------"+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=self.pos+self.size+self.size
        self.pos2=5
        self.btInversa=wx.Button(self,pos=(100,self.pos),size=(200,self.size),name="txtz1",id=0,label="Sistema 3x3")
        self.pos=self.pos+self.size
        self.btAumentada=wx.Button(self,pos=(100,self.pos),size=(200,self.size),name="txtz1",id=0,label="Sistema 2x2")
        self.btInversa.Bind (wx.EVT_BUTTON, self.sistematres)
        self.btAumentada.Bind (wx.EVT_BUTTON, self.sistemados)
        self.Centre(True)  
        self.Show(True)
    def sistematres(self,e):
    	app = wx.App(False)
    	APP_TITLE=" --Python--"
    	frame = ISistema3(None,APP_TITLE)
    	app.MainLoop()
    def sistemados(self,e):
    	app = wx.App(False)
    	APP_TITLE=" --Python--"
    	frame = ISistema2(None,APP_TITLE)
    	app.MainLoop()


