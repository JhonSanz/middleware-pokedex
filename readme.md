# POKEDEX MIDDLEWARE    

### TUTORIAL

0. Obligatorio tener docker instalado
1. ejecutar `docker compose -f .\docker-compose.yml up --build`
2. ingresar a localhost:8000/docs
3. probar los endpoints de interés
4. correr los tests con `docker exec dev-pokedex-backend pytest`
5. disfrutar


### CONSIDERACIONES

El método update es ficticio y no impacta la información real de pokeapi ya que dice explícitamente  [**This is a consumption-only API — only the HTTP GET method is available on resources.**](https://pokeapi.co/docs/v2#info). Para hacer la información persistente se requiere almacenamiento y **eso escapa a los requerimientos del ejercicio** propuesto en el PDF.