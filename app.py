#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 2022/1/10 9:50 PM

参考: https://github.com/dapr/python-sdk/blob/master/examples/demo_actor/demo_actor/demo_actor_flask.py
"""
from flask import Flask,request
import logging

from dapr.conf import settings

from dapr.clients import DaprClient
from dapr.clients.grpc._state import StateItem
from dapr.clients.grpc._request import TransactionalStateOperation, TransactionOperationType

# code
logging.basicConfig(level=logging.INFO)
DAPR_STORE_NAME = "statestore"

app = Flask('DemoActorService')


# Setup method route
@app.route('/GetMyData/<int:orderId>', methods=['GET'])
def get_my_data(orderId):
    with DaprClient() as client:
        # Using Dapr SDK to save and get state
        result = client.get_state(DAPR_STORE_NAME, "order_" + str(orderId))
        logging.info('Result after get: ' + result.data.decode('utf-8'))
        return {'data': result.data.decode('utf-8')}, 200


@app.route('/GetMyData/<int:orderId>', methods=['POST'])
def save_my_data(orderId):
    with DaprClient() as client:
        # Using Dapr SDK to save and get state
        data = str(request.json)
        client.save_state(DAPR_STORE_NAME, "order_" + str(orderId), data)
        logging.info('Result after save: ' + data)
        return {}, 201


# Run application
if __name__ == '__main__':
    app.run(port=settings.HTTP_APP_PORT)
