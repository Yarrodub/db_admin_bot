from logging import Filter


class DefaultLogFilter(Filter):
    def filter(self, record):
        return True
