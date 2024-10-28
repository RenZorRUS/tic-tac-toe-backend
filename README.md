# Tic Tac Toe (Backend)

## Overview

**Tic-tac-toe** (*noughts and crosses* or *Xs and Os*) - is a paper-and-pencil game for 2 players who take turns marking the spaces in a 3-by-3 grid with `X` or `O`.

The player who succeeds in placing 3 of their marks in a horizontal, vertical, or diagonal row is the winner.

## Dependencies

| Name | Description |
| :-- | :-- |
| [Python](https://docs.python.org/3/) | Is a powerful programming language |
| [Uv](https://docs.astral.sh/uv/) | An extremely fast `Python` package and project manager |
| [Ruff](https://docs.astral.sh/ruff/) | An extremely fast `Python` linter and code formatter |
| [Pre-commit](https://pre-commit.com/#2-add-a-pre-commit-configuration) | A framework for managing and maintaining multi-language pre-commit hooks |
| [Uvicorn](https://www.uvicorn.org) | An ASGI web server implementation for Python |
| [FastAPI](https://fastapi.tiangolo.com/) | High performance web framework |
| [MsgSpec](https://jcristharif.com/msgspec/) | A fast serialization and validation library |
| [Docker](https://www.docker.com/) | A platform designed to help developers build, share, and run container applications |
| [Docker Compose](https://docs.docker.com/compose/) | A tool for defining and running multi-container applications |

## How to Install

1. **Clone the repository** into your local machine, using the following command:

    ```bash
    # HTTPS
    git clone https://github.com/RenZorRUS/tic-tac-toe-backend.git
    # SSH
    git clone git@github.com:RenZorRUS/tic-tac-toe-backend.git
    ```

2. **Install the [`Uv` project manager](https://docs.astral.sh/uv/getting-started/installation/)** using the following instruction (skip if already installed):

3. **Create a `Uv` virtual environment** using the following command:

    ```bash
    # Creates `.venv` directory
    uv venv
    ```

4. **Activate the `Uv` virtual environment** using the following command:

    ```bash
    # MacOS & Linux
    source .venv/bin/activate
    # Windows
    .venv\Scripts\activate
    ```

    To deactivate the `Uv` virtual environment, run the following command:

    ```bash
    # MacOS & Linux
    source deactivate
    ```

5. To synchronize all project dependencies (i.e., ensure that they are installed and up-to-date with the lockfile), run the following command:

    ```bash
    # All dependencies
    uv sync
    # Only development dependencies
    uv sync --only-dev
    ```

6. **Install the `pre-commit` hooks** using the following command:

    > **NOTE:**
    >
    > Git hook scripts are useful for identifying simple issues before submission to code review

    As the result `pre-commit` will run automatically on `git commit`

    ```bash
    # Output: pre-commit installed at .git/hooks/pre-commit
    uv run pre-commit install
    ```

    To run the `pre-commit` hooks manually, run the following command:

    ```bash
    # Against the changed files
    uv run pre-commit
    # Against all of the files
    uv run pre-commit run --all-files
    ```

## How to Launch

> **NOTE:** Before launching the backend, please install [Docker](https://docs.docker.com/get-started/get-docker/) platform.

1. Run the backend `Docker` containers using the following command:

    ```bash
    docker compose up --detach --force-recreate --remove-orphans
    # To run containers with re-built images, use the following command:
    docker compose up --detach --force-recreate --remove-orphans --build
    ```

    If you want to launch only specific services, list them in the comment below:

    ```bash
    # docker compose up <OPTIONS...> <SERVICE_NAMES...> 
    docker compose up --detach --remove-orphans database message-queue
    ```

    To shutdown the backend `Docker` containers, use the following command:

    ```bash
    docker compose down --remove-orphans --volumes
    ```

2. To run the backend `Uvicorn` server use the following command:

    ```bash
    # Production mode
    uv run python -OO src/main.py --prod
    # Development mode
    uv run python -OO src/main.py
    ```

## How to Manage Dependencies

1. To add a new dependency to the `pyproject.toml`, run the following command:

    ```bash
    # Necessary project dependency
    uv add <DEPENDENCY_NAME>
    # Development dependency
    uv add --dev <DEPENDENCY_NAME>
    ```

    To add all dependencies from `requirements.txt` file, use the following command:

    ```bash
    uv add --requirements <FILE_PATH>
    ```

2. To remove a dependency from the `pyproject.toml`, run the following command:

    ```bash
    uv remove <DEPENDENCY_NAME>
    ```

3. To export dependencies to `requirements.txt` file, use the following command:

  ```bash
  # All dependencies (with development)
  uv export --output-file requirements.dev.txt --no-hashes
  # Only production dependencies
  uv export --output-file requirements.prod.txt --no-hashes --no-dev
  ```

## References

**Project Set Up:**

- [What is EditorConfig?](https://editorconfig.org/)

**Python:**

- [Caching in Python Using the LRU Cache Strategy](https://realpython.com/lru-cache-python/)
- [How can `dataclasses` be made to work better with `__slots__`?](https://stackoverflow.com/questions/50180735/how-can-dataclasses-be-made-to-work-better-with-slots)

**Security:**

- [Introducing OAuth 2.0](https://web.archive.org/web/20170306105554/http://hueniverse.com/2010/05/15/introducing-oauth-2-0/)
- [OAuth 2.0 and OpenID Connect (in plain English)](https://youtu.be/996OiexHze0?si=FjGnnsLvob0Hq2Ab)

**Asynchronous Execution:**

- [What is Concurrency? And how can Structured Concurrency make it easier?](https://youtu.be/ibxUIL_-LlA?si=ZEVBF7OOomZI-q1B)
- [Python Concurrency for Mere Mortals / Trio (Nathaniel J Smith)](https://youtu.be/i-R704I8ySE?si=66a0yWSNUy0v41wT)

**FastAPI:**

- [Setting up the `uvicorn` logger](https://stackoverflow.com/a/77007723/25203640)
- [MsgSpec integration for FastAPI](https://github.com/iurii-skorniakov/fastapi-msgspec/tree/main#fastapi-msgspec)
- [Structuring FastAPI Project Using 3-Tier Design Pattern](https://levelup.gitconnected.com/structuring-fastapi-project-using-3-tier-design-pattern-4d2e88a55757)
- [A Basic FastAPI Microservice Folder Structure](https://medium.com/@hassaan.saleem0214/a-basic-fastapi-microservice-folder-structure-01a05da43f5b)
- [Best Practices for Structuring Your FastAPI Projects](https://blog.stackademic.com/best-practices-for-structuring-your-fastapi-projects-e66482b27d02)
- [FastAPI Best Practices: A Condensed Guide with Examples](https://www.linkedin.com/pulse/fastapi-best-practices-condensed-guide-examples-nuno-bispo-9pd2e/)
- [101 FastAPI Tips by The FastAPI Expert](https://github.com/Kludex/fastapi-tips?tab=readme-ov-file#101-fastapi-tips-by-the-fastapi-expert)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices#fastapi-best-practices-)

**Git:**

- [Add `.gitattributes` To Your Git Repository](https://dev.to/deadlybyte/please-add-gitattributes-to-your-git-repository-1jld#:~:text=The%20.,file%20is%20created%20or%20saved.)
- [What is `.gitattributes`?](https://git-scm.com/docs/gitattributes)
