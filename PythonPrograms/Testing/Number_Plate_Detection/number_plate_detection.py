# from ultralytics import YOLO
#
# no_plate_model = YOLO("../number_plate_detection_2nd_dec.pt")
# model = YOLO("../yolo11x.pt")
#
#
# no_plate = no_plate_model.predict("image.jpg")[0]
#
# results = model.track("image.jpg")[0]
# name_dict = results.names
# frame_detections = {}
#
# for box_idx, box in enumerate(results.boxes):
#     track_id = int(box.id.tolist()[0])
#     result = box.xyxy.tolist()[0]
#     object_class_id = box.cls.tolist()[0]
#     object_class_name = name_dict[object_class_id]
#
#     if object_class_name in valid_classes:
#         frame_detections[track_id] = {object_class_name: result}
#
#         object_color = color_dict[object_class_name]
#         x1, y1, x2, y2 = map(int, result)
#         label = f"{object_class_name} {track_id}"
#
#         # Crop the detected object
#         cropped_object = frame[y1:y2, x1:x2]
#
#                     # # number plate
#                     # no_plate = self.no_plate_model.predict(cropped_object)[0]
#                     # # print(no_plate)
#                     # for plate_box_idx, plate_box in enumerate(no_plate.boxes):
#                     #     # plate_track_id = int(plate_box.id.tolist()[0])
#                     #     plate_result = plate_box.xyxy.tolist()[0]
#                     #     plate_x1, plate_y1, plate_x2, plate_y2 = map(int, plate_result)
#                     #     cropped_number_plate = cropped_object[plate_y1:plate_y2, plate_x1:plate_x2]
#                     #     object_filename = f"{output_dir}/{object_class_name}_frame{frame_idx}_id{track_id}_box{plate_box_idx}.jpg"
#                     #     cv2.imwrite(object_filename, cropped_number_plate)
#
#
#
#                     if track_id not in tracked_objects:
#                         tracked_objects.append(track_id)
#
#                         # no plate bounding box
#                         # number plate
#                         no_plate = self.no_plate_model.predict(cropped_object)[0]
#                         # print(no_plate)
#                         for plate_box_idx, plate_box in enumerate(no_plate.boxes):
#                             # plate_track_id = int(plate_box.id.tolist()[0])
#                             plate_result = plate_box.xyxy.tolist()[0]
#                             plate_x1, plate_y1, plate_x2, plate_y2 = map(int, plate_result)
#                             cropped_number_plate = cropped_object[plate_y1:plate_y2, plate_x1:plate_x2]
#                             object_filename = f"{output_dir}/{object_class_name}_frame{frame_idx}_id{track_id}_box{plate_box_idx}.jpg"
#                             cv2.imwrite(object_filename, cropped_number_plate)
#                             cv2.rectangle(frame, (int(x1+plate_x1), int(y1+plate_y1)), (int(x2+plate_x2), int(y2+plate_y2)), (0, 0, 255), 1)
#
#                         #update the counter
#                         counter += 1
#
#                         # # Save the cropped object as an image
#                         # object_filename = f"{output_dir}/{object_class_name}_frame{frame_idx}_id{track_id}_box{box_idx}.jpg"
#                         # cv2.imwrite(object_filename, cropped_object)
#
#                     # vehicle number
#                     total_vehicle = f"Vehicles No.: {counter}"
#                     cv2.putText(frame, total_vehicle, (int(2100), int(30)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
#                                     (0, 255, 255), 2)
#
#                     # Draw label and bounding box on the frame
#                     cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, object_color, 2)
#                     cv2.rectangle(frame, (x1, y1), (x2, y2), object_color, 2)