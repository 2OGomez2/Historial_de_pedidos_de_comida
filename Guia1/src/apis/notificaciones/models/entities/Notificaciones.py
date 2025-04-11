from utils.DateFormat import DateFormat


class Notificaciones:
    def __init__(self, id, id_cliente, fecha_envio, estado):
        self.id = id
        self.id_cliente = id_cliente
        self.fecha_envio = fecha_envio
        self.estado = estado

    def to_JSON(self):
        return {
            "id": self.id,
            "id_cliente": self.id_cliente,
            "fecha_envio": self.fecha_envio,
            "estado": self.estado
        }
