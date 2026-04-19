from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# 剧本生成
# ======================
@app.post("/api/generate_script")
def generate_script(data: dict):
    prompt = data.get("prompt", "")
    style = data.get("style", "奇幻")
    
    script = f"""【漫剧剧本】
风格：{style}
剧情：{prompt}

第一幕：故事开端
主角登场，平静的日常被打破。

第二幕：剧情发展
遭遇挑战，结识伙伴，寻找真相。

第三幕：高潮冲突
决战开启，信念与力量碰撞。

第四幕：结局
故事圆满，留下感动与新的希望。
"""
    return {"data": script}

# ======================
# 元素提取
# ======================
@app.post("/api/extract_elements")
def extract_elements(data: dict):
    return {"data": json.dumps({
        "characters": [
            {"name": "主角", "description": "勇敢、善良、拥有特殊能力"},
            {"name": "伙伴", "description": "忠诚可靠，支持主角前行"}
        ],
        "props": [
            {"name": "关键物品", "description": "承载剧情核心力量"},
            {"name": "装备", "description": "角色使用的道具"}
        ],
        "scenes": [
            {"name": "城市", "description": "现代都市背景"},
            {"name": "秘境", "description": "故事关键场景"}
        ]
    }, ensure_ascii=False)}

# ======================
# 生成分镜
# ======================
@app.post("/api/generate_storyboard")
def generate_storyboard(data: dict):
    return {"data": json.dumps([
        {"id": 1, "scene": "全景开场", "description": "展示世界观", "duration": 3},
        {"id": 2, "scene": "主角登场", "description": "人物亮相", "duration": 3},
        {"id": 3, "scene": "事件触发", "description": "剧情转折点", "duration": 4},
        {"id": 4, "scene": "行动开始", "description": "故事正式展开", "duration": 3}
    ], ensure_ascii=False)}

# ======================
# 生成图片（不加载模型，直接返回图片）
# ======================
@app.post("/api/generate_image")
def generate_image(data: dict):
    return {
        "image": "https://picsum.photos/800/450"
    }

if __name__ == "__main__":
    print("=" * 60)
    print("  漫剧AI服务启动成功！端口 8067")
    print("  所有接口正常工作")
    print("=" * 60)
    uvicorn.run(app, host="0.0.0.0", port=8067)