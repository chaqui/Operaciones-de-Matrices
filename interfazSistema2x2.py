#coding: utf-8
import wx
from Sistema2x2 import Sistema2x2
class ISistema2(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        self.b=False
        self.cadena=""
        wx.Frame.__init__(self, parent, title="Sistema 2x2"+" "+title, size=(800, 400))
        self.pos=0 
        self.size=20
        self.stCredito=wx.StaticText(self,label="-----Sistema2x2-------"+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=5
        #---------------Datos De las ecuaciones----------------s
        self.PCEcuaciones=wx.Panel(self,pos=(0,30),size=(800,200))
        #titulo de las ecuaciones
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Primera Ecuacion:",pos=(5,self.pos),size=(150,self.size))
        #x1
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="X1:",pos=(160,self.pos),size=(30,self.size))
        self.txtX1=wx.TextCtrl(self.PCEcuaciones,pos=(190,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y1
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Y1:",pos=(245,self.pos),size=(30,self.size))
        self.txtY1=wx.TextCtrl(self.PCEcuaciones,pos=(280,self.pos),size=(50,self.size),name="txty1",id=0)
        #n1
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="N1:",pos=(330,self.pos),size=(30,self.size))
        self.txtN1=wx.TextCtrl(self.PCEcuaciones,pos=(370,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        #titulo de las ecuaciones 2
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Segunda Ecuacion:",pos=(5,self.pos),size=(150,self.size))
        #x1
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="X2:",pos=(160,self.pos),size=(30,self.size))
        self.txtX2=wx.TextCtrl(self.PCEcuaciones,pos=(190,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y1
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Y2:",pos=(245,self.pos),size=(30,self.size))
        self.txtY2=wx.TextCtrl(self.PCEcuaciones,pos=(280,self.pos),size=(50,self.size),name="txty1",id=0)
        #n1
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="N2:",pos=(330,self.pos),size=(30,self.size))
        self.txtN2=wx.TextCtrl(self.PCEcuaciones,pos=(370,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        self.btAceptar=wx.Button(self.PCEcuaciones,pos=(50,self.pos),size=(90,self.size),name="txtz1",id=0,label="Analizar")
        self.pos=self.pos+self.size
        self.stEcuacionq=wx.StaticText(self.PCEcuaciones,label="--------------------------------------------------Respuesta:--------------------------------------------------",pos=(5,self.pos),size=(800,self.size))
        self.pos=self.pos+self.size
        self.stX1=wx.StaticText(self.PCEcuaciones,label="X:",pos=(131,self.pos),size=(30,self.size))
        self.stX=wx.StaticText(self.PCEcuaciones,label="",pos=(161,self.pos),size=(30,self.size))
        self.stY1=wx.StaticText(self.PCEcuaciones,label="Y:",pos=(191,self.pos),size=(30,self.size))
        self.stY=wx.StaticText(self.PCEcuaciones,label="",pos=(221,self.pos),size=(30,self.size))
        self.btAceptar.Bind (wx.EVT_BUTTON, self.ResolverS)
        self.Centre(True)  
        self.Show(True)
    def pedirMatriz(self):
        self.fila=[]
        self.matriz=[]
        self.fila.append(int(self.txtX1.GetValue()))
        self.fila.append(int(self.txtY1.GetValue()))
        self.fila.append(int(self.txtN1.GetValue()))
        self.matriz.append(self.fila)
        self.fila=[]
        self.fila.append(int(self.txtX2.GetValue()))
        self.fila.append(int(self.txtY2.GetValue()))
        self.fila.append(int(self.txtN2.GetValue()))
        self.matriz.append(self.fila)
        self.fila=[]
    def ResolverS(self,e):
        s3= Sistema2x2()
        self.pedirMatriz()
        r=s3.calcular(self.matriz)
        if r==0:
             wx.MessageBox('No tiene respuesta', 'Error!!!', wx.OK | wx.ICON_INFORMATION)
        else:
            print r
            self.stX.SetLabel(str(r[0]))
            self.stY.SetLabel(str(r[1]))
app = wx.App(False)
APP_TITLE=" --Python--"
frame = ISistema2(None,APP_TITLE)
app.MainLoop()