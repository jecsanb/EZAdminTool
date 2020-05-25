import logging

FORMAT = '%(asctime)-15s %(levelname)s : %(message)s'


class Logger:
    def __init__(self, logger_name):
        # create logger
        self.log= logging.getLogger(logger_name)
        self.log.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter(FORMAT))
        self.log.addHandler(ch)
def main():
    logger = Logger("test")
    # 'application' code
    logger.log.debug('debug message')
    logger.log.info('info message')
    logger.log.warning('warn message')
    logger.log.error('error message')
    logger.log.critical('critical message')
if __name__ == '__main__':
    main()