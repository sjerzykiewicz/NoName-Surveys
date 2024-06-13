# NoName-Surveys

**Description**:  NoName-Surveys is an open-source survey platform that allows users to create, share and fill anonymous surveys. /
There are limited and unlimited access options:
- **limited surveys** can be accessed only by specified users, and filled only one time.
- **unlimited surveys** can be accessed by anyone.

**Technology stack**: frontend is written in Svelte (TypeScript) and backend is written in FastAPI (python). Database can be anything that is supported by SQLAlchemy. For cryptography stuff on the user side we've used rust (WebAssembly).

## Dependencies
- npm
- python

## Setup
to run the app you can use prebuild images from dockerhub for [frontend]() and [backend]():
- ```sh
    docker compose up
    ```

or build it locally:
- ```sh
    docker compose -f "docker-compose.local.yml" up --no-deps --build
  ```
you have to setup needed enviroment variables (.env files in frontend/backend directory):
- frontend:
  ```sh
    GOOGLE_CLIENT_ID = "<google_client_id>" # used for oauth2.0 authentication
    GOOGLE_CLIENT_SECRET = "<google_client_secret>" # used for oauth2.0 authentication
    BACKEND_HOST = "http://backend:8000" # change it if docker is not used
    ORIGIN = "http://localhost:3000" # change it if docker is not used
    AUTH_SECRET = "<random_string>" # used for auth.js token generation
  ```
  backend:
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

## Credits and references
- [NoName WMI Team](https://git.wmi.amu.edu.pl/s452628/NoName1.0)
