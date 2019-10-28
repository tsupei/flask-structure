# Introduction

The basic structure of flask as a service providing server.

# Structure

```bash
├── README.md
├── api
│   ├── __init__.py
│   └── hello_api.py
├── application.yml
├── config
│   └── __init__.py
├── requirements.txt
├── service
│   ├── __init__.py
│   └── hello_service.py
├── start.py
└── start.sh

# /api - api 
# /service - services that could be called by api
# /config - all configuration
# application.yml - serve as a setting file
# start.py - main file
```

# How to expand?

When adding a service, do it in the following steps

1. Add a service in `/service`
2. Create an api in `/api`
3. Register the api in `start.py`

