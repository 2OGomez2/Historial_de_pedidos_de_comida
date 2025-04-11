from utils.DateFormat import DateFormat


class Productos:
    def __init__(self, id_producto, id_categoria, nombre_producto, descripcion, precio, disponible):
        self.id_producto = id_producto
        self.id_categoria = id_categoria
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.disponible = disponible

    def to_JSON(self):
        return {
            "id_producto": self.id_producto,
            "id_categoria": self.id_categoria,
            "nombre_producto": self.nombre_producto,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "disponible": self.disponible
        }