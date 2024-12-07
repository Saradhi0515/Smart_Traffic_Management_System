from utils.video_utils import read_video, save_video, detect_vehicles
from object_tracker.tracker_2 import Tracker

def main():

    frames = read_video("C:\\Users\\pardh\\Infosys_STMS\\Smart_Traffic_Management_System\\Data\\Video\\Traffic_01.mp4")

    #object tracking
    obj_tracker = Tracker()
    result = obj_tracker.process_video
    
    (frames)
    output_frames = obj_tracker.draw_annotations(frames, result)


#     save_video(output_frames, "output/123.avi")

###### Main function for 1 image

# def main():

#     frames = read_video("data/image.jpg")

#     #object tracking
#     obj_tracker = Tracker()
#     result = obj_tracker.detect_frame(frames)
#     print(result)

    # output_frames = obj_tracker.draw_annotations(frames, result)
    #
    #
    # save_video(output_frames, "output/output.avi")

if __name__ == '__main__':
    main()

