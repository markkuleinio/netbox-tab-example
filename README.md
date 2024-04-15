# NetBox Tab Example Plugin

This is an example plugin for NetBox, showing a new "Tab Example"
tab in the prefix view.


## Installation

```shell
cd /opt/netbox
sudo venv/bin/pip install git+https://github.com/markkuleinio/netbox-tab-example
sudo sh -c "echo git+https://github.com/markkuleinio/netbox-tab-example >> local_requirements.txt"
```

Add the plugin in the NetBox plugins configuration list in `/opt/netbox/netbox/netbox/configuration.py`:

```python
PLUGINS = ["netbox_tab_example"]
```

Restart NetBox:

```shell
sudo systemctl restart netbox netbox-rq
```
