import requests
import json
import sys
import os.path

sys.path.append('../../lib')

import auth
import config

if __name__ == '__main__':
    res = requests.get(config.getUrl('/storage/v1/files'), headers=auth.get_headers(config.apiKey, config.apiSecret))
    print(json.dumps(json.loads(res.text), indent=2, ensure_ascii=False))
