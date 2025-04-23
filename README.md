# 🏈Fantasy Sports API🏈
Una API RESTful construida con **FastAPI** y **SQLModel** para la gestión de datos de jugadores, equipos y ligas en un entorno de fantasy sports. Este proyecto incluye operaciones CRUD completas, filtros dinámicos y endpoints para analíticas básicas.

---

## 🚀 Tecnologías Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- SQLite (puede ser reemplazado fácilmente por PostgreSQL, MySQL, etc.)
- Pydantic
- Pytest

---

## 📁 Estructura del Proyecto
├── app/                        # Módulo principal de la aplicación FastAPI
│   ├── __pycache__/            # Archivos compilados por Python (se ignoran)
│   ├── __init__.py             # Inicializa el paquete app
│   ├── main.py                 # Punto de entrada principal de FastAPI
├── data/                       # Con los datos en csv para importar a la base de datos
├── .gitignore                  # Archivos/directorios ignorados por Git
├── crud.py                     # Funciones CRUD (acceso a la base de datos)
├── db.py                       # Configuración de la conexión a la base de datos
├── fantasy_data.db             # Base de datos SQLite con datos de fantasy
├── LICENSE                     # Licencia del proyecto
├── models.py                   # Definición de modelos con SQLModel
├── README.md                   # Documentación principal del proyecto
├── requirements.txt            # Dependencias del proyecto
├── schemas.py                  # Esquemas Pydantic para validación de datos


---

## ⚙️ Instalación y Ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/Javierxd1/SWC-API-project.git
cd SWC-API-project

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

pip install -r requirements.txt
```
