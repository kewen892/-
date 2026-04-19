# 最简单的文本AI服务，端口 8067，绝对能跑
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

# 允许跨域（网页能访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 剧本生成
@app.post("/api/generate_script")
def generate_script(data: dict):
    prompt = data.get("prompt", "")
    style = data.get("style", "")
    return {
        "data": f"【AI 生成剧本】\n风格：{style}\n\n这是一个测试剧本，服务启动成功！\n输入内容：{prompt}"
    }

# 元素提炼
@app.post("/api/extract_elements")
def extract_elements(data: dict):
    return {
        "data": json.dumps({
            "characters": [{"name": "主角", "description": "测试角色"}],
            "props": [{"name": "道具", "description": "测试道具"}],
            "scenes": [{"name": "场景", "description": "测试场景"}]
        }, ensure_ascii=False)
    }

# 分镜生成
@app.post("/api/generate_storyboard")
def generate_storyboard(data: dict):
    return {
        "data": json.dumps([
            {"id": 1, "scene": "开场", "description": "测试分镜1", "duration": 3},
            {"id": 2, "scene": "发展", "description": "测试分镜2", "duration": 4}
        ], ensure_ascii=False)
    }

if __name__ == "__main__":
    print("=" * 50)
    print("  文本AI服务启动成功！端口：8067")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=8067)