# Laboratorio 4. Taller Inicial de Django: Views, Templates y Modelos

Este laboratorio está diseñado para que los participantes puedan aprender y reforzar sus conocimientos de Python, HTML y CSS mediante la creación de una lista de Pokemones y una página de datalle. Utilizando como framework de desarrollo MVC a Django. De la misma manera se hará una introduccion a Bootstrap para el uso de librerías de Interfaz de usuario en HTML.

Por otra parte se aplica el uso de Modelos en Django y uso de bases de datos relacionales.

Además el estudiante aprenderá el manejo de Django desde los templates, views, models, así como la generación de API REST usando Django Rest Framework

## Datos del estudiante
- **Nombre:** Alberto Sebastián Andrade Endara
- **Carrera:** Ing. Informática

## Objetivos 
- El estudiante debe ser capaz de reconocer y aplicar conceptos básicos del Paradigma Orientado a Objetos (POO) como: Clases, Ojetos, Atributos, Métodos. Así mismo el presente proyecto introduce al desarrollo de aplicaciones Web mediante el uso de Django como marco de trabajo para el desarrollo.
- El estudiante reforzará sus conocimientos de POO y manejo de bases de datos relacionales a través del uso de modelos en Django
- El estudiante desarrollará backend con API REST

## Tareas a realizar
1. Generación de Modelos de Pokemon y Trainer
2. Generación de migraciones.
3. Despliegue de Pokemones en Templates lista y detalle
4. Despliegue de Entrenadores en Templates lista y detalle



## Instalación del ambiente

### Requerimientos

- Python 3.10 o superior
- PostgreSQL
- Configurar el repositorio local
    ~~~
    git config --local user.name "[Nombre del estudiante]"
    ~~~
    ~~~
    git config --local user.email "[Email de cuenta Github del estudiante]"
    ~~~

### Ubuntu Linux / MacOS
Instalación de gestor de ambientes virtuales de Python
~~~
sudo apt install python3-venv
~~~
Creación del ambiente virtual
~~~
python3 -m venv .venv
~~~
Activación del ambiente virtual
~~~
source .venv/bin/activate
~~~
Instalación de dependencias de este proyecto
~~~
pip3 install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~
### Windows
Instalación de gestor de ambientes virtuales de Python
~~~
pip install virtualenv
~~~
Creación del ambiente virtual
~~~
py -m venv .venv
~~~
Activación del ambiente virtual para CMD
~~~
.venv\Scripts\activate
~~~
Activación del ambiente virtual para PowerShell
~~~
.venv\Scripts\activate.ps1
~~~
Instalación de dependencias de este proyecto
~~~
pip install -r requirements.txt
~~~
En caso de querer desactivar el ambiente usar
~~~
deactivate
~~~


## Integración con el cliente React (Laboratorio 10)

El cliente React se ejecuta normalmente en `http://localhost:5173` y consume esta API en `http://localhost:8000/api`. Como son orígenes distintos, el backend incluye `django-cors-headers` y permite únicamente los orígenes locales de Vite:

- `http://localhost:5173`
- `http://127.0.0.1:5173`

Después de actualizar el proyecto, instala la nueva dependencia:

```bash
pip install -r requirements.txt
```

Luego inicia Django:

```bash
python manage.py migrate
python manage.py runserver
```

La lista de Pokémon queda disponible en:

```text
http://localhost:8000/api/pokemons/
```

## Comandos útiles

### Iniciar servidor
#### Linux o MaCOS
~~~
python3 manage.py runserver
~~~
#### Windows
~~~
python manage.py runserver
~~~

Una vez inicializado el servidor se deberá dirigir al siguiente enlace: <http://localhost:8000>

### Crear nueva aplicación
#### Linux o MaCOS
~~~
python3 manage.py startapp <nombre_de_la_aplicacion>
~~~
#### Windows
~~~
python manage.py startapp <nombre_de_la_aplicacion>
~~~

### Crear Súper Usuario
#### Linux o MaCOS
~~~
python3 manage.py createsuperuser
~~~
#### Windows
~~~
python manage.py createsuperuser
~~~

### Generar archivos de migración
#### Linux o MaCOS
~~~
python3 manage.py makemigrations
~~~
#### Windows
~~~
python manage.py makemigrations
~~~

### Migrar a bases de datos
#### Linux o MaCOS
~~~
python3 manage.py migrate
~~~
#### Windows
~~~
python manage.py migrate
~~~

### Almacenar dependencias y librerías instaladas
#### Linux o MaCOS
~~~
pip3 freeze > requirements.txt
~~~
#### Windows
~~~
pip freeze > requirements.txt
~~~

# Nota
Para los siguientes pasos se deberán seguir las **instrucciones del docente en clase**. No olvides que puedes contactarlo a <paperez@puce.edu.ec>


# Ejemplos de Cadenas de Conexión para Django

### PostgreSQL

- Instalar pyscopg2
    ```bash
    pip3 install psycopg2
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```
### MySQL
- Instalar mysqlclient
    ```bash
    pip3 install mysqlclient
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

### SQLite
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

### Oracle

- Instalar cx_Oracle
    ```bash
    pip3 install cx_Oracle
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '1521',
        }
    }
    ```

### SQL Server (usando django-mssql-backend)

- Instalar cx_Oracle
    ```bash
    pip3 install django-mssql-backend
    ```
- Configurar archivo settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'nombre_de_tu_base_de_datos',
            'USER': 'tu_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '1433',
            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        }
    }
    ```

## Pruebas completas con Thunder Client y OAuth2

El proyecto incluye la colección mostrada en clase dentro de `thunder-client/`:

- `Pokedex`: obtener, agregar, editar y eliminar Pokémon.
- `Trainer`: listar, agregar, editar y eliminar entrenadores.
- `User Management`: solicitud `LoginPokedex` para obtener el token OAuth2.

### 1. Preparar OAuth2

Después de instalar las dependencias, ejecuta:

```powershell
python manage.py migrate
```

Si todavía no existe el usuario administrador:

```powershell
python manage.py createsuperuser
```

Crea o actualiza la aplicación OAuth2 con el comando incluido:

```powershell
python manage.py setup_oauth_client --username admin --client-id TU_CLIENT_ID --client-secret TU_CLIENT_SECRET
```

El cliente queda configurado como `confidential` y con el grant type `password`, que es el utilizado por `LoginPokedex`.

### 2. Importar la colección

En Thunder Client:

1. Abre la sección **Env** e importa `thunder-client/Pokedex.local.env`.
2. Cambia la variable `password` por la contraseña real del usuario de Django.
3. Abre **Collections** e importa `thunder-client/thunder-collection_Pokedex.json`.
4. Ejecuta primero `LoginPokedex`.
5. La prueba de la solicitud almacena `json.access_token` en `{{access_token}}`.
6. Ejecuta las solicitudes POST, PUT y DELETE.

El archivo `Pokedex.local.env` contiene credenciales locales y está excluido de Git. Para compartir el proyecto utiliza `Pokedex.example.env`.
