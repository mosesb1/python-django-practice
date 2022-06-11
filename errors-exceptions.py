# try except finally
try:
    print('10' + 10)
except IOError:
    print('You have an input/output error')
except TypeError:
    print('You are using the wrong data types')
except:
    print('hey you got an error')
else:
    print('else block ran')
finally:
    print('finally block ran')