from ultralytics import YOLO
import supervision as sv

class Tracker:
    
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()


    def detect_frames(self, frames):
        batch_size = 20
        detections = []

        for i in range(0, len(frames), batch_size):
            detection_batch = self.model.predict(frames[i:i+batch_size], conf=0.1)
            detections += detection_batch
            break

        return detections

    def get_object_tracks(self, frames):

        detections = self.detect_frames(frames)

        for frame_num, detection in enumerate(detections):
            cls_name = detection.names
            cls_name_inv = {v:k for k,v in cls_name.items()}

            # convert the detection to supervision detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)

            #Convert goolkeeper to player object
            for object_ind, class_id in enumerate(detection_supervision.class_id):
                if cls_name[class_id] == "goalkeeper":
                    detection_supervision.class_id[object_ind] = cls_name_inv['player']

            print(detection_supervision)

            break