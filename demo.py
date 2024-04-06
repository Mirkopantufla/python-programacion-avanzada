from anuncio import Video
from campania import Campania
from datetime import datetime, timedelta

new_video = [Video(640, 480, "video.mp4", "http://example.com", "asd", 60),]

f_inicio = datetime.now()
f_termino = f_inicio + timedelta(days=2)
new_campania = Campania("Campaña1", f_inicio, f_termino, new_video)

try:
    nuevo_nombre = input(f"""
Ingrese un nuevo nombre para la campaña:
> """)
    new_campania.nombre = nuevo_nombre
    nuevo_subTipo = input(f"""
Ingrese un nuevo subtipo para el anuncio:
> """)

    new_campania.anuncios[0].sub_tipo = nuevo_subTipo

except Exception as e:
    #Al haber un error, se escribe en error.log
    with open("error.log", "a+") as log:
        #Escribe dentro del archivo, el mensaje
        log.write(f"{e}\n")