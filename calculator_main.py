#3 새 버튼 추가
import sys
from PyQt5.QtWidgets import *


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_all_buttons = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.es = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(self.es)

        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("×")
        button_division = QPushButton("÷")
        button_modula = QPushButton("%")

        ### 신규 연산기능 버튼 추가
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x²")
        button_root = QPushButton("√x")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation="/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_all_buttons.addWidget(button_plus, 4, 3)
        layout_all_buttons.addWidget(button_minus, 3, 3)
        layout_all_buttons.addWidget(button_product, 2, 3)
        layout_all_buttons.addWidget(button_division, 1, 3)
        layout_all_buttons.addWidget(button_modula, 0, 0)

        ### 신규 연산 버튼 추가
        layout_all_buttons.addWidget(button_inverse, 1, 0)
        layout_all_buttons.addWidget(button_square, 1, 1)
        layout_all_buttons.addWidget(button_root, 1, 2)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_ce = QPushButton("CE")
        button_c = QPushButton("C")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_all_buttons.addWidget(button_ce, 0, 1)
        layout_all_buttons.addWidget(button_c, 0, 2)
        layout_all_buttons.addWidget(button_backspace, 0, 3)
        layout_all_buttons.addWidget(button_equal, 5, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num=number: self.number_button_clicked(num))
            if number > 0:
                x, y = divmod(number - 1, 3)
                if (x == 0):
                    x += 2
                elif (x == 2):
                    x -= 2
                layout_all_buttons.addWidget(number_button_dict[number], x + 2, y)
            elif number == 0:
                layout_all_buttons.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        layout_all_buttons.addWidget(button_dot, 5, 2)

        button_plus_minus = QPushButton("+/-")
        button_plus_minus.clicked.connect(lambda state, num="+/-": self.toggle_plus_minus(num))
        layout_all_buttons.addWidget(button_plus_minus, 5, 0)

        # ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution, 0, 0)
        main_layout.addLayout(layout_all_buttons, 1, 0)


        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        es = self.es.text()
        es += str(num)
        self.es.setText(es)

    def button_operation_clicked(self, operation):
        es = self.es.text()
        es += operation
        self.es.setText(es)

    def button_equal_clicked(self):
        es_text = self.es.text()
        ans = eval(es_text)
        self.es.setText(str(ans))

    def button_clear_clicked(self):
        self.es.setText("")

    def button_backspace_clicked(self):
        es = self.es.text()
        es = es[:-1]
        self.es.setText(es)

    def toggle_plus_minus(self, num):
        current_text = self.es.text()
        if num == "+/-":
            if current_text.startswith('-'):
                self.es.setText(current_text[1:])  # 음수인 경우 - 제거
            else:
                self.es.setText('-' + current_text)  # 양수인 경우 맨 앞에 - 추가


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())