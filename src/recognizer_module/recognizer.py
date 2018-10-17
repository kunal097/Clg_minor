#!/usr/bin/python3

# import necessary module
import numpy as np
import cv2



# function to identify the face
# arguments -> dictionary of student_id as key and student_name as value

def identify(info_dic,path):
	# create classifier object using haar cascade
	face_cascade = cv2.CascadeClassifier('recognizer_module/data/haarcascade_frontalface_default.xml')

	# create object of LBPH face recognizer
	rec=cv2.face.LBPHFaceRecognizer_create()
	# rec.read('trainingdata.yml')


	# load the yml file (trained_model)

	rec.read('recognizer_module/recognizer/trainingdata.yml')
	
	# specify font style
	fontface= cv2.FONT_HERSHEY_SIMPLEX
	# specify font scale
	fontscale=1
	# specify font color
	fontColor=(0,255,0)


	# create webcam object
	# cam=cv2.VideoCapture(0)
	img = cv2.imread(path)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		# detect face using face_cascade object
	# faces = face_cascade.detectMultiScale(gray,1.3,5)
	faces = face_cascade.detectMultiScale(gray,
									    scaleFactor=1.1,
									    minNeighbors=5,
									    minSize=(30, 30))


	for (x,y,w,h) in faces:

		# create rectangle on detected face
		cv2.rectangle(img , (x,y) , (x+w , y+h) ,(255,0,0),2)

		# predict the id and confidence level of the detected face
		id_ , confd = rec.predict(gray[y:y+h , x:x+w])
		print("\n\n@!#@!#@\n")
		print(id_,confd)

		
		# if confidance level is greated than 60 than the rectangle show on the detected face

		# if confd>=60 :
			
		# 	# put the name on the detected as per the actual name saved in database
		# 	name = info_dic[id_]
		# 	cv2.putText(img,name,(x,y+h),fontface,fontscale,fontColor)
		# 	cv2.putText(img,str(confd),(x+w,y+h),fontface,fontscale,fontColor)

	# # show the detected image
	# cv2.imshow('image',img)


	# cv2.waitKey(0)
	# cv2.destroyAllWindows()
# destroy all windows		
		

	# return id and confidence level
	return id_,confd

