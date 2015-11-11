import abc
import datetime

class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, filename):
        self.filename = filename

    @abc.abstractmethod
    def write(self):
        return

    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()


class LogFile(WriteFile):
    def write(self, message):
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.write_line(dt_str + "    " + message)


class DelimFile (WriteFile):
    def __init__(self,filename,delim):
        super(DelimFile, self).__init__(filename)
        self.delim = delim

    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)

