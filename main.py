from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials
from presentation.controllers import ControladorPrincipal


def inicializar_firebase():
    load_dotenv()

    cred_path = os.getenv("FIREBASE_CREDENTIALS")
    db_url = os.getenv("FIREBASE_DB_URL")

    if not cred_path:
        raise ValueError("No se encontró FIREBASE_CREDENTIALS_PATH en el archivo .env")

    if not db_url:
        raise ValueError("No se encontró FIREBASE_DB_URL en el archivo .env")

    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"databaseURL": db_url})


def main():
    inicializar_firebase()
    controlador = ControladorPrincipal()
    controlador.ejecutar()


if __name__ == "__main__":
    main()
