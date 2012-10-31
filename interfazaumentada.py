'''
Created on 9/07/2012

@author: josuechaqui
'''
#coding: utf-8
import wx
class IAumentada(wx.Frame):

    def __init__(self,parent,title):
        #Hipoteca Real
        self.b=False
        wx.Frame.__init__(self, parent, title="Matriz Aumentada"+" "+title, size=(800, 400))
        self.pos=0
        self.size=20
        self.stCredito=wx.StaticText(self,label="------Matriz Aumentada------- 	"+" "+title,pos=(5,self.pos+10),size=(200,self.size))
        self.pos=5
        #---------------Datos De las ecuaciones----------------s
        self.PCEcuaciones=wx.Panel(self,pos=(0,30),size=(800,200))
        #titulo de las ecuaciones
        self.stEcuacion=wx.StaticText(self.PCEcuaciones,label="Ecuaciones:",pos=(5,self.pos),size=(150,self.size))
        self.stNombreCliente=wx.StaticText(self.PCEcuaciones,label="(de la forma ax+by+cz=d)",pos=(131,self.pos),size=(250,self.size))
        #primera ecuacion
        self.pos=self.pos+self.size
        self.stPEcuacion=wx.StaticText(self.PCEcuaciones,label="Primera Ecuacion:",pos=(5,self.pos),size=(150,self.size))
        self.txtPEcuacion=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(350,self.size),name="txtPEcuacion",id=0)
        #segunda ecuacion
        self.pos=self.pos+self.size
        self.stSEcuaciones=wx.StaticText(self.PCEcuaciones,label="Segunda Ecuacion:",pos=(2,self.pos),size=(150,self.size))
        self.txtSEcuaciones=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(350,self.size),name="txtSEcuaciones",id=0)
        #tercera ecuacion
        self.pos=self.pos+self.size
        self.stTEcuaciones=wx.StaticText(self.PCEcuaciones,label="Tercera Ecuacion:",pos=(2,self.pos),size=(150,self.size))
        self.txtTEcuaciones=wx.TextCtrl(self.PCEcuaciones,pos=(131,self.pos),size=(350,self.size),name="txtTEcuaciones",id=0)
        self.pos=self.pos+self.size
        #resultado primera ecuacion
        self.stREcuacion1=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(150,self.size))
        self.pos=self.pos+self.size
        #resultado segunda ecuacion
        self.stREcuacion2=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(150,self.size))
        self.pos=self.pos+self.size
        #resultado tercera ecuacion
        self.stREcuacion3=wx.StaticText(self.PCEcuaciones,label="",pos=(131,self.pos),size=(150,self.size))
        self.txtPEcuacion.Bind(wx.EVT_KEY_UP, self.analizarPEcuacion)
        self.txtSEcuaciones.Bind(wx.EVT_KEY_UP, self.analizarSEcuacion)
        self.txtTEcuaciones.Bind(wx.EVT_KEY_UP, self.analizarTEcuacion)
        self.Centre(True)  # Centrar la ventana en pantalla
        self.Show(True)
    def analizarPEcuacion(self,e):
        noAceptadas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
        cad1=list(self.txtPEcuacion.GetValue())
        try:
            if cad1[-1] in noAceptadas :
                print cad1
                del cad1[-1]
                cadena="".join(cad1)
                self.txtPEcuacion.SetValue(cadena)
            else:
                self.stREcuacion1.SetLabel(str(self.analizar(cad1,True)))
            if self.txtSEcuaciones.GetValue() != "":
                self.stREcuacion2.SetLabel(str(self.analizar(list(self.txtSEcuaciones.GetValue()),False)))
            if self.txtTEcuaciones.GetValue() != "":
                self.stREcuacion3.SetLabel(str(self.analizar(list(self.txtTEcuaciones.GetValue()),False)))
        except Exception, e:
            cad1=[]
            self.stREcuacion1.SetLabel("")
    def analizarSEcuacion(self,e):
        noAceptadas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
        cad1=list(self.txtSEcuaciones.GetValue())
        try:
            if cad1[-1] in noAceptadas :
                print cad1
                del cad1[-1]
                cadena="".join(cad1)
                self.txtSEcuaciones.SetValue(cadena)
            else:
                self.stREcuacion2.SetLabel(str(self.analizar(cad1,False)))
        except Exception, e:
            cad1=[]
            self.stREcuacion2.SetLabel("")
    def analizarTEcuacion(self,e):
        noAceptadas=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
        cad1=list(self.txtTEcuaciones.GetValue())
        try:
            if cad1[-1] in noAceptadas :
                print cad1
                del cad1[-1]
                cadena="".join(cad1)
                self.txtTEcuaciones.SetValue(cadena)
            else:
                self.stREcuacion3.SetLabel(str(self.analizar(cad1,False)))
        except Exception, e:
            cad1=[]
            self.stREcuacion3.SetLabel("")
    def analizar(self,lista,k):
        print lista
        x=0
        y=0
        z=0
        n=0
        nb=False
        ns=""
        self.fila=[]
        matrizr=[]
        for i in xrange(0,3):
            x=0
            y=0
            z=0
            n=0
            ns=""
            nb=False
            self.fila=[]
            cad=lista
            for letra in cad:
                if nb==False:
                    if letra=="x":
                        if ns=="+":
                            x=x+1
                        elif ns=="-":
                            x=x-1
                        elif ns=="":
                            x=x+1
                        else:
                            x=x+float(ns)
                        ns=""
                    elif letra =="y":
                        if ns=="+":
                            y=y+1
                        elif ns=="-":
                            y=y-1
                        elif ns=="":
                            y=y+1
                        else:
                            y=y+float(ns)
                        ns=""
                    elif letra =="z":
                        if ns=="+":
                            z=z+1
                        elif ns=="-":
                            z=z-1
                        elif ns=="":
                            z=z+1
                        else:
                            z=z+float(ns)
                        ns=""
                    elif letra=="=":
                        nb=True
                        ns=""
                    else:
                        ns=ns+letra
                else:
                    ns=ns+letra
        n=float(ns)
        self.fila.append(x)
        self.fila.append(y)
        if z != 0:
            if k==True:
                self.fila.append(z)
                self.b=True
            elif self.b:
                self.fila.append(z)
        else:
            if k==True:
                self.b=False
            elif self.b:
                self.fila.append(z)
        self.fila.append(n)
        matrizr.append(self.fila)
        print "la Matriz Aumentada es la siguiente:"
        for x in matrizr:
            print x
        return matrizr
app = wx.App(False)
APP_TITLE=" --Python--"
frame = IAumentada(None,APP_TITLE)
app.MainLoop()