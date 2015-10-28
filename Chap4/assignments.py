class WriteFile(object):
    def __init__(self, filename):
        self.fh = open(filename, "x")

    def write(self):
        self.fh.write()

class LogFile(WriteFile):
    def write(self, message):
        import datetime
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        fh.write(dt_str + message)

class DelimFile (WriteFile):
