"""
Sistema de Gestion de Inventario - Interfaz Principal
Aplicación interactiva para gestionar productos
"""


from src.mi_proyecto.models.producto import Categoria, Producto
from src.mi_proyecto.repositories.inventario import RepositorioMemoria, Inventario
from src.mi_proyecto.services.reportes import GeneradorReportes
from src.mi_proyecto.utils.validadores import Validadores
from src.mi_proyecto.utils.formatters import Formateadores


class AplicacionInventario:
    """Aplicacion principal con interfaz de usuario."""
    
    def __init__(self):
        """Inicializa la aplicación."""
        self.repository = RepositorioMemoria() 
        self.inventario = Inventario(self.repository)
        self.reportes = GeneradorReportes(self.inventario)
        
    def mostrar_menu_principal(self) ->  str:
        """ Muestra el menu principal."""
        print("\n" + "=" * 50)
        print(".....SISTEMA DE GESTION DE INVENTARIO")
        print("=" * 50)
        print("1. Agregar producto")
        print("2. Ver todos los productos")
        print("3. Aumentar stock")
        print("4. Disminuir stock (Venta)")
        print("5. Productos con bajo stock")
        print("6. Ver reporte completo")
        print("7. Salir")
        print("=" * 50)
        
        return input("Seleccione una opcion: ")
    
    def agregar_producto_interactivo(self):
        """Permite agregar un producto de forma interativa."""
        try:
            print("\n--- AGREGAR NUEVO PRODUCTO ---")
            nombre = input("Nombre del producto: ")
            Validadores.validar_nombre_no_vacio(nombre)
            
            descripcion = input("descripcion:") 
               
            precio = float(input("Precio: $"))
            Validadores.validar_precio_positivo(precio)
            
            cantidad = int(input("Cantidad inicial: "))
            Validadores.validar_cantidad_no_negativa(cantidad)
            
            print("\nCategorias disponibles: ")
            for cat in Categoria:
                print(f"...{cat.value}")
                
                cat_str = input("Categoria: ")
                categoria = Categoria[cat_str.upper().replace(" ", "_")]
                
                producto = self.inventario.agregar_producto(nombre, descripcion, precio, cantidad, categoria)
                print(f"\nOK - Producton agregado: {producto}")
                
        except (ValueError, KeyError) as e:
            print(f"\nERROR: {e}")
            
    def ver_todos_productos(self):
        """Muestra todos los productos."""
        productos = self.repository.obtener_todos()
        print(Formateadores.formatear_lista_productos(productos))
        
    def aumentar_stock_interactivo(self):
        """Aumenta el stock de un producto."""
        try:
            id_prod = int(input("\nID del producto: "))
            cantidad = int(input("CANTIDAD A AUMENTAR: "))
            
            self.inventario.aumentar_stock(id_prod, cantidad)
            print("OK - Stock aumentado exitosamente")
            
        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")
            
    def disminuir_stock_interactivo(self):
        """Disminuir el stock de un producto (simula venta)""" 
        try:
            id_prod = int(input("\nID del producto: ")) 
            cantidad =  int(input("Cantidad vendida"))
            
            self.inventario.disminuir_stock(id_prod, cantidad)
            print("OK - Venta registrada exitosamente")  
            
        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")            
            
    def ver_bajo_stock(self):
        """Muestra productos con bajo stock"""
        limite = int(input("\nlimite de stock bajo (ddefoult 10): ") or "10")
        productos = self.inventario.obtener_productos_bajo_stock(limite)
        print(Formateadores.formatear_lista_productos(productos))
        
    def ver_reporte(self):
        """MUESTRA EL REPORTE COMPLETO""" 
        reporte = self.reportes.reporte_completo()
        print(Formateadores.formatear_reporte(reporte))
        
    def ejecutar(self):
        """Ejecuta la aplicacion principal"""
        self._cargar_datos_prueba()
        
        while True:
            opcion  = self.mostrar_menu_principal()
            
            if opcion == "1":
                self.agregar_producto_interactivo()
            elif opcion == "2":
                self.ver_todos_productos()
            elif opcion == "3":
                self.aumentar_stock_interactivo()
            elif opcion == "4":
                self.disminuir_stock_interactivo()
            elif opcion == "5":
                self.ver_bajo_stock()
            elif opcion == "6":
                self.ver_reporte()
            elif opcion == "7":
                print("\nHasta luego!")
                break
            else:
                print("\nERROR - Opción Invalida")
                
    def _cargar_datos_prueba(self):
        """Carga datos de prueba en el inventario."""
        productos_prueba = [
            ("Laptop", "Laptop Core i7", 899.99, 5, Categoria.ELECTRONICA),
            ("Mouse", "Mouse inalambrico ", 25.50, 50, Categoria.ELECTRONICA),
            ("Teclado", "Teclado Mecanico", 120.00, 15, Categoria.ELECTRONICA),
            ("Pan", "Pan Blanco artesanal", 3.50, 100, Categoria.ALIMENTOS),
            ("Queso", "Queso fresco", 12.00, 30, Categoria.ALIMENTOS),
            ("Camiseta", "Camiseta de algodón", 45.00, 20, Categoria.ROPA),
            ("Python Pro", "Libro de Python avanzado", 89.99, 8, Categoria.LIBROS),
        ]     

        for nombre, desc, precio, cantidad, categoria in productos_prueba:
            self.inventario.agregar_producto(nombre, desc, precio, cantidad, categoria)
        
        print("OK - Datos de prueba cargados") 
         
def main():   
    app = AplicacionInventario()
    app.ejecutar()
    
if __name__ == '__main__':
     main()
            
   
