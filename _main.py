import cv2
import pytesseract
import pyperclip
from image_selector import OpenFileDialog


class ImageTextExtractor:
    def __init__(self):
        self.img = None
        self.text = ""

    def open_image(self):
        self.img = cv2.imread(OpenFileDialog().show())
        if self.img is None:
            print("Error: Could not open image file.")
            exit()

    def display_image(self):
        cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Image', self.img)

    def select_roi(self):
        roi = cv2.selectROI('Image', self.img)
        return roi
    
    def crop_image(self, roi):
        cropped_img = self.img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        return cropped_img

    def preprocess_image(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        return thresh

    def extract_text(self, img):
        text = pytesseract.image_to_string(img)
        return text

    def copy_text_to_clipboard(self, text):
        pyperclip.copy(text)
        spam = pyperclip.paste()

    def run(self):
        self.open_image()
        self.display_image()
        roi = self.select_roi()
        cropped_img = self.crop_image(roi)
        thresh = self.preprocess_image(cropped_img)
        self.text = self.extract_text(thresh)
        self.copy_text_to_clipboard(self.text)
        cv2.imshow('Cropped Image', cropped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    extractor = ImageTextExtractor()
    extractor.run()