#!/usr/bin/env python

import sys, hashlib

if len(sys.argv) != 2:
    print("Uso: ./hash.py <mensagem>")
    sys.exit(1)

dgst1 = hashlib.md5(sys.argv[1].encode()).hexdigest()
dgst2 = hashlib.sha1(sys.argv[1].encode()).hexdigest()
dgst3 = hashlib.sha224(sys.argv[1].encode()).hexdigest()
dgst4 = hashlib.sha512(sys.argv[1].encode()).hexdigest()

print("--------------=HASHES=------------------")
print("md5 => " + dgst1)
print("sha1 => " + dgst2)
print("sha224 => " + dgst3)
print("sha512 => " + dgst4)
print("----------------------------------------")
