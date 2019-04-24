# DC-wrapper 
Docker-Compose v:3
## Use:
This package is meant to aid in the building of complex docker environments (docker-compose).
It follows a very simple usage procedure. Example:
```python
my_compose = Build()
y.build.context('<file-location>')
```
cap_add, cap_drop

## Missing:
service.deploy.rollback_config
service.deploy.update_config
service.healthcheck
service.links -- LEGACY FEATURE