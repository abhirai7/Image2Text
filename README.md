# Image2Text

This is a Python script that extracts text from an image using OpenCV and Pytesseract.

## Requirements

* Python 3.x
* install dependencies with 
    ```bash
    pip install -r requirements.txt
    ```
* Tesseract-OCR engine 
  - For Ubuntu/Debian-based systems:
    1. Install Tesseract-OCR using the following command:
        ```bash
        sudo apt-get install tesseract-ocr
        ```
    2. Install the language data for the languages you want to recognize (e.g., English):
        ```bash
        sudo apt-get install tesseract-ocr-eng
        ```
  - For macOS (using Homebrew):
    1. Install Tesseract-OCR using the following command:
        ```bash
        brew install tesseract
        ```
  - For Windows:
    1. Download the Tesseract-OCR installer from the official GitHub repository: https://github.com/tesseract-ocr/tesseract
    2. Follow the installation instructions to install Tesseract-OCR on your system.
* Enable Pyperclip
  - For Linux systems:
    1. Install the xclip or xsel package, which provides a command-line interface to the X11 clipboard. You can install it using the following command:
        ```
        sudo apt-get install xclip
        ```
    2. If you're using a Wayland-based system, you may need to install the wl-clipboard package instead:
        ```
        sudo apt-get install wl-clipboard
        ```
  - For macOS (using Homebrew):
    1. Install the pbcopy and pbpaste commands using the following command:
        ```
        brew install pbcopy
        ```
  - For Windows:
    1. Pyperclip should work out of the box on Windows, but if you're still encountering issues, you can try installing the pywin32 library:
        ```
        pip install pywin32
        ```

## Usage

1. Run the script using `python image_text_extractor.py`
2. Select an image file using the file dialog
3. The script will display the image and allow you to select a region of interest (ROI)
4. The script will extract text from the ROI and copy it to the clipboard
5. Press `SPACE` or `ENTER` button to copy the selected text and Press `c` or `esc` button to exit anytime.

## Class Structure

The script is organized into a single class `ImageTextExtractor` that encapsulates the entire process of extracting text from an image. The class has the following methods:

* `open_image`: Opens an image file using OpenCV
* `display_image`: Displays the image using OpenCV
* `select_roi`: Allows the user to select a region of interest (ROI) from the image
* `crop_image`: Crops the image to the selected ROI
* `preprocess_image`: Applies thresholding to the cropped image
* `extract_text`: Extracts text from the preprocessed image using Pytesseract
* `copy_text_to_clipboard`: Copies the extracted text to the clipboard
* `run`: Orchestrates the entire process of extracting text from an image

## License

This script is licensed under the MIT License.
