from ctypes import *

def main():
	
	#load dll
	dll = windll.LoadLibrary(r'C:\Program Files\JAI\SDK\bin\Jai_Factory.dll')
	
	J_CAMERA_ID_SIZE = 512
	J_ST_SUCCESS = 0
	
	print "flag"
	
	#list of ctypes variables
	hFactory = c_long() #factory handle
	hCamera = c_long()	#camera handle
	retval = c_int()	#capture return value from the functions
	bHasChanged = c_bool() 
	nCameras = c_uint32() #number of cameras
	sCameraId = (c_int8*J_CAMERA_ID_SIZE)() 
	size = c_uint32()
	
	retval = dll.J_Factory_Open("", pointer(hFactory))
	if (retval == J_ST_SUCCESS):
		#search for cameras on all the networks
		retval = dll.J_Factory_UpdateCameraList(hFactory, pointer(bHasChanged))
		if ((retval == J_ST_SUCCESS) and bHasChanged):
			retval = J_Factory_GetNumOfCameras(hFactory, pointer(nCameras))
			print("%d cameras are detected")%nCameras
			
			
			if ((retval == J_ST_SUCCESS) and nCameras > 0):
				#get the first camera in the camera list
				index = c_uint32(0)
				retval = dll.J_Factory_GetCameraIDByIndex(hFactory, index, sCameraId, pointer(size))
				
				if (retval == J_ST_SUCCESS):
					print("Camera is returned successfully")
				
				else: 
					print("Camera cannot be returned")
			else:
				print("No camera is found")
		else:
			print("Camera list is not updated")
	else:
		print("Failed to open factory")
		
		
if __name__ == '__main___':
	print "here"
	main()
