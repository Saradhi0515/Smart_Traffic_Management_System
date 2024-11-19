from utils.video_utils import read_video, save_video, detect_vehicles

def main():

    frames = read_video("data/traffic_video.mp4")

    # Video processing and detection
    detection_of_vehicles = detect_vehicles(frames)




    save_video(frames, "output/output.avi")

if __name__ == '__main__':
    main()