import logging
import logging.config
import sys

import os

logging.config.fileConfig("./test/logging_test.conf")

logger = logging.getLogger(os.path.basename(__file__) + __name__)
logger.debug("test");
logger.info("test");
logger.warning("test");
logger.error("test");