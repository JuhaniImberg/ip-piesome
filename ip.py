#!/usr/bin/env python

from bottle import (request, run, get, default_app)

@get("/")
def route_index():
    return request.remote_route[0]

@get("/.json")
@get("/json")
def route_json():
    return {"ip": request.remote_route[0]}

if __name__ == "__main__":
    run(host="0.0.0.0", port=8080)

app = default_app()