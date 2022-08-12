from abc import ABCMeta, abstractmethod

# 抽象类及抽象方法示例


class Entity(metaclass=ABCMeta):

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):

    # 抽象方法必须要被子类实现
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


if __name__ == "__main__":
    document = Document()
    document.set_title("Hello, LeonardoEzio")

    print(document.get_title())

    # 抽象类不能被实例化
    # entity = Entity()