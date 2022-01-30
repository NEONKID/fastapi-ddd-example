from fastapi import FastAPI


def add_routes(routes, app: FastAPI):
    for route in routes:
        app.include_router(route)
