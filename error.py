class LargoExcedidoError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class SubTipoInvalidoError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje