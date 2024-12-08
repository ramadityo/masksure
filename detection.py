
from PIL import Image
from ultralytics import YOLO

class Detection:

    def detect(img):
        # img = Image.open(file_path)
        model = YOLO('model/last.pt')
        results = model(img)

        rgb_image = results[0].plot()[:, :, ::-1]
        Image.fromarray(rgb_image).save('result.png')
        img_result = Image.open('result.png')
        results = results[0].speed
        return img_result, results
