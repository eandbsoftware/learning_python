class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self, data):
        assert False, 'converter must be defined'

class Upperclass(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

class StdinGetter:
    def readline(self):
        return input('enter some text: ')

if __name__ == '__main__':
    import sys, os
    # print(os.getcwd())
    # obj1 = Upperclass(open(r'resources\trispam.txt', 'r'), sys.stdout)
    # obj1.process()

    # obj2 = Upperclass(open(r'resources\trispam.txt', 'r'), open(r'resources\trispamup.txt', 'w'))
    # obj2.process()

    Upperclass(open(r'resources\trispam.txt', 'r'), HTMLize()).process()
    print()
    
    Upperclass(StdinGetter(), HTMLize()).process()
    
