from abc import ABC, abstractmethod
from error import LargoExcedidoError, SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, new_ancho):
        self.__ancho = new_ancho if self.__ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, new_alto):
        self.__alto = new_alto if self.__alto > 0 else 1
        
    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, new_url_archivo):
        self.__url_archivo = new_url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, new_url_clic):
        self.__url_clic = new_url_clic

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, new_sub_tipo):
        if new_sub_tipo in self.SUBTIPOS:
            self.__sub_tipo = new_sub_tipo
        else:
            mensaje = ", ".join(self.SUBTIPOS)
            raise SubTipoInvalidoError(f"Error: ingresaste [ {new_sub_tipo} ] y solo se permiten [ {mensaje} ]")
                

    @abstractmethod
    def comprimir_anuncios():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass

    @staticmethod
    def mostrar_formatos(formato: str, subTipos: tuple):
        print(f"""
FORMATO {formato}
==========
- {subTipos[0]}
- {subTipos[1]}
""")
        

class Video(Anuncio):
    FORMATO = "Video"
    SUBTIPOS = ("instream", "outstream")

    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str, duracion:int):
        super().__init__(ancho, alto,url_archivo,url_clic, sub_tipo)
        self.__alto = 1
        self.__ancho = 1
        self.__duracion = duracion if duracion > 0 else 5
    
    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, new_ancho):
        pass

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, new_alto):
        pass

    def comprimir_anuncios(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATO = "Display"
    SUBTIPOS = ("tradicional", "native")
    
    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametros

    def comprimir_anuncios(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("Recorte de display no implementada aún")

class Social(Anuncio):
    FORMATO = "Social"
    SUBTIPOS = ("facebook", "linkedin")

    def __init__(self,ancho:int, alto:int,url_archivo:str, url_clic:str, sub_tipo:str):
        super().__init__(ancho, alto, url_archivo,url_clic, sub_tipo) #ejecutame el constructor del padre para definir todos estos parametro

    def comprimir_anuncios(self):
        print("Compresion de social no implementada aún")

    def redimensionar_anuncio(self):
        print("Recorte de social no implementada aún")