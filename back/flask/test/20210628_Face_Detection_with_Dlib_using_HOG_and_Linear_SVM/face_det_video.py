"""
USAGE:
python face_det_video.py -i input/video1.mp4
python face_det_video.py -i input/video1.mp4 -u 1
python face_det_video.py -h
"""

import dlib
import argparse
import cv2
import sys
import time

import process_dlib_boxes

# construct the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default='../../input/test_data/video1.mp4',
                    help='path to the input image')
parser.add_argument('-u', '--upsample', default=None, type=float,
                    help='factor by which to upsample the image, default None, ' + \
                          'pass 1, 2, 3, ...')
args = vars(parser.parse_args())

# initilaize the Dlib face detector
detector = dlib.get_frontal_face_detector()

# capture the video
cap = cv2.VideoCapture(args['input'])

if (cap.isOpened() == False):
    print('Error opening video file. Please check file path...')

# get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# file name for saving the resulting video
save_name = f"{args['input'].split('/')[-1].split('.')[0]}_u{args['upsample']}"
# define codec and create VideoWriter object 
out = cv2.VideoWriter(f"outputs/{save_name}.mp4", 
                      cv2.VideoWriter_fourcc(*'mp4v'), 30, 
                      (frame_width, frame_height))

# for counting the total number of frames
frame_count = 0
# to keep track of the total frames per second
total_fps = 0

while(cap.isOpened()):
    # capture each frame of the video
    ret, frame = cap.read()
    if ret:
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # detect the faces in frame
        if args['upsample'] == None:
            start = time.time()
            detected_boxes = detector(image_rgb)
            end = time.time()
        elif args['upsample'] > 0 and args['upsample'] < 4:
            start = time.time()
            detected_boxes = detector(image_rgb, int(args['upsample']))
            end = time.time()
        else:
            warn_string = 'Please provide usample value > 1 and < 4.' + \
                    ' Else it might lock your CPU.'
            print(warn_string)
            sys.exit(0)

        # get the current fps
        fps = 1 / (end - start)
        # add `fps` to `total_fps`
        total_fps += fps
        # increment frame count
        frame_count += 1

        # draw the boxes on the original frame
        for box in detected_boxes:
            res_box = process_dlib_boxes.process_boxes(box)
            cv2.rectangle(frame, (res_box[0], res_box[1]),
                        (res_box[2], res_box[3]), (0, 255, 0), 
                        2)

        # put the fps text on the current frame            
        # cv2.putText(frame, f"{fps:.3f} FPS", (15, 30), cv2.FONT_HERSHEY_SIMPLEX,
        #             1, (0, 255, 0), 2)
        cv2.imshow('Result', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# release VideoCapture()
cap.release()
# close all frames and video windows
cv2.destroyAllWindows()

# calculate and print the average FPS
avg_fps = total_fps / frame_count
print(f"Average FPS: {avg_fps:.3f}")