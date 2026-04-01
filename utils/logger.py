import logging

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    logger.propagate = False

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(message)s"
        )

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger