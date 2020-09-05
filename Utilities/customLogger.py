import logging

class LogGen:
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r'D:\NopCommerceApp\Logs\Automation.log',
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='w')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger