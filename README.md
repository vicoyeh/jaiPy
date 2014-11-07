jaiPy
==========

jaiPy is a Python wrapper for JAI Jai_Factory.dll. The goal is to provide a Python interface for controlling JAI cameras directly. The Python wrapper allows the user to run Python code in normal Python IDE instead of running .NET SDK class wrappers in IronPython (developed by the official JAI company). jai.py is bascially translating the low level C API into python using ctypes library. The C sample code is written in the offical JAI documentation.

##Unsolved issue
jai.py is running successfully before line 101:
  dll.J_Camera_ExecuteCommanda

Currently, jai.py can start J_Factory and J_Camera (return values are correct). It will open an empty view window on line 93. However, the camera fails to execute image acquisition on line 101. The view window does not display live images while the camera is recording. 

I contacted JAI technical support, but apparantly this problem is new to them and they aren't planning to develop a python wrapper at this point.

Please email me if anyone is interested in continuing the project.


