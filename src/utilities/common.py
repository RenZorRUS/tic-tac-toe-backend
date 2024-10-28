"""Contains common utilities."""


def get_env_file_name(*, is_production: bool = False) -> str:
    """Get the name of the environment file."""
    return '.env.prod' if is_production else '.env.dev'
