import logging

logger = logging.getLogger("Main")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()

logger_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(logger_formatter)
logger.addHandler(console_handler)