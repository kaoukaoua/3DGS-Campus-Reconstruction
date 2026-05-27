import cv2, os
video_dir = '/share/indoor_videos'
output_dir = '/share/indoor_frames'
interval = 15  # extract every 15th frame

for video_file in sorted(os.listdir(video_dir)):
    cap = cv2.VideoCapture(os.path.join(video_dir, video_file))
    frame_id, saved = 0, 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % interval == 0:
            fname = f"{video_file[:-4]}_{saved:04d}.jpg"
            cv2.imwrite(os.path.join(output_dir, fname), frame)
            saved += 1
        frame_id += 1
    cap.release()
