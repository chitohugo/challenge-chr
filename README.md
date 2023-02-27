# Challenge for CHR

## Running with docker

### Pre-requisites:
- docker
- docker compose (New)

### Steps
1. Create a file called `.env` with environment variables
2. Build with `docker compose build`
3. Run with `docker compose up`

### How to use
1. In terminal run: 
   - `docker compose exec web python manage.py migrate` 
   - `docker compose exec web python manage.py createsuperuser`
   - `docker compose exec web python manage.py runscript get_seia`
   - `docker compose exec web python manage.py runscript get_citi_bik`
   - `Go to http://localhost:8000/admin/`


### Variables

- SECRET_KEY = 'Generate secret key'
- POSTGRES_DB = 
- POSTGRES_USER =
- POSTGRES_PASSWORD =
- URL_API = 'http://api.citybik.es/v2/networks/bikesantiago'
- URL_API2 = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'