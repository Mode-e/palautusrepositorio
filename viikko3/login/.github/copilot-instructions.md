# Copilot Instructions

## Build and test

- Install the project and its development dependencies with `uv sync`.
- Start the Flask app from the project root with `uv run python src/index.py`. The browser tests expect it to be available at `http://localhost:5001`; keep it running in a separate terminal.
- Run all browser tests with `uv run robot src/tests`.
- Run one suite with `uv run robot src/tests/login.robot`, or one test case with `uv run robot --test "Login With Correct Credentials" src/tests/login.robot`.
- Robot Framework tests use a visible Chromium browser by default. To run headlessly, pass `--variable HEADLESS:true` to the Robot command.

## Architecture and conventions

- `src/app.py` defines Flask routes and handles form submissions; `src/index.py` is the development entry point. User validation and credential checks belong in `src/services/user_service.py`, while persistence behavior belongs in `src/repositories/user_repository.py`.
- The repository is currently an in-memory singleton, shared with the service through module imports. `src/entities/user.py` is the user model.
- HTML pages are Jinja templates in `src/templates/`; they extend `layout.html`. Form errors are flashed and the user is redirected back to the form.
- End-to-end tests are Robot Framework Browser suites in `src/tests/`. They share browser setup and URLs from `resource.robot`; suite setup uses `AppLibrary.py` to reset the app or create users through its HTTP endpoints. Keep the app running while executing these tests.
