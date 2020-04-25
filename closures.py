#nested functon
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()

if __name__ == '__main__':
    outerFunction('Hey !')

#closure
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction

if __name__ == '__main__':
    myFunction = outerFunction('Hey !')
    myFunction()

#
import logging
logging.basicConfig(filename='example.log', level = logging.INFO)

def loger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__ , args)
            )
        print(func(*args))

    return log_func

def add(x, y):
    return x+y
def sub(x, y):
    return x-y

add_logger = loger(add)
sub_logegr = loger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logegr(10,5)
sub_logegr(20, 19)
