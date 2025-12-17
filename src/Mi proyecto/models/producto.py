"""
Modulo de Modelos - Producto
Define las entidades principales del sistema
"""
from datetime import datetime
from enum import Enum

class Categoria(Enum):
    """
    Enumeracion de categorias de productos."""
    ELECTRONICA = "Electronica"
    ALIMENTOS = "Alimentos"
    ROPA = "Ropa"
    LIBROS = "Libros"
    OTROS = "Otros"
    
class Producto:
        """
        Represneta un producto en el inventario.
        
        Attributos:
            id_producto (int): Identificador unico 
            nombre (str:) Nombre del producto
            descripcion (str): descripcion dle producto
            precio (float): Precio unitario
            cantidad (init): cantidad ne stock
            categoria (categoria): Categoria del producto
            fecha_creacion (str): Fecha de creacion
        """
        _contador = 1000
        
        def __init__(self, nombre: str, descripcion: str, precio: float,    cantidad: int, categoria: Categoria):
            """
            Inicializa un producto.
            Args:
            nombre (str): Nombre del  producto
            descripcion (str): Descripcion del producto
            precio (float): Precio unitario
            cantidad (init): Cantidad en stock
            categoria: (Categoria): Categoria del producto
            """
            if not nombre or not nombre.strip():
                raise ValueError("El nombre no puede estar vacio")
            if precio < 0:
                raise ValueError("El precio  o puede ser negativo")
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            
            Producto._contador += 1
            self.id_producto = Producto._contador
            self.nombre = nombre.strip()
            self.descripcion = descripcion.strip()
            self.precio = precio
            self.cantidad = cantidad
            self.categoria = categoria
            self.categoria = categoria
            self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        def actualizar_cantidad(self, cantidad: int) -> bool:
            """Actualizar la cantidad de productos."""
            if cantidad < 0:
                raise ValueError("la cantidad no puede ser negativa")
            self.cantidad = cantidad
            return True
        
        def actualizar_precio(self, precio: float) -> bool:
            """Actualizar la cantidad del productos."""
            if precio < 0:
                raise ValueError("El precio no puede ser negativo")
            self.precio = precio
            return True
        
        def calcular_valor_total(self) -> float:
            """Calcular el valor total del producto en stock."""
            return self.precio * self.cantidad
        
        def _str_(self) -> str:
            """ Represnetacion en string del producto."""  
            return f"[{self.id_producto}] {self.nombre} - ${self.precio:.2f} (stock: {self.cantidad})"
        
        def _repr_(self) -> str: 
            """ Representacion en string del producto."""
            return f"producto(id={self.id_producto},nombre='{self.nombre}, precios={self.precio}, cantidad={self.cantidad})"
        
        