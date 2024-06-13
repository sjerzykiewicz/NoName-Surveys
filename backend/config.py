
from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    envvar_prefix="SETTINGS",
    default_env="dev",
    settings_files=['settings.toml'],
)
