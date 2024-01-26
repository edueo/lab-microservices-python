#!/usr/bin/env python
# -*- coding: utf-8 -*-

from quart import Quart

app = Quart(__name__)


@app.route("/api")
def my_microservice():
    return {'hello': 'world'}


if __name__ == "__main__":

    app.run()
    #  app.run(host="0.0.0.0", port=8000) # para quando a aplicação não estiver rodando no mesmo computador que está sendo desenvolvida
