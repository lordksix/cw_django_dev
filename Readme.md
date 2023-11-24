# Claritywave challenge
```bash

```

Author: Wladimir-lordksix

## Instructions
- Project can be run in two environments, development or production. It is also deployed to [here](https://lit-hollows-12137-4ef97bdabd36.herokuapp.com/). Admin user for deployment is user and password is user.
1. To run locally no matter the type of enviroment, you need to have docker install. You must clone and run the following command:

Development
```bash
    docker compose -f docker-compose.yml up -d --build
```
and go to localhost:8000

Production: I need to setup .env using .env.example as template.
```bash
    docker compose -f docker-compose.prod.yml up -d --build
```
and go to localhost

- To create a new super user, run the following command inside the container cw_django_dev or cw_django_prod depending on the environment chosen
```bash
    python manage.py createsuperuser
```

- To run tests, run the following command inside the container cw_django_dev or cw_django_prod depending on the environment chosen
```bash
    python manage.py test
```

- To stop running the app run the following commands
Development
```bash
    docker compose -f docker-compose.yml stop
```

Production
```bash
    docker compose -f docker-compose.prod.yml stop
```

- To delete containers run the following commands
Development
```bash
    docker compose -f docker-compose.yml down
```

Production
```bash
    docker compose -f docker-compose.prod.yml down
```

- To authentication, authorization was also implemented. Just the user that created the question can modified it.
- Production-setup branch has development and production environments
- Development branch has development environments

Author: CW-TEAM

## Instrucciones:

### How to
1. Genera un fork de este proyecto para que puedas trabajar en tu propio espacio.
2. Una vez finalizado, esperamos que nos envíes el enlace a tu repositorio y el tiempo estimado que te llevó hacerlo. Si no quieres hacer público tu fork, nos puedes contactar y te decimos como lo solucionamos.

### Constraints

Esperamos que dejes una app funcional.
* En la página principal se tienen que mostrar las mejores 20 preguntas ordenadas según el siguiente ranking:
    1. Cada respuesta suma 10 puntos al ranking
    2. Cada like suma 5 puntos al ranking
    3. Cada dislike resta 3 puntos al ranking
    4. Las preguntas del día de hoy, tienen un extra de 10 puntos


_Ejemplo_:
Una pregunta que tiene 6 respuesta de usuarios, 2 likes y 1 dislike:
ranking: `6*10 + 2*5 - 1*3 = 60 + 10 - 3 = 67`
Si además es del día de la hoy:
ranking: `6*10 + 2*5 - 1*3 + 10 = 60 + 10 - 3 +10 = 77`

### A tener en cuenta:
- Modifica todo lo que creas necesario. Dejamos errores voluntariamente.
- Evaluaremos no solo la funcionalidad, también esperamos una buena performance ante la posibilidad de que escale el proyecto
- El sistema de login/logout no es necesario modificarlo. Genera los usuarios para probar desde la consola.

### Extras
- Si puedes levantar un entorno con docker, te invitamos a que lo hagas.
- Nos gustaría ver que puedes generar un test con los casos de usos básicos.

###

### Ejemplo
Este es un ejemplo de como queda el listado con su ranking y se ve como respondió/votó el usuario actual.

![Example](example.png)
