# -*- encoding:utf-8 -*-
# __Author__:yuslience
from logger_test.logconf import get_share_logger

logger = get_share_logger("test_log")

if __name__ == "__main__":
    logger.info("this is info1111")

