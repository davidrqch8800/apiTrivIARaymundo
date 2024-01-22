# Instalación

Para descargar, ejecuta:

```sh
git clone https://github.com/davidrqch8800/apiTrivIARaymundo.git  
```
Una vez que esté descargado, debes crear un ambiente virtual con python dentro de la carpeta `/apiTrivIARaymundo`.

```sh
python -m venv mv
```
Ahora activar el ambiente virtual:

```sh
cd mv
```
```sh
cd Scripts
```
```sh
activate
```

Regresamos a `/apiTrivIARaymundo` y a continuacion instalamos lo siguiente:

```sh
pip install fastapi uvicorn
```
```sh
pip install scikit-learn sqlalchemy pymysql
```
```sh
pip install pandas
```
```sh
pip install cryptography
```
## Configuración

Ir a `config/dbp.py` y modificar la contraseña de mysql `contraseña` y el nombre de tu base de datos `basededatos` :
```sh
URL_DATABASE = 'mysql+pymysql://root:contraseña@localhost:3306/basededatos'
```
