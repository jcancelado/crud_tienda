class ConsolaUI:
    def mostrar_menu(self, titulo, opciones):
        print(f"\n==============================")
        print(f" {titulo}")
        print(f"==============================")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")
        print("==============================")
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            print("⚠️ Debe ingresar un número válido.")
            return 0
