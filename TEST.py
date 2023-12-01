import os, sys, platform
 
os.system('test_enc')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf aws1.so aws32.so')
