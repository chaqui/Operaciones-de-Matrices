import wx
from interfazaumentada import IAumentada
from interfazinversa import Iinversa
from interfazTraspuesta import ITraspuesta
from menusistemas import IMenuS
class IMenu(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        self.b=False
        self.cadena=""
        wx.Frame.__init__(self, parent, title="Menu"+" "+title, size=(400, 400))
        self.pos=0 
        self.size=35
        self.stCredito=wx.StaticText(self,label="------Algebra linear-------",pos=(5,self.pos+10),size=(200,self.size))
        self.pos=self.pos+self.size+self.size
        self.pos2=5
        self.btInversa=wx.Button(self,pos=(100,self.pos),size=(200,self.size),name="txtz1",id=0,label="Matriz Inversa")
        self.pos=self.pos+self.size
        self.btAumentada=wx.Button(self,pos=(100,self.pos),size=(200,self.size),name="txtz1",id=0,label="Matriz Aumentada")
        self.pos=self.pos+self.size
        self.btTraspuesta=wx.Button(self,pos=(100,self.pos),size=(200,self.size),name="txtz1",id=0,label="Matriz Traspuesta")
        self.pos=self.pos+self.size
        self.btres=wx.Button(self,pos=(100,self.pos),size=(200,self.size),name="txtz1",id=0,label="Resolucion de Sistema")
        self.pos=self.pos+self.size+self.size
        self.stCredito=wx.StaticText(self,label="Programa hecho en Python \n Josue Fuentes \n Marlon Orozco \n Gerardo Davila",pos=(5,self.pos+10),size=(200,self.size))
        #titulo de las ecuaciones
        self.btInversa.Bind (wx.EVT_BUTTON, self.MInversa)
        self.btAumentada.Bind (wx.EVT_BUTTON, self.MIAumentada)
        self.btTraspuesta.Bind (wx.EVT_BUTTON, self.MITraspuesta)
        self.btres.Bind (wx.EVT_BUTTON, self.Menu)
        self.Centre(True)  
        self.Show(True)
    def MInversa(self,e):
        app = wx.App(False)
        APP_TITLE=" --Python--"
        frame = Iinversa(None,APP_TITLE)
        app.MainLoop()
    def MIAumentada(self,e):
        app = wx.App(False)
        APP_TITLE=" --Python--"
        frame = IAumentada(None,APP_TITLE)
        app.MainLoop()
    def MITraspuesta(self,e):
        app = wx.App(False)
        APP_TITLE=" --Python--"
        frame = ITraspuesta(None,APP_TITLE)
        app.MainLoop()
    def Menu(self,e):
        app = wx.App(False)
        APP_TITLE=" --Python--"
        frame = IMenuS(None,APP_TITLE)
        app.MainLoop()
        
if __name__ == '__main__':
    app = wx.App(False)
    APP_TITLE=" --Python--"
    frame = IMenu(None,APP_TITLE)
    app.MainLoop()
