from setuptools import setup

setup(
    name="torchtriton",
    version="99.0.0",
    packages=["torchtriton"],
    install_requires=["requests"],  # 确保依赖requests库
)

print("[torchtriton] Setup complete!")
