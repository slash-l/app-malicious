import pickle
import pickletools
import sys

def analyze_pickle(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # 检查文件头是否包含非pickle数据
        if not data.startswith(b'\x80'):  # 常见pickle协议头
            print("文件可能包含非pickle数据")
            # 尝试找到真正的pickle数据开始位置
            pickle_start = data.find(b'\x80')
            if pickle_start > 0:
                data = data[pickle_start:]
        
        pickletools.dis(data)
    except (ValueError, pickle.UnpicklingError) as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python script.py <pickle文件路径>")
        sys.exit(1)
    analyze_pickle(sys.argv[1])


