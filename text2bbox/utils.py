import cv2
import matplotlib.pyplot as plt

# draw utils

def draw_bbox(path, bb):
    img_path = path.replace(WEB_DIR, OUR_DIR)
    img = cv2.imread(img_path)
    
    result = img.copy()
    cv2.rectangle(result, (bb['left'], bb['top']), (bb['right'], bb['bottom']), (0, 255, 0), 5)
    plt.figure(figsize=(12, 8))
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.show()