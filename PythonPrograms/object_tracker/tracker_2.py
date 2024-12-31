from ultralytics import YOLO
import cv2
import os

class Tracker:

    def __init__(self):
        self.model = YOLO("X:\\Infosys_STMS\\Smart_Traffic_Management_System\\Requirements\\yolov8x.pt")
        self.no_plate_model = YOLO("X:\\Infosys_STMS\\Smart_Traffic_Management_System\\Requirements\\new_best_2nd_dec.pt")

    # def process_video(self, frames):
    #     detections = []
    #     output_video_frames = []
    #
    #     color_dict = {
    #         "car": (0, 255, 0),
    #         "bus": (0, 0, 255),
    #         "truck": (255, 0, 0),
    #         "motorcycle": (255, 255, 0),
    #         "bicycle": (0, 255, 255)
    #     }
    #
    #     valid_classes = ["car", "bus", "truck", "motorcycle", "bicycle"]
    #
    #     for frame in frames:
    #         results = self.model.track(frame, persist=True)[0]
    #         name_dict = results.names
    #
    #         frame_detections = {}
    #
    #         for box in results.boxes:
    #             track_id = int(box.id.tolist()[0])
    #             result = box.xyxy.tolist()[0]
    #             object_class_id = box.cls.tolist()[0]
    #             object_class_name = name_dict[object_class_id]
    #
    #             if object_class_name in valid_classes:
    #                 frame_detections[track_id] = {object_class_name: result}
    #
    #                 object_color = color_dict[object_class_name]
    #                 x1, y1, x2, y2 = result
    #                 label = f"{object_class_name} {track_id}"
    #
    #                 cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, object_color, 2)
    #                 cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), object_color, 2)
    #
    #         detections.append(frame_detections)
    #         output_video_frames.append(frame)
    #
    #     return output_video_frames
    def process_video(self, frames, output_dir="detected_objects"):
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        detections = []
        output_video_frames = []

        color_dict = {
            "car": (0, 255, 0),
            "bus": (0, 0, 255),
            "truck": (255, 0, 0),
            "motorcycle": (255, 255, 0),
            "bicycle": (0, 255, 255)
        }

        valid_classes = ["car", "bus", "truck", "motorcycle", "bicycle"]
        tracked_objects = []
        counter = 0

        licence_plate =""
        licence_plate_score = 0
        for frame_idx, frame in enumerate(frames):
            results = self.model.track(frame, persist=True)[0]
            name_dict = results.names
            frame_detections = {}

            for box_idx, box in enumerate(results.boxes):
                track_id = int(box.id.tolist()[0])
                result = box.xyxy.tolist()[0]
                object_class_id = box.cls.tolist()[0]
                object_class_name = name_dict[object_class_id]

                if object_class_name in valid_classes:
                    frame_detections[track_id] = {object_class_name: result}

                    object_color = color_dict[object_class_name]
                    x1, y1, x2, y2 = map(int, result)
                    label = f"{object_class_name} {track_id}"

                    # Crop the detected object
                    cropped_object = frame[y1:y2, x1:x2]


                    # # number plate
                    # no_plate = self.no_plate_model.predict(cropped_object)[0]
                    #
                    # # print(no_plate)
                    # for plate_box in no_plate.boxes:
                    #     plate_result = plate_box.xyxy.tolist()[0]
                    #     plate_x1, plate_y1, plate_x2, plate_y2 = map(int, plate_result)
                    #
                    #     cropped_number_plate = cropped_object[plate_y1:plate_y2, plate_x1:plate_x2]
                    #
                    #
                    #
                    #     object_filename = f"{output_dir}/{object_class_name}_frame{frame_idx}_id{track_id}_box.jpg"
                    #     cv2.imwrite(object_filename, cropped_number_plate)



                    if track_id not in tracked_objects:
                        tracked_objects.append(track_id)

                        # no plate bounding box
                        cv2.rectangle(frame, (x1, y1), (x2, y2), object_color, 2)

                        #update the counter
                        counter += 1

                        # # Save the cropped object as an image
                        # object_filename = f"{output_dir}/{object_class_name}_frame{frame_idx}_id{track_id}_box{box_idx}.jpg"
                        # cv2.imwrite(object_filename, cropped_object)

                    # vehicle number
                    total_vehicle = f"Vehicles No.: {counter}"
                    cv2.putText(frame, total_vehicle, (int(2100), int(30)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                    (0, 255, 255), 2)

                    # Draw label and bounding box on the frame
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, object_color, 2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), object_color, 2)
                    # frame = cv2.resize(frame, (1280, 720))
                    cv2.imshow("Live Camera", frame)

                    if cv2.waitKey(1) == ord('q'):
                        break



            detections.append(frame_detections)
            output_video_frames.append(frame)
            cv2.destroyAllWindows()

        return output_video_frames

    def show_video(self, frames):

        for frame in frames:
            cv2.imshow("Live Camera", frame)

            if cv2.waitKey(1) == ord('q'):
                break