from log_config.filters import DefaultLogFilter
from sys import stdout


logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': ('[{asctime}]  #{levelname:8}  {filename:}({lineno})  -  {name}\n'
                       '    {message}'),
            'style': '{'
        }
    },
    'filters': {
        'default_filter': {
            '()': DefaultLogFilter
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['default_filter'],
            'stream': stdout
        },
        'stderr': {
            'class': 'logging.StreamHandler'
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['default_filter'],
            'stream': stdout
        }
    },
    'loggers': {
        '__main__': {
            'level': 'INFO',
            'handlers': ['default']
        },
        'command_handlers': {
            'level': 'INFO',
            'handlers': ['default']
        },
    },
    'root': {
        'level': 'DEBUG',
        'formatter': 'default',
        'handlers': ['default']
    }
}
