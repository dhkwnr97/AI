	*
train.py와 Fetal_detection.ipynb은 Google_ObjDetectAPI가 설치된
.../TensorFlow\models\research\object_detection
으로 이동시켜야 합니다.
	*
ssd_mobilenet_v1_coco_2018_01_28.tar는 Google_ObjDetectAPI가 설치된
.../TensorFlow\models\research\object_detection\ssd_mobilenet_v1_coco_2018_01_28
의 폴더명을 유지하여 압축을 풀어야 합니다.
	*
inference_graph_person.zip은 모델훈련 후 나온 tensorflow 그래프 이므로 Google_ObjDetectAPI가 설치된
.../TensorFlow\models\research\object_detection\inference_graph_person
의 폴더명을 유지하여 압축을 풀어야 합니다.
	*
Grand Challenges 에서 받고 사진들을 DvidingData_test_train.py로 test_set과 train_set 나눈 후, 사진들을
.../TensorFlow\models\research\object_detection\images
폴더를 새로 만들고 그 폴더 안에
test : .../TensorFlow\models\research\object_detection\images\test
train : .../TensorFlow\models\research\object_detection\images\train
폴더를 새로 만든 후 각 파일명에 맞는 xml_set폴더 내 xml파일과 함께 나누어 담아줍니다.
	*
ssd_mobilenet_v1_pets.config파일은
.../TensorFlow\models\research\object_detection\training
폴더를 새로 만들고 그 폴더 안에 위치시킵니다.
	*
object-detection.pbtxt파일은
.../TensorFlow\models\research\object_detection\data
폴더에 위치시킵니다.
	*
train_Labels.csv와 test_Labels.csv파일은 generate_tfrecord.py를 이용하여 record파일로 변환 후
.../TensorFlow\models\research\object_detection\data
폴더에 csv, record를 모두 위치시킵니다.
