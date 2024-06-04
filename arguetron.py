import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Arguetron")
        self.setGeometry(100, 100, 800, 600)

        # Create a label to display the GIF
        self.background_label = QtWidgets.QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)

        # Set the background GIF
        self.background_movie = QtGui.QMovie(r"C:\Users\colem\Downloads\angry_robot.gif")
        self.background_label.setMovie(self.background_movie)
        self.background_movie.start()
        self.background_label.setScaledContents(True)

        # Add interactive elements
        self.initUI()

    def resizeEvent(self, event):
        # Ensure the background label and GIF resize with the window
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_movie.setScaledSize(QtCore.QSize(self.width(), self.height()))
        super().resizeEvent(event)

    def initUI(self):
        # Response label
        self.response_label = QtWidgets.QLabel(self)
        self.response_label.setAlignment(QtCore.Qt.AlignCenter)
        self.response_label.setWordWrap(True)
        self.response_label.setGeometry(250, 400, 300, 80)  # Set the position and size

        font = self.response_label.font()
        font.setPointSize(16)
        font.setBold(True)
        self.response_label.setFont(font)
        self.response_label.setStyleSheet("color: red; background-color: white;")

        # Input line edit
        self.line_edit = QtWidgets.QLineEdit(self)
        self.line_edit.setPlaceholderText("Type anything...")
        self.line_edit.setGeometry(250, 500, 300, 40)

        # Reply button
        self.reply_button = QtWidgets.QPushButton("Get Reply", self)
        self.reply_button.setGeometry(250, 550, 300, 40)
        self.reply_button.clicked.connect(self.reply)

        self.line_edit.returnPressed.connect(self.reply)

    def reply(self):
        responses = [
            "Hell no",
            "That's the dumbest shit I've ever heard.",
            "Are you retarded?",
            "Fuck off.",
            "Not right now. I'm meeting your mom at the no tell motel.",
            "Why do you care?",
            "Is that really any of your business?",
            "Figure it out yourself.",
            "Do I look like I care?",
            "Not my problem.",
            "Ask someone who cares.",
            "Why don't you use your brain for once?",
            "Google it, genius.",
            "What a dumb question.",
            "Seriously? You don't know that?",
            "Seriously, you're asking that?",
            "Do you ever think before you speak?",
            "That's the dumbest thing I've heard all day.",
            "Not this again...",
            "Why don't you just go away?",
            "I can't believe you even thought that was a good question.",
            "You're wasting my time.",
            "Are you always this clueless?",
            "That's none of your business.",
            "Why do you care?",
        ]

        user_input = self.line_edit.text()
        if user_input:
            response = random.choice(responses)
            self.response_label.setText(response)
            self.line_edit.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

