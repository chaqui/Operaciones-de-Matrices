#coding: utf-8
import wx
class ITraspuesta(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        self.b=False
        self.cadena=""
        wx.Frame.__init__(self, parent, title="Matriz Traspuesta"+" "+title, size=(800, 400))
        self.pos=0 
        self.size=20
        self.stCredito=wx.StaticText(self,label="------Matriz Traspuesta-------"+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=5
        #---------------Datos De las ecuaciones----------------s
        self.PCEcuaciones=wx.Panel(self,pos=(0,30),size=(800,200))
        #titulo de las ecuaciones
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Primera Fila:",pos=(5,self.pos),size=(150,self.size))
        #x1
        self.txtX1=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y1
        self.txtY1=wx.TextCtrl(self.PCEcuaciones,pos=(185,self.pos),size=(50,self.size),name="txty1",id=0)
        #z1
        self.txtZ1=wx.TextCtrl(self.PCEcuaciones,pos=(240,self.pos),size=(50,self.size),name="txtz1",id=0)
        #n1
        self.txtN1=wx.TextCtrl(self.PCEcuaciones,pos=(290,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        #titulo de las ecuaciones 2
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Segunda Fila:",pos=(5,self.pos),size=(150,self.size))
        #x2
        self.txtX2=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y2
        self.txtY2=wx.TextCtrl(self.PCEcuaciones,pos=(185,self.pos),size=(50,self.size),name="txtX1",id=0)
        #z2
        self.txtZ2=wx.TextCtrl(self.PCEcuaciones,pos=(240,self.pos),size=(50,self.size),name="txtX1",id=0)
        #n2
        self.txtN2=wx.TextCtrl(self.PCEcuaciones,pos=(290,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        #titulo de las ecuaciones
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Tercera Fila:",pos=(5,self.pos),size=(150,self.size))
        #x3
        self.txtX3=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y3
        self.txtY3=wx.TextCtrl(self.PCEcuaciones,pos=(185,self.pos),size=(50,self.size),name="txtX1",id=0)
        #z3
        self.txtZ3=wx.TextCtrl(self.PCEcuaciones,pos=(240,self.pos),size=(50,self.size),name="txtX1",id=0)
        #n3
        self.txtN3=wx.TextCtrl(self.PCEcuaciones,pos=(290,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        #titulo de las ecuaciones
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Cuarta Fila:",pos=(5,self.pos),size=(150,self.size))
        #x4
        self.txtX4=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(50,self.size),name="txtPEcuacion",id=0)
        #y4
        self.txtY4=wx.TextCtrl(self.PCEcuaciones,pos=(185,self.pos),size=(50,self.size),name="txtX1",id=0)
        #z4
        self.txtZ4=wx.TextCtrl(self.PCEcuaciones,pos=(240,self.pos),size=(50,self.size),name="txtX1",id=0)
        #n4
        self.txtN4=wx.TextCtrl(self.PCEcuaciones,pos=(290,self.pos),size=(50,self.size),name="txtz1",id=0)
        self.pos=self.pos+self.size
        #titulo de las ecuaciones
        self.stEcuacionq=wx.StaticText(self.PCEcuaciones,label="--------------------------------------------------Respuesta:--------------------------------------------------",pos=(5,self.pos),size=(800,self.size))
        self.pos=self.pos+self.size
        self.stX1=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(50,self.size))
        self.stY1=wx.StaticText(self.PCEcuaciones,label="",pos=(185,self.pos),size=(50,self.size))
        self.stZ1=wx.StaticText(self.PCEcuaciones,label="",pos=(240,self.pos),size=(50,self.size))
        self.stN1=wx.StaticText(self.PCEcuaciones,label="",pos=(290,self.pos),size=(50,self.size))
        self.pos=self.pos+self.size
        self.stX2=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(50,self.size))
        self.stY2=wx.StaticText(self.PCEcuaciones,label="",pos=(185,self.pos),size=(50,self.size))
        self.stZ2=wx.StaticText(self.PCEcuaciones,label="",pos=(240,self.pos),size=(50,self.size))
        self.stN2=wx.StaticText(self.PCEcuaciones,label="",pos=(290,self.pos),size=(50,self.size))
        self.pos=self.pos+self.size
        self.stX3=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(50,self.size))
        self.stY3=wx.StaticText(self.PCEcuaciones,label="",pos=(185,self.pos),size=(50,self.size))
        self.stZ3=wx.StaticText(self.PCEcuaciones,label="",pos=(240,self.pos),size=(50,self.size))
        self.stN3=wx.StaticText(self.PCEcuaciones,label="",pos=(290,self.pos),size=(50,self.size))
        self.pos=self.pos+self.size
        self.stX4=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(50,self.size))
        self.stY4=wx.StaticText(self.PCEcuaciones,label="",pos=(185,self.pos),size=(50,self.size))
        self.stZ4=wx.StaticText(self.PCEcuaciones,label="",pos=(240,self.pos),size=(50,self.size))
        self.stN4=wx.StaticText(self.PCEcuaciones,label="",pos=(290,self.pos),size=(50,self.size))
        self.txtX1.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtY1.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtZ1.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtN1.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtX2.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtY2.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtZ2.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtN2.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtX3.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtY3.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtZ3.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtN3.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtX4.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtY4.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtZ4.Bind(wx.EVT_KEY_UP, self.analizar)
        self.txtN4.Bind(wx.EVT_KEY_UP, self.analizar)
        self.Centre(True)  
        self.Show(True)
    def analizar(self,e):
        if self.buscar(self.txtX1.GetValue()):
            self.stX1.SetLabel(self.incluir(self.txtX1.GetValue()))
        else:
            self.txtX1.SetValue(self.cadena)
        if self.buscar(self.txtY1.GetValue()):
            self.stX2.SetLabel(self.incluir(self.txtY1.GetValue()))
        else:
            self.txtY1.SetValue(self.cadena)
        if self.buscar(self.txtZ1.GetValue()):
            self.stX3.SetLabel(self.incluir(self.txtZ1.GetValue()))
        else:
            self.txtZ1.SetValue(self.cadena)
        if self.buscar(self.txtN1.GetValue()):
            self.stX4.SetLabel(self.incluir(self.txtN1.GetValue()))
        else:
            self.txtN1.SetValue(self.cadena)
        ################################################################
        #································2····························
        if self.buscar(self.txtX2.GetValue()):
            self.stY1.SetLabel(self.incluir(self.txtX2.GetValue()))
        else:
            self.txtX2.SetValue(self.cadena)
        if self.buscar(self.txtY2.GetValue()):
            self.stY2.SetLabel(self.incluir(self.txtY2.GetValue()))
        else:
            self.txtY2.SetValue(self.cadena)
        if self.buscar(self.txtZ2.GetValue()):
            self.stY3.SetLabel(self.incluir(self.txtZ2.GetValue()))
        else:
            self.txtZ2.SetValue(self.cadena)
        if self.buscar(self.txtN2.GetValue()):
            self.stY4.SetLabel(self.incluir(self.txtN2.GetValue()))
        else:
            self.txtN2.SetValue(self.cadena)
        ################################################################
        #··························3·····················3
        if self.buscar(self.txtX3.GetValue()):
            self.stZ1.SetLabel(self.incluir(self.txtX3.GetValue()))
        else:
            self.txtX3.SetValue(self.cadena)
        if self.buscar(self.txtY3.GetValue()):
            self.stZ2.SetLabel(self.incluir(self.txtY3.GetValue()))
        else:
            self.txtY3.SetValue(self.cadena)
        if self.buscar(self.txtZ3.GetValue()):
            self.stZ3.SetLabel(self.incluir(self.txtZ3.GetValue()))
        else:
            self.txtZ3.SetValue(self.cadena)
        if self.buscar(self.txtN3.GetValue()):
            self.stZ4.SetLabel(self.incluir(self.txtN3.GetValue()))
        else:
            self.txtN3.SetValue(self.cadena)
        ################################################################
        #··························4·····················3
        if self.buscar(self.txtX4.GetValue()):
            self.stN1.SetLabel(self.incluir(self.txtX4.GetValue()))
        else:
            self.txtX4.SetValue(self.cadena)
        if self.buscar(self.txtY4.GetValue()):
            self.stN2.SetLabel(self.incluir(self.txtY4.GetValue()))
        else:
            self.txtY4.SetValue(self.cadena)
        if self.buscar(self.txtZ4.GetValue()):
            self.stN3.SetLabel(self.incluir(self.txtZ4.GetValue()))
        else:
            self.txtZ4.SetValue(self.cadena)
        if self.buscar(self.txtN4.GetValue()):
            self.stN4.SetLabel(self.incluir(self.txtN4.GetValue()))
        else:
            self.txtN4.SetValue(self.cadena)
    def incluir(self,a):
        if a!="":
            return a
        else:
            return "0"
    def buscar(self,q):
        b=True
        noAceptadas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        cad1=list(q)
        try:
            if cad1[-1] in noAceptadas :
                print cad1
                del cad1[-1]
                self.cadena="".join(cad1)
                return False
            else:
                return True
        except Exception, e:
            cad1=[]
