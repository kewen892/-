# AI 绘画服务 - 端口 8068
# 直接返回测试图片，确保能运行
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# 跨域，允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 绘图接口
@app.post("/api/generate_image")
def generate_image(data: dict):
    prompt = data.get("prompt", "漫剧画面")
    print(f"收到绘图请求：{prompt}")
    
    # 返回一张可直接显示的测试图片（不会报错、能正常显示）
    return {
        "image": "https://picsum.photos/800/450"
    }

if __name__ == "__main__":
    print("=" * 50)
    print("   AI 绘画服务启动成功！端口：8068")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8068)