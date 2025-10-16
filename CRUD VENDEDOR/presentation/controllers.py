from data.firebase_repository import FirebaseRepository
from presentation.console_ui import ConsolaUI


class ControladorPrincipal:
    def __init__(self):
        self.repo = FirebaseRepository()
        self.ui = ConsolaUI()

    def ejecutar(self):
        while True:
            opcion = self.ui.mostrar_menu("MENÚ PRINCIPAL", [
                "Gestionar clientes",
                "Gestionar productos",
                "Salir"
            ])

            if opcion == 1:
                self.menu_clientes()
            elif opcion == 2:
                self.menu_productos()
            elif opcion == 3:
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida.")

    # ---------------------------------------------------------------------
    # CLIENTES
    # ---------------------------------------------------------------------
    def menu_clientes(self):
        while True:
            opcion = self.ui.mostrar_menu("GESTIÓN DE CLIENTES", [
                "Agregar cliente",
                "Listar clientes",
                "Actualizar cliente",
                "Eliminar cliente",
                "Volver al menú principal"
            ])

            if opcion == 1:
                self.agregar_cliente()
            elif opcion == 2:
                self.listar_clientes()
            elif opcion == 3:
                self.actualizar_cliente()
            elif opcion == 4:
                self.eliminar_cliente()
            elif opcion == 5:
                break
            else:
                print("❌ Opción inválida.")

    def agregar_cliente(self):
        nombre = input("Ingrese el nombre del cliente: ").strip()
        deuda = input("Ingrese la deuda del cliente: ").strip()
        try:
            deuda = float(deuda)
        except ValueError:
            print("⚠️ La deuda debe ser un número.")
            return
        cliente = {"nombre": nombre, "deuda": deuda}
        self.repo.agregar_cliente(cliente)

    def listar_clientes(self):
        clientes = self.repo.listar_clientes()
        if not clientes:
            print("⚠️ No hay clientes registrados.")
            return
        print("\n📋 LISTA DE CLIENTES:")
        for c in clientes:
            print(f"🆔 {c['id']} | Nombre: {c['nombre']} | Deuda: {c['deuda']}")
        print()

    def actualizar_cliente(self):
        cliente_id = input("Ingrese el ID del cliente a actualizar: ").strip()
        nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip()
        deuda = input("Nueva deuda (dejar vacío para no cambiar): ").strip()

        campos = {}
        if nombre:
            campos["nombre"] = nombre
        if deuda:
            try:
                campos["deuda"] = float(deuda)
            except ValueError:
                print("⚠️ La deuda debe ser un número.")
                return

        if campos:
            self.repo.actualizar_cliente(cliente_id, campos)
        else:
            print("⚠️ No se ingresaron campos para actualizar.")

    def eliminar_cliente(self):
        cliente_id = input("Ingrese el ID del cliente a eliminar: ").strip()
        self.repo.eliminar_cliente(cliente_id)

    # ---------------------------------------------------------------------
    # PRODUCTOS
    # ---------------------------------------------------------------------
    def menu_productos(self):
        while True:
            opcion = self.ui.mostrar_menu("GESTIÓN DE PRODUCTOS", [
                "Agregar producto",
                "Listar productos",
                "Actualizar producto",
                "Eliminar producto",
                "Volver al menú principal"
            ])

            if opcion == 1:
                self.agregar_producto()
            elif opcion == 2:
                self.listar_productos()
            elif opcion == 3:
                self.actualizar_producto()
            elif opcion == 4:
                self.eliminar_producto()
            elif opcion == 5:
                break
            else:
                print("❌ Opción inválida.")

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ").strip()
        precio = input("Ingrese el precio del producto: ").strip()
        stock = input("Ingrese el stock (opcional, por defecto 0): ").strip()

        try:
            precio = float(precio)
            stock = int(stock) if stock else 0
        except ValueError:
            print("⚠️ Precio o stock inválido.")
            return

        producto = {"nombre": nombre, "precio": precio, "stock": stock}
        self.repo.agregar_producto(producto)

    def listar_productos(self):
        productos = self.repo.listar_productos()
        if not productos:
            print("⚠️ No hay productos registrados.")
            return
        print("\n📦 LISTA DE PRODUCTOS:")
        for p in productos:
            print(f"🆔 {p['id']} | Nombre: {p['nombre']} | Precio: {p['precio']} | Stock: {p.get('stock', 0)}")
        print()

    def actualizar_producto(self):
        producto_id = input("Ingrese el ID del producto a actualizar: ").strip()
        nombre = input("Nuevo nombre (dejar vacío para no cambiar): ").strip()
        precio = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
        stock = input("Nuevo stock (dejar vacío para no cambiar): ").strip()

        campos = {}
        if nombre:
            campos["nombre"] = nombre
        if precio:
            try:
                campos["precio"] = float(precio)
            except ValueError:
                print("⚠️ El precio debe ser un número.")
                return
        if stock:
            try:
                campos["stock"] = int(stock)
            except ValueError:
                print("⚠️ El stock debe ser un número.")
                return

        if campos:
            self.repo.actualizar_producto(producto_id, campos)
        else:
            print("⚠️ No se ingresaron campos para actualizar.")

    def eliminar_producto(self):
        producto_id = input("Ingrese el ID del producto a eliminar: ").strip()
        self.repo.eliminar_producto(producto_id)
