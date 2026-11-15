# WebLogin – Agent Instructions

## Project

This is a Python Flask web application for the University of Helsinki Software Production course.

The project uses `uv` for dependency management. Run all commands from the `viikko3/login` directory.

## Running the application

Install dependencies:

    uv sync

Start the Flask application:

    uv run python src/index.py

The application runs at http://localhost:5001.

## Acceptance tests

Tests use Robot Framework and the Browser library with Chromium.

The Flask application must be running before executing browser tests.

Run all tests:

    uv run robot --variable HEADLESS:true src/tests

Run only registration tests:

    uv run robot --variable HEADLESS:true src/tests/register.robot

Install Chromium if needed:

    uv run rfbrowser install chromium

## Project structure

- `src/app.py` – Flask routes
- `src/index.py` – application entry point
- `src/services/user_service.py` – user registration, login and validation
- `src/repositories/user_repository.py` – in-memory user repository
- `src/templates/` – HTML templates
- `src/tests/` – Robot Framework acceptance tests
- `src/AppLibrary.py` – test setup and application reset helpers

## Validation

Username and password validation belongs in the `validate` method of `UserService` in `src/services/user_service.py`.

The existing requirements include a minimum username length of 3 characters and a minimum password length of 8 characters.

Use acceptance tests to specify and verify new requirements before implementing them.

## Working instructions

- Make changes only within the WebLogin project.
- Write acceptance tests before implementing new functionality.
- Run relevant tests after making changes.
- Keep existing tests passing.
- Do not commit generated test reports, virtual environments or cache files.
