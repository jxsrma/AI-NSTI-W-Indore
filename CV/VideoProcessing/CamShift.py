import cv2
# Open video or webcam
cap = cv2.VideoCapture('CV\\vid.mp4')
ret, frame = cap.read()
# Select ROI to track
x, y, w, h = cv2.selectROI("Frame", frame, False)
track_window = (x, y, w, h)
# Setup ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
# Calculate histogram and normalize
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# Setup termination criteria: 10 iterations or move by at least 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    back_proj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    # Apply CamShift to get the new location
    ret, track_window = cv2.CamShift(back_proj, track_window, term_crit)
    # Draw rotated rectangle
    pts = cv2.boxPoints(ret)
    pts = pts.astype(int)
    result = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
    cv2.imshow('CamShift Tracking', result)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
