# Python x Slenium Grid Example

Example of using WebDriver remotely from Python.
Automatically mounts the /src directory by default. You can place any program and check its operation.

# Getting Started

## Start Container

Create & start docker container.

```shell
docker compose up -d
```

## Run Python Script

```shell
docker compose exec app python main.py
```

Access to [localhost:7900](http://localhost:7900/?autoconnect=1&resize=scale&password=secret).
You can check the result of the operation by WebDriver.

Access [localhost:4444](http://localhost:4444) to view the overview and sessions.
