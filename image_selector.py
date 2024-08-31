import sys
from PyQt5.QtWidgets import QApplication, QFileDialog

class OpenFileDialog:

    def show(self):
        app = QApplication(sys.argv)
        file_path, _ = QFileDialog.getOpenFileName(None, "Select an image file", "", "Image files (*.jpg *.png)")
        app.exit()
        return(file_path)

# Example usage:
# dialog = OpenFileDialog()
# print(dialog.show())