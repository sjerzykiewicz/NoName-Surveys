## TL;DR
**NoName Anonymous Surveys** is a fully open-source platform for conducting anonymous surveys. By using linkable ring signatures, it ensures that:
- You can verify that a response is from a member of a specific group.
- The identity of the respondent remains unknown.
- Each user can only respond once.

You can freely use the code, modify it, and host your own instance of the platform - tips for which you can find [here](#Setup). We also welcome contributions from the community.

## Example Use Case
We've set up an example instance for the [University of Adam Miczkiewicz](https://amu.edu.pl/en). You can check it out [here](https://noname-stage.projektstudencki.pl/).

## How To Use
### User's Guide
1. **Generate Keys**
> [!IMPORTANT]
> Your keys are being generated on your device and only the public key is sent to the server.
  - Click on the "Account" button in the navigation bar.
  - Provide a passphrase which will be used to encrypt and decrypt your keys on your device.
  - Click on the "Generate keys" button.
  - Save the generated keys in a place of your choice.

2. **Create a Survey**
  - Click on the "Create" button in the navigation bar.
  - Fill in the survey title and prepare questions.
  - Optionally, you can save a created structure for later by clicking on "Save draft".
  - You can view how the survey will look by clicking on "Preview".
  - When you're ready, click on "Finish".
  - Choose whether you want to specify a group of users who can respond to the survey.
    - **If Yes**:
      - Select "Secure".
      - Choose a group from the list of previously created user groups or specify users by their email addresses.
      - Make sure that all users have registered beforehand and created their keys.
      - Only users from the specified group will be able to respond.
    - **If No**:
      - Select "Public".
      - The survey will be open to everyone.
  - Click on "Finish" to create the survey.

3. **Respond to a Survey**
  - Click on the survey link.
  - Fill in the answers.
  - Click on the "Submit" button.

4. **View Survey Results**
  - TODO

5. **Create a User Group**
  - TODO

## Administrator's Guide
### Dependencies
- npm
- Python

### Setup
To run the app, you can use prebuilt images from DockerHub for [frontend]() and [backend]():
- ```sh
  docker compose up
  ```

Or build it locally:
- ```sh
  docker compose -f "docker-compose.local.yml" up --no-deps --build
  ```

You have to set up the needed environment variables (.env files in the frontend/backend directory):
- frontend:
  ```sh
  AUTH_GOOGLE_ID = "<google_client_id>" # used for oauth2.0 authentication
  AUTH_GOOGLE_SECRET = "<google_client_secret>" # used for oauth2.0 authentication
  AUTH_GITHUB_ID = "<github_client_id>" # used for oauth2.0 authentication
  AUTH_GITHUB_SECRET = "<github_client_secret>" # used for oauth2.0 authentication
  AUTH_USOS_ID="<usos_consumer_key>" # used for usos oauth1.0a authentication
  AUTH_USOS_SECRET="<usos_consumer_secret>" # used for usos oauth1.0a authentication
  AUTH_USOS_BASE_URL="<usosapi_base_url>" # used for usos oauth1.0a authentication
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

## Developers
### Contributing
We welcome contributions from the community. To contribute, please fork the repository, create a new branch, and submit a pull request. Make sure to follow our coding standards and include tests for any new features or bug fixes.

### Open Source Licensing Info
1. [LICENSE](LICENSE)
