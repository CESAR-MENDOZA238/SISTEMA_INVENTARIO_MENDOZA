
"""
    Módulo de Utilidades - Formateadores
    Define funciones para formatear y presentar datos
"""

from typing import List, Dict, Any
from ..models.producto import Producto

class Formateadores:
    """Clase con métodos estáticos para formatear datos."""
    
    @staticmethod
    def formatear_precio(precio: float) -> str:
        """Formatea precio con símbolo de moneda."""
        return f"${precio:.2f}"
    
    @staticmethod
    def formatear_producto_tabla(producto: Producto) -> str:
        """Formatea producto para visualización en tabla."""
        return (f"| {producto.id_producto:>3} | {producto.nombre:<20} | "
                f"{producto.descripcion:<20} | {producto.precio:>8.2f} |  "
                f"{producto.cantidad:>5} | {producto.calcular_valor_total():>11.2f} |")
    
    @staticmethod
    def formatear_lista_productos(productos: List[Producto]) -> str:
        """Formatea lista de productos para mostrar"""
        if not productos:
            return "No hay productos para mostrar"
        
        encabezado = "|  ID  | Nombre   | Descripcion                                | Precio | Stock | Valor Total |"
        separador = "-" * 80
        filas = [Formateadores.formatear_producto_tabla(p) for p in productos]
        
        return f"{(separador)}\n{(encabezado)}\n{(separador)}\n" + "\n".join(filas) + f"\n{(separador)}"
    
    @staticmethod
    def formatear_reporte(reporte: Dict[str, Any]) -> str:
        """Formatea reporte para visualización"""
        output = "\n" + "=" * 60 + "\n"
        output += "           REPORTE DE INVENTARIO\n"
        output += "=" * 60 + "\n"
        output += f"Fecha: {reporte['fecha_generacion']}\n\n"
        output += f"Total de Productos: {reporte['total_productos']}\n"
        output += f"Total de Ítems en Stock: {reporte['total_items']}\n"
        output += f"Valor Total del Inventario: {reporte['valor_total']:.2f}\n\n"
        
        if reporte['producto_mas_caro']:
            output += f"Producto Más Caro: {reporte['producto_mas_caro'].nombre} "
            output += f"(${reporte['producto_mas_caro'].precio:.2f})\n"
        
        if reporte['producto_mas_barato']:
            output += f"Producto Más Barato: {reporte['producto_mas_barato'].nombre}"
            output += f" (${reporte['producto_mas_barato'].precio:.2f})\n"
        
        output += f"\nProductos Bajo Stock: ({len(reporte['productos_bajo_stock'])})\n"
        output += "=" * 60 + "\n"
        
        return output