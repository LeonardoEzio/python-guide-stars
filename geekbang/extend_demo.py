class Entity:
    def __init__(self, object_type):
        print("parent class init called! object type : "+object_type)
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'Document')
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'Video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return len(self.__video_length)


if __name__ == '__main__':
    harry_potter_book = Document('Harry Potter(Book)', 'J.K.Rowling', 'Forever Do not be........')
    print(harry_potter_book.object_type)
    harry_potter_book.print_title()
    print(harry_potter_book.get_context_length())
