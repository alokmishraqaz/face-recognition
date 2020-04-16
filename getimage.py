import cv2 
import os 
  
# Read the video from specified path 
def makeimage(data):
    video="students/"+data+".mp4"
    print(video)
    cam = cv2.VideoCapture(video)
  
    try:
        path='recognize/data/'+data
        # creating a folder named data
        if not os.path.exists('recognize/data/'+data):
            os.makedirs('recognize/data/'+data)
  
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
  
    # frame
    currentframe = 0
  
    while(True):
      
        # reading from frame
        ret,frame = cam.read()
  
        if ret:
            # if video is still left continue creating images
            name = path+'/' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
            scale_percent = 100 # percent of original size
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame.shape[0] * scale_percent / 100)
            dim = (width, height)
    # resize image
            resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            img_rotate_90_counterclockwise = cv2.rotate(resized, cv2.ROTATE_90_COUNTERCLOCKWISE)
  
            # writing the extracted images
            cv2.imwrite(name, img_rotate_90_counterclockwise)
  
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
  
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
