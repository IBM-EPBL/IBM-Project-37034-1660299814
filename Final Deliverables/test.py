 import keras.models immport load_model
 import cv2
 import numpu as np
import os
 as.environ[TF-CP_MIN_LOG_LEVEL']='2'
 val=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
 model=load_,odel('aslpng.h5')
 from skimage.transform import resize
 def detect(frame):
 img= resize(frame,(64,64,1))
 img= np.expand_dims(img,axis=0))
 if(np.max(img)>1);
 img=img/255.0
 predict_x=model.predict(img)
 print(predict_x)
 predtict=np.argmax(predict_x,axis=1)
 x=predict[0]
 print(val[x])
 frame=cv2.imread(r"c/C:\Users\GCE\Desktop\ibm\Realtime_Communicati
on_System_For_Specially_Abled\Dataset\test_set\B\1.png
 data=detect(frame)