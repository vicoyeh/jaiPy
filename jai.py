from ctypes import *




def main():
	
	#load dll
	dll = windll.LoadLibrary(r'C:\Program Files\JAI\SDK\bin\Jai_Factory.dll')
	
	J_CAMERA_ID_SIZE = 512
	J_ST_SUCCESS = 0

	
	#list of ctypes variables
	hFactory = c_void_p() #factory handle
	hCamera = c_void_p()	#camera handle
	retval = c_int()	#capture return value from the functions
	bHasChanged = c_bool() 
	nCameras = c_uint32() #number of cameras
	sCameraId = (c_int8*J_CAMERA_ID_SIZE)() 
	size = c_uint32(J_CAMERA_ID_SIZE)
	
	
	#sys.path.append('C:\Users\lab\Desktop\Vic')
	
	class J_tIMAGE_INFO(Structure):
		_fields_ = [('iPixelType', c_uint32),
				('iSizeX', c_uint32),
				('iSizeY', c_uint32),
				('iImageSize',c_uint32),
				('pImageBuffer',POINTER(c_uint8)),
				('iTimeStamp',c_uint64),
				('iMissingPackets',c_uint32),
				('iAnnouncedBuffers',c_uint32),
				('iQueuedBuffers',c_uint32),
				('iOffsetX',c_uint32),
				('iOffsetY',c_uint32),
				('iAwaitDelivery',c_uint32),
				('iBlockId',c_uint32)]
	
	
	#image acquisition variables
	g_hView = c_void_p() #global view handle
	hThread = c_void_p()
	
	ViewSize = (c_int*2)()
	ViewSize[0] = c_int(500) #window width
	ViewSize [1]= c_int(500) #window height
	
	TopLeft = (c_int*2)() #top-left corner 
	TopLeft[0] = c_int(100) #top-left corner x-coord
	TopLeft[1] = c_int(100) #top-left corner y-coord 
	
	#CALLBACKFUNC = CFUNCTYPE(None,POINTER(J_tIMAGE_INFO))
	TESTFUNC = CFUNCTYPE(None)
	
	#def StreamCBFunc(pImageInfo):
	#	dll.J_Image_ShowImage(g_hView,pImageInfo)
		
	def test():
		print "yes"
		
	#call_back = CALLBACKFUNC(test)
	call_back = TESTFUNC(test)
	#call_back_content = cast(call_back,c_void_p)
	#vfptr = cast(call_back,c_void_p).value
	#ptr=cast(StreamCBFunc,pointer(c_void_p))
	#ptr()
	
	
	#open factory
	retval = dll.J_Factory_Open("", pointer(hFactory))
	if (retval == J_ST_SUCCESS):
		#search for cameras on all the networks
		retval = dll.J_Factory_UpdateCameraList(hFactory, pointer(bHasChanged))
		if ((retval == J_ST_SUCCESS) and bHasChanged):
			retval = dll.J_Factory_GetNumOfCameras(hFactory, pointer(nCameras))
			print nCameras," cameras are detected" 
			
			
			if ((retval == J_ST_SUCCESS) and nCameras > 0):
				#get the first camera in the camera list
				index = c_uint32(0) #index of the first camera
				retval = dll.J_Factory_GetCameraIDByIndex(hFactory, index, sCameraId, pointer(size))
				
				if (retval == J_ST_SUCCESS):
					print "Camera ", index, " = ", sCameraId	
					retval = dll.J_Camera_Open(hFactory, sCameraId, pointer(hCamera))
	
					print "Camera opened successfully"
					
					retval = dll.J_Image_OpenViewWindow(c_char_p("Live Window"),pointer(TopLeft),pointer(ViewSize),pointer(g_hView))
					if (retval == J_ST_SUCCESS):
						print "Window opened successfully"
						
						#retval = dll.J_Image_OpenStreamLight(hCamera,0,pointer(hThread))
						retval=dll.J_Image_OpenStream(hCamera,0,None, call_back, byref(hThread),ViewSize[0]*ViewSize[1]*6)
						print retval
						if (retval == J_ST_SUCCESS):
							print dll.J_Camera_ExecuteCommand(hCamera,"AcquisitionStart") #Start Image Acquisition
							print "Start Image Acquisition"
					
					
					#retval = dll.J_Camera_Close(hCamera)
					#print "Camera closed successfully"
					
				else: 
					print "Camera cannot be returned" 
			else:
				print "No camera is found" 
		else:
			print "Camera list is not updated" 
	else:
		print "Failed to open factory" 
		
		
if __name__ == '__main___':
	main()
