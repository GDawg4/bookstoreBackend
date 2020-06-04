# Book Store - Backend

## Requsitos
Tener instalado Django y Python
Tener un ambiene virtual creado

## Pasos para levantar el servidor
1. Activar el ambiente virtual
2. Navegar hacia el directorio del backend
3. Instalar los requirements
4. Hacer las migraciones (en caso no estén hechas), ejecutar 
```bash
$ python manage.py makemigrations
```
5. Migrar, ejecutar
```bash
$ python manage.py migrate
```
6. Para cargar los datos iniciales, ejecutar
```bash
$ python manage.py runscript setup
```
7. Para levantar el servidor ejecutar
```bash
$ python manage.py runserver 192.168.1.8:8000
```

## NOTA 
En caso la dirección IPv4 propia fuese otra, correr con la IPv4 propia en lugar ed 192.168.1.8
