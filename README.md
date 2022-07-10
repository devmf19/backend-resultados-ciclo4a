
# REQUERIMIENTOS:

- flask
- flask-cors
- waitress


## INSTALACIÓN EN PYCHARM:

Para llevar a cabo el proceso de instalación se debe ubicar sobre las palabras subrayadas en el archivo main.py y 
se activará un círculo rojo con un signo de exclamación, se debe dar click sobre este y aparecerá la opción de instalar el paquete.

En caso que no aparezca la opción “Install package” como es el caso de la librería “flask_cors”, 
es necesario ingresar al menú de la parte superior izquierda “File” opción “Settings”. Una vez se ingresa al menú del interprete de Python, 
se debe dar click sobre el botón “+”. Luego se debe buscar el nombre de la librería correspondiente, en este caso se instalará “flask-cors” y 
se procede a instalarla.

# Contribuciones
Estamos trabajando sobre la rama developer y dejamos la rama main para las versiones estables
## Clonar el proyecto en local

```
git clone https://github.com/martinezfran19/backend-resultados-ciclo4a.git

```

## Cómo guardo mis cambios en el repositorio?

Primero guardo mis cambios en local y luego los agrego al repositorio
```
git add .
git commit -m "mensaje con el que identifico mis cambios"
git push origin main:nombre_de_mi_rama
```

Después de esto ingresa a este Git y debes hacer el pull request. La url debe ser algo como

```
https://github.com/martinezfran19/backend-resultados-ciclo4a/pull/new/nombre_de_mi_rama
```

## Cómo hago si ya he trabajado pero mis compañeros ya han hecho algo?
En este caso es muy común y debes actualizar tu colaboración con lo que ya se ha hecho entes de subir tus cambios.
> Recuerda guardar tus cambios el local antes de cualquier cosa

```
git add .
git commit -m "mensaje con el que identifico mis cambios"
git pull --rebase
```

Ya actualizado puedes subir los cambios en conjunto
```
git push origin main:nombre_de_mi_rama
```
# No tengo permiso para hacer cambios!!
Solo dilo por whatsapp a Francisco Martínez [martinezfran19 ]

# Instalation

```
$ pip install -r requirements.txt
```

# Running and test

```
$ python main.py
```
