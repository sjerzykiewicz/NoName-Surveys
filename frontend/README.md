## Prerequisites

In order to use this app, you need to have `npm` installed.

## Getting started

To start your work, you need to set up your local environment.

```sh
npm install
```

## Running the app

If you want to run app locally, you can use:

```sh
npm run dev
```

## Running the tests

> [!IMPORTANT]
> Before running tests, you need to run backend api.
> To run tests, you can use:

```sh
npm playwright_install
npm run test
```

## Additional information

If you want to use oauth2.0 instead of oauth1.0a, you can check `./demo/outh2.0.md` file.

## General Application Structure

The application is structured as follows:

- **demo/**: Contains an unused OAuth 2.0 example usage.

- **src/**

  - **lib/**: Contains the application library code.
    - **assets/**: Contains graphics.
    - **components/**: Contains Svelte components.
    - **entities/**: Contains classes and enums.
    - **fonts/**: Contains custom fonts and icons.
    - **server/database.ts**: Contains requests to the backend API.
    - **stores/**: Contains initializations for the Svelte stores.
    - **utils/**: Contains often used functions.
    - **translations.ts**: Contains the translations dictionary.
  - **routes/**: Contains all the routes for the application.
    - **api/**: Contains API request handlers.
  - **app.css**: Contains global CSS rules.
  - **app.html**: The page template.
  - **hooks.server.ts**: Contains serverside app-wide functions.

- **static/**: Contains logo icons.

- **tests/**: Contains the tests for the application.

- **wasm/**: Contains the cryptographic module.
