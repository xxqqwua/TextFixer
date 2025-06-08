# Define the logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
}

# Apply the logging configuration
import logging.config

logging.config.dictConfig(LOGGING_CONFIG)
