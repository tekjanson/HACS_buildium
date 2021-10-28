"""Define buildium_iot-wide constants."""

DOMAIN = "buildium_iot"

CONFIG_ENTRY = "config_entry"
CONFIG_ENTRY_OLD = "config_entry_old"
UNSUB_LISTENERS = "unsub_listeners"

FOLDER = "buildium_iot"

UNPINNED_VERSION = "_unpinned_version"

ATTR_INSTALLED_VERSION = "installed_version"
ATTR_SOURCES = "sources"
ATTR_VERSION = "version"

CONF_ALLOW_ALL_IMPORTS = "allow_all_imports"
CONF_HASS_IS_GLOBAL = "hass_is_global"
CONF_BUILDIUM_CLIENT_ID = "buildium_client_id"
CONF_BUILDIUM_SECRET = "buildium_secret"
CONF_INSTALLED_PACKAGES = "_installed_packages"

SERVICE_JUPYTER_KERNEL_START = "jupyter_kernel_start"

LOGGER_PATH = "custom_components.buildium_iot"

REQUIREMENTS_FILE = "requirements.txt"
REQUIREMENTS_PATHS = ("", "apps/*", "modules/*", "scripts/**")

WATCHDOG_OBSERVER = "watch_dog_observer"
WATCHDOG_TASK = "watch_dog_task"

ALLOWED_IMPORTS = {
    "black",
    "cmath",
    "datetime",
    "decimal",
    "fractions",
    "homeassistant.const",
    "isort",
    "json",
    "math",
    "number",
    "random",
    "re",
    "statistics",
    "string",
    "time",
    "voluptuous",
}
