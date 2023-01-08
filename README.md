# smauto-server
REST API implementation for [SmAuto](https://github.com/robotics-4-all/smauto-dsl).

## Installation

Clone this repository

```
git clone https://github.com/robotics-4-all/smauto-server && cd smauto-server
```

Install package and runtime dependencies

```
pip install .
```

Install uvicorn WSGI server. We will use this to launch our API.

```
pip install uvicorn
```

## Usage

Launch the API server with (under the base directory of this repo):

```
uvicorn smauto_server.smauto_server:api --reload --workers 1 --host 0.0.0.0 --port 8080
```

The output should match the below:

```
INFO:     Will watch for changes in these directories: ['/home/klpanagi/development/smauto/smauto-server']
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:     Started reloader process [3867604] using StatReload
```

This means that you can access the API locally via `http://localhost:8080`.

Furthermore, you can access the UI for accessing the endpoints via your
preferred web browser at `http://localhost:8080/docs`

![2023-01-08-153513_1543x470_scrot](https://user-images.githubusercontent.com/4770702/211198940-2ee67e2c-5d8c-4820-ab16-d7fa21226bf8.png)
