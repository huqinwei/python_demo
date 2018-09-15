class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url
    def who(self):
        print("name: ", self.name)
        print("url: ",self.__url)

    def __foo(self):
        print('private func')
    def foo(self):
        print('public func')
        self.__foo()
X = Site('fuck','www.fuck.com')
X.who()
#X.__foo()
X.foo()
