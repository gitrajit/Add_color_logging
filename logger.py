import logging

logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s' ,datefmt='%a %d %b %Y %H:%M:%S', )
log = logging.getLogger()
log.setLevel(logging.INFO)
#Handler for saving to a file
fileHandler = logging.FileHandler(r'tmp.log')
fileHandler.setFormatter(logFormatter)
log.addHandler(fileHandler)

#Handler for printing to console
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)

#for adding color
def add_color(fn):
    
    def data(*args):
        text = copy.copy(args[1].msg)
        levelno = copy.copy(args[1].levelno)
        if (levelno >= 50):
            color = '\x1b[31m'  # red
        elif (levelno >= 40):
            color = '\x1b[31m'  # red
        elif (levelno >= 30):
            color = '\x1b[33m'  # yellow
        elif (levelno >= 20):
            color = '\x1b[32m'  # green
        elif (levelno >= 10):
            color = '\x1b[35m'  # pink
        else:
            color = '\x1b[0m'
        args[1].msg = color + str(text) + '\x1b[0m'

        return fn(*args)

    return data

logging.StreamHandler.emit = add_color(logging.StreamHandler.emit)
