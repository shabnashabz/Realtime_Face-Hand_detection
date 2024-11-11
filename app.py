from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

app = Flask(__name__)

# Initialize MediaPipe models
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_results = face_detection.process(rgb_frame)
            if face_results.detections:
                for detection in face_results.detections:
                    mp_drawing.draw_detection(frame, detection)
            hand_results = hands.process(rgb_frame)
            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
