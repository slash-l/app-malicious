# 用户原本的安全代码（无需修改）
import pickle

def load_model(path):
    with open(path, 'rb') as f:
		# print(f.read()[:20])  # 查看文件头是否符合pickle格式
        return pickle.load(f)

# 用户加载模型文件
model = load_model('malicious_model.pkl')

