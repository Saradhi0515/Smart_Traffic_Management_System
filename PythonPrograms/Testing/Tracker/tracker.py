import cv2
from ultralytics import YOLO
import os
import random

# Load the model and class list
model = YOLO("X:\\Infosys_STMS\\Smart_Traffic_Management_System\\Requirements\\yolo11x.pt")

cap = cv2.VideoCapture('X:\\Infosys_STMS\\Smart_Traffic_Management_System\\Data\\Video\\Traffic_05.mp4')
valid_objects = ['bicycle','car','motorcycle','bus','truck']
color_dict = {
            'bicycle': (0, 255, 0),  # Green
            'car': (255, 0, 0),  # Blue
            'motorcycle': (0, 0, 255),  # Red
            'bus': (255, 255, 0),  # Cyan
            'truck': (0, 255, 255),  # Yellow
        }

cy1 = 1100
offset = 6

counter = 0
track_ids = []


def detect_objects(self, frames):
    detections = []

    for frame in frames:
        deteced_objs = self.detect_frame(frame)
        detections.append(deteced_objs)
    # for i in range(0, len(frames),5):
    #     frame = frames[i]
    #     detected_objs = self.detect_frame(frame)
    #     detections.append(detected_objs)

    return detections


def detect_frame(self, frame):
    results = self.model.track(frame, persist=True)[0]

    # print(results)
    name_dict = results.names

    valid_objects = ['bicycle', 'car', 'motorcycle', 'bus', 'truck']

    dict = {}

    for box in results.boxes:
        track_id = int(box.id.tolist()[0])
        result = box.xyxy.tolist()[0]
        object_class_id = box.cls.tolist()[0]
        object_class_name = name_dict[object_class_id]
        # if object_class_name == "car":
        #     dict[track_id] = result

        if object_class_name in valid_objects:
            dict[track_id] = {object_class_name: result}

    return dict


def read_video(video_path):

    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.track(frame, persist=True)[0]

        # print(results)
        name_dict = results.names

        valid_objects = ['bicycle', 'car', 'motorcycle', 'bus', 'truck']

        dict = {}

        for box in results.boxes:
            track_id = int(box.id.tolist()[0])
            result = box.xyxy.tolist()[0]
            object_class_id = box.cls.tolist()[0]
            object_class_name = name_dict[object_class_id]
            # if object_class_name == "car":
            #     dict[track_id] = result

            if object_class_name in valid_objects:
                dict[track_id] = {object_class_name: result}

        return dict


# while True:
#     print("hello")
#     ret, frame = cap.read()
#     if not ret:
#         print("hello")
#         break
#
#     results = model.track(frame, persist=True)[0]
#
#     name_dict = results.names
#
#     for box in results.boxes:
#         track_id = int(box.id.tolist()[0])
#         print(track_id)
#         result = box.xyxy.tolist()[0]
#         object_class_id = box.cls.tolist()[0]
#         object_class_name = name_dict[object_class_id]
#
#         if object_class_name in valid_objects:
#             x1, y1, x2, y2 = result
#
#             object_color = color_dict.get(object_class_name,
#                                           (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#
#             # center point
#             cx = int(x1 + x2) // 2
#             cy = int(y1 + y2) // 2  # 1105
#             cv2.circle(frame, (cx, cy), 4, (255, 0, 0), -1)
#
#             cv2.line(frame, (450, 1100), (2100, 1100), (255, 255, 255), 1)
#             # Put text on the bbox
#             label = f"{object_class_name} {track_id}"
#
#             cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, object_color, 2)
#
#             # vehicle number
#             total_vehicle = f"Vehicles No.: {counter}"
#             cv2.putText(frame, total_vehicle, (int(2100), int(30)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
#
#             # Drawing the bbox
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), object_color, 2)
#
#             if cy1 < cy:
#
#                 cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)
#
#                 if track_id not in track_ids:
#                     track_ids.append(track_id)
#                     counter += 1
#
#
#     cv2.imshow("RGB", frame)
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()