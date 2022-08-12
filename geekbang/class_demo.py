class Document:

    # 常量定义
    WELCOME_STR = "Welcome! the brief context for this book is {}."

    # __init__ 构造函数
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author,
        # __开头代表私有属性
        self.__context = context

    # classmethod 类函数 cls类对象
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context="nothing")

    # staticmethod 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

    def get_context_length(self):
        return len(self.__context)

    def intercept_context(self, length):
        self.__context = self.__context[:length]

    def get_context(self):
        return self.__context


if __name__ == "__main__":
    harry_potter_book = Document("Harry Potter", "J.K.Rowling", "... Forever Do not believe ........")
    print(harry_potter_book.title)
    print(harry_potter_book.author)
    print(harry_potter_book.get_context_length())
    print(harry_potter_book.get_context())
    harry_potter_book.intercept_context(10)
    print(harry_potter_book.get_context_length())
    # 私有属性无法被访问
    # print(harry_potter_book.__context)
    print(harry_potter_book.get_context())

    print("================================")

    print(Document.WELCOME_STR)
    print(Document.get_welcome("the author is too lazy , this book has no content"))
    empty_book = Document.create_empty_book("new Book", "LeonardoEzio")
    print(empty_book.get_context_length())
    print(empty_book.get_context())

