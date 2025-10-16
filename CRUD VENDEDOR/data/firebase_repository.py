import firebase_admin
from firebase_admin import credentials, db
from typing import Dict, Any, List
import os
from dotenv import load_dotenv


class FirebaseRepository:
    def __init__(self):
        # Cargar variables desde el archivo .env
        load_dotenv()

        db_url = os.getenv("FIREBASE_DB_URL")
        cred_path = os.getenv("FIREBASE_CREDENTIALS", "firebase_key.json")

        if not db_url:
            raise ValueError("⚠️ No se encontró FIREBASE_DB_URL en el archivo .env")

        # Inicializar Firebase solo una vez
        if not firebase_admin._apps:
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {"databaseURL": db_url})

        print("✅ Conectado correctamente a Firebase Realtime Database.")

        # Referencias principales
        self.customers_ref = db.reference("clientes")
        self.products_ref = db.reference("productos")

    # ---------------------------------------------------------------------
    # CLIENTES
    # ---------------------------------------------------------------------
    def listar_clientes(self) -> List[Dict[str, Any]]:
        data = self.customers_ref.get() or {}
        return [{"id": k, **v} for k, v in data.items()]

    def obtener_cliente(self, cliente_id: str) -> Dict[str, Any] | None:
        data = self.customers_ref.child(str(cliente_id)).get()
        if data:
            return {"id": cliente_id, **data}
        return None

    def agregar_cliente(self, cliente: Dict[str, Any]) -> Dict[str, Any]:
        nuevo_id = f"cliente_{len(self.listar_clientes()) + 1}"
        new_ref = self.customers_ref.child(nuevo_id)
        new_ref.set({
            "nombre": cliente.get("nombre"),
            "deuda": cliente.get("deuda")
        })
        cliente["id"] = nuevo_id
        print(f"🟢 Cliente '{cliente['nombre']}' agregado con ID {nuevo_id}")
        return cliente

    def actualizar_cliente(self, cliente_id: str, campos: Dict[str, Any]) -> bool:
        ref = self.customers_ref.child(str(cliente_id))
        if ref.get():
            ref.update(campos)
            print(f"🟡 Cliente {cliente_id} actualizado.")
            return True
        print("❌ Cliente no encontrado.")
        return False

    def eliminar_cliente(self, cliente_id: str) -> bool:
        ref = self.customers_ref.child(str(cliente_id))
        if ref.get():
            ref.delete()
            print(f"🔴 Cliente {cliente_id} eliminado.")
            return True
        print("❌ Cliente no encontrado.")
        return False

    # ---------------------------------------------------------------------
    # PRODUCTOS
    # ---------------------------------------------------------------------
    def listar_productos(self) -> List[Dict[str, Any]]:
        data = self.products_ref.get() or {}
        return [{"id": k, **v} for k, v in data.items()]

    def obtener_producto(self, producto_id: str) -> Dict[str, Any] | None:
        data = self.products_ref.child(str(producto_id)).get()
        if data:
            return {"id": producto_id, **data}
        return None

    def agregar_producto(self, producto: Dict[str, Any]) -> Dict[str, Any]:
        nuevo_id = f"producto_{len(self.listar_productos()) + 1}"
        new_ref = self.products_ref.child(nuevo_id)
        new_ref.set({
            "nombre": producto.get("nombre"),
            "precio": producto.get("precio"),
            "stock": producto.get("stock", 0)
        })
        producto["id"] = nuevo_id
        print(f"🟢 Producto '{producto['nombre']}' agregado con ID {nuevo_id}")
        return producto

    def actualizar_producto(self, producto_id: str, campos: Dict[str, Any]) -> bool:
        ref = self.products_ref.child(str(producto_id))
        if ref.get():
            ref.update(campos)
            print(f"🟡 Producto {producto_id} actualizado.")
            return True
        print("❌ Producto no encontrado.")
        return False

    def eliminar_producto(self, producto_id: str) -> bool:
        ref = self.products_ref.child(str(producto_id))
        if ref.get():
            ref.delete()
            print(f"🔴 Producto {producto_id} eliminado.")
            return True
        print("❌ Producto no encontrado.")
        return False
