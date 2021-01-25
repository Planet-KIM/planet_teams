import os
from bcrypt import *
import json


# random_value1 = random_value.encode('utf-8')
# check = checkpw(random_value, str(random_value1).encode('utf-8'))


def make_random_key_txt():
    value = str(os.urandom(32))

    random_value = (hashpw(value.encode('UTF-8'), gensalt())).decode('utf-8')

    folder = 'api-key'

    if os.path.isdir(folder) is True:

        file = open(os.path.join(folder, 'planet_auth.json'), 'w')
        file.write(value + '\n')
        file.write(random_value)
        file.close()

        return random_value

    else:
        os.makedirs(folder)
        file = open(os.path.join(folder, 'planet_auth.json'), 'w')
        file.write(value + '\n')
        file.write(random_value)
        file.close()
        return random_value


def make_random_key_json():
    #32비트로 랜덤값 부여
    value = str(os.urandom(32))
    #
    random_value = (hashpw(value.encode('UTF-8'), gensalt())).decode('utf-8')

    folder = 'api-key'

    key_json = {}
    if os.path.isdir(folder) is True:
        key_json['random32'] = value
        key_json['planetkey'] = random_value

        with open(os.path.join(folder, 'planet_auth.json'), 'w', encoding='utf-8') as jsonfile:
            json.dump(key_json, jsonfile, ensure_ascii=False, indent='\t')

        return json.dumps(key_json, ensure_ascii=False, indent='\t')

    else:
        os.makedirs(folder)
        key_json['random32'] = value
        key_json['planetkey'] = random_value

        with open(os.path.join(folder, 'planet_auth.json'), 'w', encoding='utf-8') as jsonfile:
            json.dump(key_json, jsonfile, ensure_ascii=False, indent='\t')

        return json.dumps(key_json, ensure_ascii=False, indent='\t')


def descript_random_key(filename):
    return ''


make_random_key_json()
