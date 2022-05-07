
def one():
    print("one")


if __name__ == '__main__':
    one()
else:
    # 被别的模块导入时执行
    print("I'm Been Imported")


