import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from controles.menu import InterfazMenu

app = QApplication(sys.argv)

stack = QStackedWidget()

menu = InterfazMenu()

stack.addWidget(menu)        # index 0

# Mostrar login primero
stack.setCurrentIndex(0)
stack.setFixedSize(400, 373)
stack.show()

# Luego puedes cambiar de vista con:
# stack.setCurrentIndex(1)

sys.exit(app.exec())
