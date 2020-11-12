import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow logging (1)
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"     # disable gpu

import tensorflow as tf
import cv2

import numpy as np
import warnings

warnings.filterwarnings('ignore')  # Suppress Matplotlib warnings

tf.get_logger().setLevel('ERROR')  # Suppress TensorFlow logging (2)

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

import time
from object_detection.utils import label_map_util
from object_detection.utils import config_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

from absl import app

PATH_TO_MODEL_DIR = "./demo/ssd_mobilenet_v2_320x320_coco17_tpu-8"
PATH_TO_CFG = PATH_TO_MODEL_DIR + "/pipeline.config"
PATH_TO_CKPT = PATH_TO_MODEL_DIR + "/checkpoint"
PATH_TO_LABELS = "./demo/mscoco_label_map.pbtxt"

print('Loading model... ', end='')
start_time = time.time()

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file(PATH_TO_CFG)
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# In this session, I want to convert the tf2.0 to h5 model, then convert to savedmodel with freezn variable
print("detection_model loaded")

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join(PATH_TO_CKPT, 'ckpt-0')).expect_partial()


def detect_fn(image):
    """Detect objects in image."""
    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)

    return detections


end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))


def main(_):
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                        use_display_name=True)

    threshold = 0.6
    wait_time = 1

    vc = cv2.VideoCapture(0)
    rval, frame = vc.read()
    
    cv2.namedWindow('camera', 0)
    
    while rval:
        rval, frame = vc.read()

        input_tensor = tf.convert_to_tensor(np.expand_dims(frame, 0), dtype=tf.float32)

        start_time = time.time()
        detections = detect_fn(input_tensor)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Detect done! Took {} seconds'.format(elapsed_time))

        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                      for key, value in detections.items()}
        detections['num_detections'] = num_detections
        # detection_classes should be ints.
        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

        label_id_offset = 1

        viz_utils.visualize_boxes_and_labels_on_image_array(
            frame,
            detections['detection_boxes'],
            detections['detection_classes'] + label_id_offset,
            detections['detection_scores'],
            category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=200,
            min_score_thresh=threshold,
            agnostic_mode=False)

        cv2.imshow('camera', frame)
        key = cv2.waitKey(wait_time)

        if key == ord('q'):
            break
        if key == ord('p'):
            wait_time = (wait_time + 1) % 2


if __name__ == '__main__':
    app.run(main)
