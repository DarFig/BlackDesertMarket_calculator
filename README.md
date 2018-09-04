# BDO Market Calculator

Esta aplicación es simplemente para manejar los datos de una BBDD personal sobre estudios de mercado en el mmorpg Black Desert Online. El objetivo es tener una aplicación con una interfaz para permitir gestionar datos de forma cómoda, a diferencia de lo que hacen otros usuarios con **hojas de cálculo**, o anotaciones manuales.

## Uso

## Requisitos

- Una lista de requisitos en ![requirements](https://github.com/DarFig/BlackDesertMarket_calculator/blob/master/requirements.txt)

## Instalación

- La instalación se divide entre **inst.sh** (requiere python y apt) y el despliegue de la BBDD ver ![./BBDD/crearBBDD.txt](https://github.com/DarFig/BlackDesertMarket_calculator/blob/master/BBDD/crearBBDD.sql) y ![./BBDD/crearBBDD.txt](https://github.com/DarFig/BlackDesertMarket_calculator/blob/master/BBDD/create_tables.sql) 
- En ./web/configFile.txt poner una línea con los datos de acceso a la BBDD para la aplicación. Hay que tener en cuenta que la aplicación solo necesita leer, escribir y borrar en las tablas, no crear ni destruir. El formato es el siguiente:
**data_base_uri mysql+pymysql://user:passw@host/nombreBBDD**


## Diagramas

### Base de Datos

#### Modelos de acceso

- Ingrediente
- Objeto
- Precio
- Proceso
- Receta


## Estado

### Views

- index
- objeto
- nuevoobjeto
- receta

### Routes

**GET**

- /           -> _views/index           
- /objeto/id/ -> _views/objeto          
- /newobject/ -> _views/nuevoobjeto     
- /id/edit/   -> _views/nuevoobjeto     
- /receta/id/ -> _views/receta          

**POST**

- /receta/id/ -> _views/receta          
