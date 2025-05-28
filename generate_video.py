import cv2
from datetime import datetime
import os

GENERATED_FOLDER = 'generated_videos'
os.makedirs(GENERATED_FOLDER, exist_ok=True)

def generate_video_with_text(image_path, text):
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    video_path = os.path.join(GENERATED_FOLDER, f"output_{timestamp}.mp4")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, 1.0, (width, height))

    for _ in range(30):
        frame = img.copy()
        cv2.putText(frame, text, (50, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
        out.write(frame)

    out.release()
    return video_path


