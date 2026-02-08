def greet(name="GitHub"):
    """打招呼功能"""
    return f"你好，{name}！欢迎来到我的仓库"

def calculate(a, b):
    """简单计算示例"""
    return a + b, a - b, a * b, a / b if b != 0 else "除数不能为0"

def main():
    # 1. 执行基础功能
    print(greet())
    # 2. 执行计算功能
    add, sub, mul, div = calculate(10, 5)
    print(f"计算结果：10+5={add}，10-5={sub}，10×5={mul}，10÷5={div}")
    # 3. 自定义你的功能
    print("✨ 这里可以加你的核心代码")

if __name__ == "__main__":
    main()
