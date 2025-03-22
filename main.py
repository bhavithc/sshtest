import ssh_remote
import logging

def setup_logger():
    # file_handler = logging.FileHandler('my_app.log')
    # file_handler.setFormatter(formatter)

    return logger


if __name__ == "__main__":


    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    # print(logger)
    logger.debug("Welcome deepak")
    logger.info("executing remote ssh...")
    ssh_remote.main(logger)
    logger.info("remote execution is success !")