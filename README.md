# stackstorm-hpe-arubacx
Stackstorm integration pack for Aruba CX

This pack allows you to integrate with
[HPE Aruba OS-CX](https://www.arubanetworks.com/resources/hewlett-packard-enterprise/).

## Configuration
Copy the example configuration in [arubaoscx.yaml.example](./arubaoscx.yaml.example) to
`/opt/stackstorm/configs/arubaoscx.yaml` and edit as required.

It must contain:

```
ipaddress - Your Aruba CX switch IP address
username - Aruba-CX Username
password - Aruba-CX Password
version - API version
```

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

Example configuration:

```yaml
---
  ipaddress: "10.10.10.10"
  username: "admin"
  password: "admin"
  version: "v10.4"
```
You can also run `st2 pack config hpecfm` and answer the promts

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

Actions are defined in two groups:

### Individual actions: GET, POST, PUT with under bar will precede each individual action
* ``get_alarms``
* ``get_switches``
* ``get_events``
* ``post_fit``

### Orquestra Workflows: will not
* ``sendsnow``
* ``performfit``
* ``getswitches``
