# Fastapi Docker PostgreSQL Test Example
This demonstrates how to test FastAPI endpoints reliant on a PostgreSQL database with Docker.
## Prerequisites

The following are must be installed to run the backend:

- Python 3.11
- pipenv (pip3 install pipenv)

## Project Commands

### Project Setup

 * **Install dependancies:**
  
```bash

make install

```

 * **Activate Environment:**
  
```bash

make activate

```

### Run Uvicorn Server

 * **To start the Uvicorn server in development mode:**
  
```bash

make run

```

 * **Remove the database and start the Uvicorn server in development mode:**
  
```bash

make clean-run

```


### Generate Requirements

* **Generate the requirements for the project:**
  
```bash

make generate_requirements_txt

```

### Test The Project

* **Run local tests:**
  
```bash
make test
```

* **Get test coverage:**
  
```bash
make test-coverage
```