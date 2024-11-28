# import PIL 
from PIL import Image
import matplotlib.pyplot as plt
# import ultralytics
from ultralytics import YOLO

class Detection:

    def detect(file_path):
        img = Image.open(file_path)
        model = YOLO('model/last.pt')
        results = model(img)

        rgb_image = results[0].plot()[:, :, ::-1]
        Image.fromarray(rgb_image).save('result.png')
        img_result = Image.open('result.png')
        return img_result
