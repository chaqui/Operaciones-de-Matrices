#coding: utf-8
import wx
from matrizInversa import MatrizInversa
class Iinversa(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        self.b=False
        self.cadena=""
        wx.Frame.__init__(self, parent, title="Matriz Inversa"+" "+title, size=(800, 400))
        self.pos=0 
        self.size=20
        self.stCredito=wx.StaticText(self,label="------Matriz Inversa 3 x 3-------"+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=5
        self.pos2=5
        #---------------Datos De las ecuaciones----------------s
        self.PCEcuaciones=wx.Panel(self,pos=(0,30),size=(800,200))
        #titulo de las ecuaciones 
        self.pos2=5
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Primera Fila:",pos=(self.pos2,self.pos),size=(150,self.size))
        #x1
        self.pos2=155
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna1:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stP1=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y1
        self.pos2+=50
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna2:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stP2=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txty1",id=0)
        #z1
        self.pos2+=50
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna3:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stP3=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        ###########################################################################################
        #titulo de las ecuaciones 2
        self.pos2=5
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Segunda Fila:",pos=(self.pos2,self.pos),size=(150,self.size))
        #x1
        self.pos2=155
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna1:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stS1=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y1
        self.pos2+=50
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna2:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stS2=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txty1",id=0)
        #z1
        self.pos2+=50
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna3:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stS3=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
         ###########################################################################################
        #titulo de las ecuaciones 3
        self.pos2=5
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Tercera Fila:",pos=(self.pos2,self.pos),size=(150,self.size))
        #x1
        self.pos2=155
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna1:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stT1=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y1
        self.pos2+=50
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna2:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stT2=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txty1",id=0)
        #z1
        self.pos2+=50
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Columna3:",pos=(self.pos2,self.pos),size=(70,self.size))
        self.pos2+=70
        self.stT3=wx.TextCtrl(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        self.pos2=55
        self.btAceptar=wx.Button(self.PCEcuaciones,pos=(self.pos2,self.pos),size=(90,self.size),name="txtz1",id=0,label="Analizar")
        #titulo de las ecuaciones
        self.pos=self.pos+self.size
        self.stEcuacionq=wx.StaticText(self.PCEcuaciones,label="--------------------------------------------------Respuesta:--------------------------------------------------",pos=(5,self.pos),size=(800,self.size))
        self.pos=self.pos+self.size
        self.stX1=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(100,self.size))
        self.stY1=wx.StaticText(self.PCEcuaciones,label="",pos=(270,self.pos),size=(100,self.size))
        self.stZ1=wx.StaticText(self.PCEcuaciones,label="",pos=(400,self.pos),size=(100,self.size))
        self.pos=self.pos+self.size
        self.stX2=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(100,self.size))
        self.stY2=wx.StaticText(self.PCEcuaciones,label="",pos=(270,self.pos),size=(100,self.size))
        self.stZ2=wx.StaticText(self.PCEcuaciones,label="",pos=(400,self.pos),size=(100,self.size))
        self.pos=self.pos+self.size
        self.stX3=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(100,self.size))
        self.stY3=wx.StaticText(self.PCEcuaciones,label="",pos=(270,self.pos),size=(100,self.size))
        self.stZ3=wx.StaticText(self.PCEcuaciones,label="",pos=(400,self.pos),size=(100,self.size))
        self.btAceptar.Bind (wx.EVT_BUTTON, self.ResolverM)
        self.Centre(True)  
        self.Show(True)
    def pedirMatriz(self):
    	self.fila=[]
    	self.matriz=[]
    	self.fila.append(int(self.stP1.GetValue()))
    	self.fila.append(int(self.stP2.GetValue()))
    	self.fila.append(int(self.stP3.GetValue()))
    	self.matriz.append(self.fila)
    	self.fila=[]
    	self.fila.append(int(self.stS1.GetValue()))
    	self.fila.append(int(self.stS2.GetValue()))
    	self.fila.append(int(self.stS3.GetValue()))
    	self.matriz.append(self.fila)
    	self.fila=[]
    	self.fila.append(int(self.stT1.GetValue()))
    	self.fila.append(int(self.stT2.GetValue()))
    	self.fila.append(int(self.stT3.GetValue()))
    	self.matriz.append(self.fila)
    	self.fila=[]
    def ResolverM(self,e):
        self.pedirMatriz()
        self.resM=MatrizInversa()
        self.resp=self.resM.calcularM(self.matriz)
        print "a"
        print self.resp
        if self.resp==[]:
            wx.MessageBox('No tiene respuesta', 'Error!!!', wx.OK | wx.ICON_INFORMATION)
        else:
            self.stX1.SetLabel(str(self.resp[0][0]))
            self.stY1.SetLabel(str(self.resp[0][1]))
            self.stZ1.SetLabel(str(self.resp[0][2]))
            self.stX2.SetLabel(str(self.resp[1][0]))
            self.stY2.SetLabel(str(self.resp[1][1]))
            self.stZ2.SetLabel(str(self.resp[1][2]))
            self.stX3.SetLabel(str(self.resp[0][0]))
            self.stY3.SetLabel(str(self.resp[0][1]))
            self.stZ3.SetLabel(str(self.resp[0][2]))