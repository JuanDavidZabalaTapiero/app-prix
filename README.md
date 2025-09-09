# App-Prix

## Clonar el repositorio

```bash
git clone https://github.com/JuanDavidZabalaTapiero/app-prix.git
cd app-prix
```

## Crear entorno virtual

```bash
python -m venv .venv
```

## Activar entorno
```bash
# Windows
.venv\Scripts\activate
```

```bash
# Linux / Mac
source .venv/bin/activate
```

## Instalar dependencias

```bash
# Producción
pip install -r requirements.txt
```

```bash
# Desarrollo
pip install -r requirements.txt
```

## Configuración de variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
SECRET_KEY=tu_clave_secreta
DATABASE_URL=mysql://usuario:contraseña@host:3306/nombre_bd
```

## Base de datos (migraciones)

Si no está la carpeta migrations/:
```bash
flask db init
```

Si hay cambios en los modelos:
```bash
flask db migrate -m "mensaje describiendo el cambio"
```

Actualizar la BD:
```bash
flask db upgrade
```

## Pre-commit
```bash
pre-commit install
```

## Ejecutar tests
```bash
pytest
```

## Ejecutar la aplicación
```bash
python run.py
```
## Documentación
Se sigue el **Google style** para docstrings y documentación de funciones.
