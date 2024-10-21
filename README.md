# NoName-Surveys

**Description**:  NoName-Surveys is an open-source survey platform that allows users to create, share, and fill out anonymous surveys. /
There are limited and unlimited access options:
- **limited surveys** can be accessed only by specified users, and filled out only once.
- **unlimited surveys** can be accessed by anyone.

**Technology stack**: frontend is written in Svelte (TypeScript) and backend is written in FastAPI (Python). Database can be anything that is supported by SQLAlchemy. For cryptography stuff on the user side, we've used Rust (WebAssembly).

## Dependencies
- npm
- Python

## Setup
to run the app you can use prebuilt images from dockerhub for [frontend]() and [backend]():
- ```sh
  docker compose up
    ```

or build it locally:
- ```sh
  docker compose -f "docker-compose.local.yml" up --no-deps --build
  ```
you have to set up the needed environment variables (.env files in the frontend/backend directory):
- frontend:
  ```sh
  AUTH_GOOGLE_ID = "<google_client_id>" # used for oauth2.0 authentication
  AUTH_GOOGLE_SECRET = "<google_client_secret>" # used for oauth2.0 authentication
  AUTH_GITHUB_ID = "<github_client_id>" # used for oauth2.0 authentication
  AUTH_GITHUB_SECRET = "<github_client_secret>" # used for oauth2.0 authentication
  AUTH_USOS_ID="<usos_consumer_key>" # used for usos oauth1 authentication
  AUTH_USOS_SECRET="<usos_consumer_secret>" # used for usos oauth1 authentication
  AUTH_USOS_BASE_URL="<usosapi_base_url>" # used for usos oauth1 authentication
  BACKEND_HOST = "http://backend:8000" # change it if docker is not used
  ORIGIN = "http://localhost:3000" # change it if docker is not used
  AUTH_SECRET = "<random_string>" # used for auth.js token generation
  ```
- backend:
  ```sh
  SETTINGS_db_type = "" # database type (postgresql)
  SETTINGS_db_dialect =  "" # can be left empty
  SETTINGS_db_user = "" # database username
  SETTINGS_db_password = "" # database password
  SETTINGS_db_host = "" # database server address
  SETTINGS_db_port = "" # database server port
  SETTINGS_db_name = "" # database name
  ```

## Open source licensing info
1. [LICENSE](LICENSE)
