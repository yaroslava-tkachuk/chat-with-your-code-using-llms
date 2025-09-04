import os


def __validate_env_var(var_name: str) -> None:
    if not os.getenv(var_name):
        raise EnvironmentError(f"{var_name} not found in environment variables")


def validate_env() -> None:
    requred_env_vars = ["OPENAI_API_KEY", "GITHUB_TOKEN", "ACTIVELOOP_TOKEN", "DATASET_PATH"]
    for var in requred_env_vars:
        __validate_env_var(var)
