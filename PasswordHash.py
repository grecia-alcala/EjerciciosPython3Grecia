#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import sys
import hashlib
import hmac
import os
import base64

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generates SHA diggest.')
    parser.add_argument('str', type=str, #nargs=1, 
                    help='The string to be processed')
    parser.add_argument('--salt', dest='salt', action='store_const',
                    const=True, default=False,
                    help='add salt to the hash')
    parser.add_argument('-d', '--dig_alg', required=True,
                choices=['md5', 'sha256', 'sha512'], 
                help='Choose a digest Algorithm [md5, sha256, sha512]')
    parser.add_argument('-c', '--check',  type=str, dest='check', 
                default=None, help='Check the digges against the passphrase')

    args = parser.parse_args()
    str = args.str
    salt = args.salt
    dig_func = getattr(hashlib, args.dig_alg)
    dig_name = args.dig_alg
    check = args.check
    
    if salt:
        if not check:
            salt = os.urandom(16)
            m = dig_func(str)
            m.update(salt)
            print  'hash: %s' % m.hexdigest()
            print  'salt: %s' % base64.urlsafe_b64encode(salt)
        else:
            str,salt = str.split(',')
            m = dig_func(str)
            m.update(base64.urlsafe_b64decode(salt))
            print hmac.compare_digest(m.hexdigest(), check)
            
    else:
        if not check:
            print  dig_func(str).hexdigest()
        else:
            print hmac.compare_digest(dig_func(str).hexdigest(), check)