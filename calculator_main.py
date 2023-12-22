import sys
from PyQt5.QtWidgets import *

#2 사칙연산 배치 변경
class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_clear_equal = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.es = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(self.es)

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation="+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation="-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation="*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation="/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_plus,4,3)
        layout_operation.addWidget(button_minus,3,3)
        layout_operation.addWidget(button_product,2,3)
        layout_operation.addWidget(button_division,1,3)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("Clear")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal, 5, 3)

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
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number == 0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num=".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num="00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        # ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution,0,0)
        # main_layout.addLayout(layout_all_buttons,1,0)
        main_layout.addLayout(layout_operation,1,0)
        main_layout.addLayout(layout_clear_equal,2,0)
        main_layout.addLayout(layout_number,3,0)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())