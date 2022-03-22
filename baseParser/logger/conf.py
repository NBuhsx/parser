import logging
from app_loggers import get_logger, get_file_handler, get_stream_handler







def main():
    logger.info("Программа стартует")
    package1.process(msg="сообщение")
    logger.warning("Это должно появиться как в консоли, так и в файле журнала")
    logger.info("Программа завершила работу")

if __name__ == "__main__":
    main()