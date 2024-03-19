import logging


class LogInfoGenerator:

    @staticmethod
    def logGen():
        logging.basicConfig(filename="C:\\Users\\lokes\\PycharmProjects\\seleniumAutomation\\Logs\\TCs.log",
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m/%d/%Y  %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger