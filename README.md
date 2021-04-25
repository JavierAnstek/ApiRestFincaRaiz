# ApiFincaRaiz

Este componente se ha desarrollado con el único propósito de abordar una prueba técnica para el área de tecnología en Finca Raíz.

## Instalación y puesta en marcha

1. descargue los archivos del proyecto y ubíquelos en la ruta de su ordenador que usted considere.
2. cree un ambiente virtual dentro de la carpeta que contiene los archivos del proyecto, se recomienda trabajar con Python en su versión 3.7

```bash
### python -m venv NombreAmbienteVirtual
```

3. Una vez creado el ambiente virtual instale los paquetes requeridos en el archivo requirements.txt que se encuentra en la raíz de la carpeta principal, (No olvide activar el ambiente virtual que creó en el paso anterior).

```bash
### pip install -r requirements.txt
```

## Modo de uso de la aplicación

Si el proceso de creación del ambiente virtual y la instalación de los paquetes requeridos no ha presentado problema, entonces ya estará listo para validar el desarrollo en ambiente local, el proyecto contará con los paquetes de django, django-rest_framework y una base de datos sqlite3.

Para ejecutar el servidor use el siguiente comando en una consola de su interés, (No olvide ubicarse en la ruta del proyecto y tener activo el ambiente virtual creado)

```bash
### python manage.py runserver
```

Si todo ha ido bien en la instalación y configuración, el framework de django deberá lanzar un servidor de prueba en modo local generalmente por el puerto 8000, tal como se muestra en la siguientes líneas.

```bash
### System check identified no issues (0 silenced).
### April 24, 2021 - 19:17:53
### Django version 3.2, using settings 'apifincaraiz.settings.local'
### Starting development server at http://127.0.0.1:8000/
### Quit the server with CTRL-BREAK.
```

Si el resultado de ejecutar el comando runserver es similar al anterior, entonces ya podrá ejecutar las APSIS desarrolladas en éste proyecto, los endpoint a los cuales tendrá acceso son los siguientes:

> **NOTA: _todos los endpoint referenciados a continuación se pueden probar directamente desde el servidor de prueba que ofrece django, pero además se puede usar el administrador de django a modo de gestión de los mismos datos tal como se detallará al final del ítem._**

- States: Corresponde a los endpoints de acceso y gestión CRUD de los registros de estados.

```bash
### api/states.
### api/states/create
### api/states/detail/<pk> : recibe el identificador del registro que se desea consultar
### api/states/update/<pk> : recibe el identificador del registro que se desea modificar
### api/states/delete/<pk> : recibe el identificador del registro que se desea eliminar
```

- Cities: Corresponde a los endpoints de acceso y gestión CRUD de los registros de ciudades.

```bash
### api/cities.
### api/cities/create
### api/cities/detail/<pk> : recibe el identificador del registro que se desea consultar
### api/cities/update/<pk> : recibe el identificador del registro que se desea modificar
### api/cities/delete/<pk> : recibe el identificador del registro que se desea eliminar
```

- Categories: Corresponde a los endpoints de acceso y gestión CRUD de los registros de Categorias.

```bash
### api/categories
### api/categories/create
### api/categories/detail/<pk> : recibe el identificador del registro que se desea consultar
### api/categories/update/<pk> : recibe el identificador del registro que se desea modificar
### api/categories/delete/<pk> : recibe el identificador del registro que se desea eliminar
```

- PropertiesTypes: Corresponde a los endpoints de acceso y gestión CRUD de los registros de Tipos de Propiedades.

```bash
### api/propertyTypes
### api/propertyTypes/create
### api/propertyTypes/detail/<pk> : recibe el identificador del registro que se desea consultar
### api/propertyTypes/update/<pk> : recibe el identificador del registro que se desea modificar
### api/propertyTypes/delete/<pk> : recibe el identificador del registro que se desea eliminar
```

- Properties: Corresponde a los endpoints de acceso y gestión CRUD de los registros de Propiedades.

```bash
### api/properties
### api/properties/create
### api/properties/detail/<pk> : recibe el identificador del registro que se desea consultar
### api/properties/update/<pk> : recibe el identificador del registro que se desea modificar
### api/properties/delete/<pk> : recibe el identificador del registro que se desea eliminar
```

- Reviews: Corresponde a los endpoints de acceso para consulta y creación de los registros de comentarios o reviews realizados a las propiedades.

```bash
### api/reviews/<pk> : recibe el identificador de la propiedad a la cual se quiere listar sus reviews
### api/reviews/create
```

## Modo de uso del Administrador de Django

Para gestionar los datos desde el administrador de django se debe acceder a la siguiente ruta y proporcionar usuario y password.

```bash
### http://127.0.0.1:8000/admin/
### User:___
### Pass:___
```

Una vez en el administrador se podrá realizar la gestión de cada uno de los modelos gestionados por los endpoints presentados anteriormente.

## Oportunidades de mejora

Las siguientes son oportunidades de mejora que por la limitación en tiempo no se incluyeron en el desarrollo

- Gestión de Usuarios
- Seguridad en las APIS mediante token u otra técnica existente
