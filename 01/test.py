import sys, os, platform

print(f'{os.getlogin()} @ {platform.node()}:{platform.system()}.{platform.release()}')
print(sys.version)