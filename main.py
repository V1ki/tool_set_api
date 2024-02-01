from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

app = FastAPI()

# 检查 static 目录是否存在, 不存在则创建
if not os.path.exists("./static"):
    os.mkdir("./static")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # 指定 ssl 证书
    uvicorn.run(app, host="0.0.0.0", port=443,
                ssl_keyfile="./ssl/site.key", ssl_certfile="./ssl/site_bundle.crt",
                )
