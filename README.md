# 📖 Parallelus - Visor Bíblico Paralelo

Una aplicación web Django para consultar la Biblia con múltiples traducciones en paralelo, incluyendo textos en hebreo y griego.

## 🚀 Características

- **Múltiples traducciones**: Soporte para diversas versiones bíblicas
- **Texto interlineal**: Visualización en hebreo/griego original
- **Interfaz moderna**: Diseño responsive con Bootstrap 4
- **Navegación intuitiva**: Selección de libro, capítulo y versículo
- **Comparación paralela**: Visualización simultánea de diferentes versiones

## 🛠️ Tecnologías

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 4, jQuery
- **Base de datos**: SQLite (desarrollo), PostgreSQL (producción recomendado)
- **Servidor**: Gunicorn

## 📋 Requisitos

- Python 3.8+
- pip
- Archivos bíblicos (.bbli, .bblx)

## 🔧 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd parallelus
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp env.example .env
   # Editar .env con tus configuraciones
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

## 📁 Estructura del Proyecto

```
parallelus/
├── home/                    # Aplicación principal
│   ├── bibles/             # Archivos bíblicos (.bbli, .bblx)
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas y lógica de negocio
│   ├── admin.py            # Configuración del admin
│   └── templates/          # Plantillas HTML
├── parallelus/             # Configuración del proyecto
│   ├── settings.py         # Configuración de Django
│   └── urls.py             # URLs principales
├── requirements.txt        # Dependencias de Python
└── README.md              # Este archivo
```

## 🔒 Configuración de Seguridad

### Variables de Entorno

Crea un archivo `.env` con las siguientes variables:

```env
SECRET_KEY=tu_clave_secreta_muy_segura
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
```

### Configuraciones de Producción

1. **Cambiar DEBUG a False**
2. **Configurar ALLOWED_HOSTS**
3. **Usar una base de datos más robusta (PostgreSQL)**
4. **Configurar HTTPS**
5. **Usar un servidor web como Nginx**

## 📊 Modelos de Datos

### Book
- `num`: Número del libro (1-66)
- `name`: Nombre del libro
- `hebreo`: Nombre en hebreo
- `fonetica`: Transcripción fonética

### Bible
- `name`: Nombre interno del archivo
- `label`: Nombre para mostrar
- `description`: Descripción de la versión
- `file`: Nombre del archivo .bbli/.bblx
- `visible`: ¿Es visible en la interfaz?
- `activo`: ¿Está activa para mostrar en paralelo?

## 🔧 API Endpoints

- `GET /`: Página principal
- `POST /ajax/capitulos/`: Obtener capítulos de un libro
- `POST /ajax/versiculos/`: Obtener versículos de un capítulo
- `POST /ajax/test/`: Obtener texto bíblico

## 🎨 Personalización

### Estilos CSS
Los estilos personalizados se encuentran en `home/static/home/custom.css`

### Plantillas
Las plantillas HTML están en `home/templates/home/`

## 🚀 Despliegue

### Con Docker (Recomendado)

1. **Crear Dockerfile**
2. **Crear docker-compose.yml**
3. **Ejecutar**: `docker-compose up -d`

### Con Gunicorn

```bash
gunicorn parallelus.wsgi:application --bind 0.0.0.0:8000
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:

1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema

## 🔄 Changelog

### v2.0.0 (2024)
- ✅ Corregidas vulnerabilidades de seguridad
- ✅ Actualizadas dependencias
- ✅ Mejorada interfaz de usuario
- ✅ Agregadas validaciones de datos
- ✅ Mejorado manejo de errores

### v1.0.0 (2020)
- 🎉 Lanzamiento inicial 