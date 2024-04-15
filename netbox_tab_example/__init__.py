from netbox.plugins import PluginConfig

from .version import __version__

class TabExampleConfig(PluginConfig):
    name = "netbox_tab_example"
    verbose_name = "Tab example"
    description = "An example NetBox plugin"
    version = __version__
    author = "Markku Leiniö"
    required_settings = []
    default_settings = {}

config = TabExampleConfig
