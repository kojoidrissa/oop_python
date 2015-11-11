from assignment2 import LogFile, DelimFile

log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same

'''
# text of log.txt
2015-01-21 18:35   this is a log message
2015-01-21 18:35   this is another log message

# text of data.csv
a,b,c,d
1,2,3,4
'''