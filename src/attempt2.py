import glob
import pathlib
import cv2
import mediapipe as mp

def getData():
  data_file = open("attempt2_data.txt")
  data = data_file.read()
  data = data.split("\n")

  for i in range(len(data)):
    data[i] = data[i].split(",")
    data[i].pop()
  data_file.close()
  return data


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

BATCH_SIZE = 4
IMG_WIDTH = 480
IMG_HEIGHT = 640


# For static images:
IMAGE_FILES = getData()
print(IMAGE_FILES[0][0])

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

  for i in range(len(IMAGE_FILES)): 
    for idx, file in enumerate(IMAGE_FILES[i]):
      print(file)
      # Read an image, flip it around y-axis for correct handedness output (see
      # above).
      image = cv2.flip(cv2.imread(file), 1)
      # Convert the BGR image to RGB before processing.
      results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

      # Print handedness and draw hand landmarks on the image.
      print('Handedness:', results.multi_handedness)
      if not results.multi_hand_landmarks:
        continue
      image_height, image_width, _ = image.shape
      annotated_image = image.copy()
      for hand_landmarks in results.multi_hand_landmarks:
        print('hand_landmarks:', hand_landmarks)
        print(
            f'Index finger tip coordinates: (',
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
            f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
        )
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
      cv2.imwrite(
          '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
      # Draw hand world landmarks.
      if not results.multi_hand_world_landmarks:
        continue
      for hand_world_landmarks in results.multi_hand_world_landmarks:
        mp_drawing.plot_landmarks(
          hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

# For webcam input: