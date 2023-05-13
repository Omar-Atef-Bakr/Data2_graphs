import ctypes
import os


os.add_dll_directory("C:/Users/Omar/Documents/code/DataStruct2/graphs/src/")
clib = ctypes.CDLL("C:/Users/Omar/Documents/code/DataStruct2/graphs/src/main.so", winmode=0)
clib.main()
ret = clib.fun()



print("\n", ret)