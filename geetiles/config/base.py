"""-"""

import os
from geetiles.utils.files import BASE_DIR
from dotenv import load_dotenv

load_dotenv()

SETTINGS = {
    'logging': {
        'level': 'DEBUG'
    },
    'service': {
        'port': os.getenv('PORT')
    },
    'redis': {
        'url': os.getenv('REDIS_URL')
    },
    'gee': {
        'service_account': 'earth-engine@notional-impact-169016.iam.gserviceaccount.com',
        'privatekey_file': BASE_DIR + '/privatekey.json'
    },
    'storage': {
        "bucket": os.getenv('GOOGLE_CLOUD_BUCKET')
    }
}
