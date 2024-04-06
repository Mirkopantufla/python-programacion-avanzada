from anuncio import Video, Display, Social
from error import LargoExcedidoError
from datetime import datetime

class Campania():
    def __init__(self, nombre:str, fecha_inicio:datetime, fecha_termino:datetime, anuncios:list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        if len(new_nombre) >= 250:
            raise LargoExcedidoError(f"""Error: El largo no puede exceder los 250 caracteres, ingresaste un total de {len(new_nombre)} caracteres.""")
        else:
            self.__nombre = new_nombre
        
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, new_fecha_inicio):
        self.__fecha_inicio = new_fecha_inicio
        
    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, new_fecha_termino):
        self.__fecha_termino = new_fecha_termino

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        cant_video = 0
        cant_display = 0
        cant_social = 0
        #anuncios nos tra objetos de tipo [Video, Social, Video, Display]
        for elemento in self.__anuncios:
            if isinstance(elemento, Video):
                cant_video +=1
            elif isinstance(elemento, Display):
                cant_display+=1
            elif isinstance(elemento, Social):
                cant_social += 1
        # cant_video = len([elemento for elemento in self.anuncios if isinstance(elemento,Video)])    
        return f"""
        Nombre de la Campaña: {self.__nombre}
        Anuncios: {cant_video} Video, {cant_display} Display, {cant_social} Social
        """