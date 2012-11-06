from distutils.core import setup

setup(name="Resolucion de programas de algebra",
      version="0.1",
      description="Programa hecho en python para algebra lineal",
      author="@josuecha",
      author_email="josue.chaqui@gmail.com",
      license="GPL",
      scripts=["menu.py"],
      py_modules=["interfazSistema2x2","interfazSistema3x3","interfazTraspuesta","matrizInversa","menusistemas","Sistema3x3","interfazaumentada","interfazSistema2x2"]

)