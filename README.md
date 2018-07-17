# BDO Market Calculator

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
