import io
import cv2
import requests
import base64

def cin_to_server(index,sensor, bytes_image):

    url = (f'http://180.83.19.43:7579/Mobius/HAETAE/raindrop{index}/{sensor}')
    
    headers =   {'Accept':'application/json',
    'X-M2M-RI':'12345',
    'X-M2M-Origin':'SpUuMHvGqsO', # change to your aei
    'Content-Type':'application/vnd.onem2m-res+json; ty=4'
    }

    data =   {
        "m2m:cin": {
            "con": img_str
            }
            }

    r = requests.post(url, headers=headers, json=data)
    
    try:
        r.raise_for_status()
        print(r)
    except Exception as exc:
        print('There was a problem: %s'%(exc))


canny_output_filename = 'canny_output.mp4'
frame_output_filename = 'frame_output.mp4'

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('cant open')
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'X264')
canny_out = cv2.VideoWriter(canny_output_filename, fourcc, fps, (frame_width, frame_height))
frame_out = cv2.VideoWriter(frame_output_filename, fourcc, fps, (frame_width, frame_height))

def on_trackbar(val):
    pass

cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Min Threshold', 'Canny Edge Detection', 0, 255, on_trackbar)
cv2.createTrackbar('Max Threshold', 'Canny Edge Detection', 0, 255, on_trackbar)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    min_threshold = cv2.getTrackbarPos('Min Threshold', 'Canny Edge Detection')
    max_threshold = cv2.getTrackbarPos('Max Threshold', 'Canny Edge Detection')

    edges = cv2.Canny(frame, min_threshold, max_threshold)
    lines = cv2.HoughLinesP(edges, 1, 3.14/180, threshold=100, minLineLength=100, maxLineGap=10)

    if lines is not None:
        line_count = len(lines)
        if line_count > 500:
            _, img_encoded = cv2.imencode('.jpg', frame)
            image_bytes = img_encoded.tobytes()
            img_str = base64.b64encode(image_bytes).decode('utf-8')
            cin_to_server(1,"camera",img_str)
            
    canny_out.write(edges)
    frame_out.write(frame)

    cv2.imshow('Canny Edge Detection', edges)
    cv2.imshow('show', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
canny_out.release()
frame_out.release()
cv2.destroyAllWindows()
