import cv2
# Load video
cap = cv2.VideoCapture('CV\\vid.mp4')
# Read the first frame
ret, frame = cap.read()
# Select ROI (x, y, width, height)
x, y, w, h = cv2.selectROI('Select Object', frame, False)
track_window = (x, y, w, h)
# Setup the ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# Create a mask to filter out low light/noise pixels
mask = cv2.inRange(hsv_roi, (0, 60, 32), (180, 255, 255))
# Calculate the HSV histogram of the ROI
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# Set up termination criteria (max 10 iterations or move at least 1 pixel)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Backproject the histogram onto the current frame
    back_proj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    # Apply meanShift to get the new location
    ret, track_window = cv2.meanShift(back_proj, track_window, term_crit)
    # Draw the tracked window
    x, y, w, h = track_window
    tracked_frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Mean Shift Tracking', tracked_frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
