

### 运行依赖
通过 `dapr init` 启动默认配置 

或手动运行如下服务: 

1. redis: localhost:6379 
2. zipkin: http://localhost:9411 


安装依赖
```bash
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

### 运行服务
https://github.com/dapr/python-sdk/tree/release-1.0/examples/demo_actor

```bash

dapr run --app-id demo-actor --app-port 3000 --dapr-http-port 3500 --components-path ./dapr/components --config  ./dapr/config.yaml -- python app.py

```

## 访问
```bash
# dapr api:
curl http://localhost:3500/v1.0/secrets/my-secret-store/my-secret

curl -X POST -H "Content-Type: application/json" -d '[{ "key": "order_1", "value": "250"}]' http://localhost:3500/v1.0/state/statestore
curl http://localhost:3500/v1.0/state/statestore/order_1



# app api:
curl http://localhost:3000/GetMyData/1
curl -X POST  -H "Content-type: application/json" -d '{"a":1}' http://localhost:3000/GetMyData/1
curl http://localhost:3000/GetMyData/1

```