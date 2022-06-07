#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import cv2 as cv


# In[ ]:


emoji1=np.zeros((400,400,3), np.uint8)
cir=cv.circle(emoji1, (100,200),63,(0,200,150),-1)
line=cv.line(emoji1,(70,170),(85,172),(0,100,0),5)
line= cv.line(emoji1,(115,170),(130,172),(0,100,0),5)
line= cv.line(emoji1,(80,215),(120,215),(0,100,0),5)
text=cv.putText(emoji1,"sad",(30,350),2,cv.FONT_HERSHEY_COMPLEX,(0,0,200),3)
cv.imshow('emoji', emoji1)
cv.waitKey(0)


# In[ ]:


emoji2 = np.zeros((400,400,3), np.uint8)
cir=cv.circle(emoji2,(200,200), 70, (255,211,67), -1)
cir=cv.circle(emoji2,(170,180), 6, (155,100,215), -1)
cir=cv.circle(emoji2,(220,180), 6, (155,100,215), -1)
el=cv.ellipse(emoji2,(200,220),(40,30),0,0,180,120,-1)
text=cv.putText(emoji2,"smiley",(30,350),4,cv.FONT_HERSHEY_COMPLEX,(0,255,0),3)
cv.imshow('emoji', emoji2)
cv.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:




