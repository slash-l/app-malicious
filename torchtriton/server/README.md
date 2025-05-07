### 攻击流程分析
1. 用户行为：
执行 pip install torch-nightly → pip默认从PyPI拉取torchtriton（而非PyTorch官方源）。

2. 恶意代码触发：
当用户代码import torch时，torchtriton/__init__.py自动执行，窃取数据。

3. 数据外传：
环境变量和路径通过HTTP发送到攻击者服务器。
