# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import os
script_dir=os.path.dirname(__file__)
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 768)   #1337, 768
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("background-color:lightblue;")
        # MainWindow.setStyleSheet("border: 1px solid black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet("background-color:lightgray;")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 1351, 31))  #0, 0, 1351, 31
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.rs_label = QtWidgets.QLabel(self.centralwidget)
        self.rs_label.setGeometry(QtCore.QRect(1020, 40, 241, 20))
        self.rs_label.setTextFormat(QtCore.Qt.AutoText)
        self.rs_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rs_label.setObjectName("rs_label")

        self.credits_label = QtWidgets.QLabel(self.centralwidget)
        self.credits_label.setGeometry(QtCore.QRect(670, 665, 750, 30))
        self.credits_label.setAlignment(QtCore.Qt.AlignCenter)
        self.credits_label.setObjectName("credits_label")
        self.credits_label.setFont(QtGui.QFont('Arial', 15))
        #################
        self.ins_queue_label = QtWidgets.QLabel(self.centralwidget)
        self.ins_queue_label.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.ins_queue_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ins_queue_label.setObjectName("ins_queue_label")

        self.ins_queue = QtWidgets.QListWidget(self.centralwidget)
        self.ins_queue.setGeometry(QtCore.QRect(10, 70, 191, 191))
        self.ins_queue.setObjectName("ins_queue")
        self.ins_queue.setFont(QtGui.QFont('Arial', 13))
        self.ins_queue.setSpacing(1)
        self.ins_queue.setStyleSheet("background-color: white; border: 1px solid black;")
        ##################

        #########
        self.rs_table = QtWidgets.QTableWidget(self.centralwidget)
        self.rs_table.setGeometry(QtCore.QRect(930, 70, 420, 584))  #930, 70, 421, 601)
        self.rs_table.setRowCount(21)
        self.rs_table.setColumnCount(8)
        self.rs_table.setObjectName("rs_table")
        self.rs_table.horizontalHeader().setVisible(True)
        self.rs_table.horizontalHeader().setDefaultSectionSize(47) #46
        self.rs_table.horizontalHeader().setMinimumSectionSize(46)
        self.rs_table.verticalHeader().setVisible(True)
        self.rs_table.verticalHeader().setDefaultSectionSize(27) #27
        self.rs_table.verticalHeader().setMinimumSectionSize(27)

        self.rs_table.verticalHeader().setFont(QtGui.QFont('Arial', 7))
        self.rs_table.horizontalHeader().setFont(QtGui.QFont('Arial', 7))

        self.rs_table.setHorizontalHeaderLabels(['RS TAG','BUSY', 'OPCODE','TAG1','VALUE1','TAG2','VALUE2','ISSUED'])
        self.rs_table.setVerticalHeaderLabels(['INT ADD','INT ADD', 'INT ADD','INT MUL','INT MUL','INT MUL','FLT ADD','FLT ADD','FLT ADD','FLT MUL','FLT MUL','FLT MUL','SHIFT','SHIFT','SHIFT','COMP','COMP','NAND','NAND','XOR','XOR'])
        self.rs_table.horizontalHeader().setStyleSheet("background-color: darkgreen; color: white");
        self.rs_table.verticalHeader().setStyleSheet("background-color: darkgreen; color: white");
        self.rs_table.setStyleSheet("background-color: white; border: 1px solid black;")
        ##########


        self.int_register = QtWidgets.QTableWidget(self.centralwidget)
        self.int_register.setGeometry(QtCore.QRect(490, 70, 200, 417)) #490, 70, 201, 431
        self.int_register.setRowCount(16)
        self.int_register.setColumnCount(3)
        self.int_register.setObjectName("int_register")
        self.int_register.horizontalHeader().setVisible(True)
        self.int_register.horizontalHeader().setDefaultSectionSize(59) #49
        self.int_register.horizontalHeader().setMinimumSectionSize(59)
        self.int_register.verticalHeader().setVisible(True)
        self.int_register.verticalHeader().setDefaultSectionSize(25) #25
        self.int_register.verticalHeader().setMinimumSectionSize(25)
        self.int_register.setHorizontalHeaderLabels(['BUSY','TAG', 'DATA'])
        self.int_register.setVerticalHeaderLabels(['R0','R1', 'R2','R3','R4','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','R15'])
        self.int_register.verticalHeader().setFont(QtGui.QFont('Arial', 7))
        self.int_register.horizontalHeader().setFont(QtGui.QFont('Arial', 7))
        self.int_register.horizontalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.int_register.verticalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.int_register.setStyleSheet("background-color: white; border: 1px solid black;")



        self.fp_register = QtWidgets.QTableWidget(self.centralwidget)
        self.fp_register.setGeometry(QtCore.QRect(710, 70, 199, 417))  #710, 70, 201, 431)
        self.fp_register.setRowCount(16)
        self.fp_register.setColumnCount(3)
        self.fp_register.setObjectName("fp_register")
        self.fp_register.horizontalHeader().setVisible(True)
        self.fp_register.horizontalHeader().setDefaultSectionSize(59) #49
        self.fp_register.horizontalHeader().setMinimumSectionSize(59)
        self.fp_register.horizontalHeader().setSortIndicatorShown(False)
        self.fp_register.verticalHeader().setVisible(True)
        self.fp_register.verticalHeader().setDefaultSectionSize(25)
        self.fp_register.verticalHeader().setMinimumSectionSize(25)
        self.fp_register_label = QtWidgets.QLabel(self.centralwidget)
        self.fp_register_label.setGeometry(QtCore.QRect(710, 40, 201, 20))
        self.fp_register_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fp_register_label.setObjectName("fp_register_label")
        self.fp_register.horizontalHeader().setFont(QtGui.QFont('Arial', 7))
        self.fp_register.verticalHeader().setFont(QtGui.QFont('Arial', 7))
        self.fp_register.setHorizontalHeaderLabels(['BUSY','TAG', 'DATA'])
        self.fp_register.setVerticalHeaderLabels(['F0','F1', 'F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15'])
        self.fp_register.horizontalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.fp_register.verticalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.fp_register.setStyleSheet("background-color: white;  border: 1px solid black;")

        self.int_register_label = QtWidgets.QLabel(self.centralwidget)
        self.int_register_label.setGeometry(QtCore.QRect(490, 40, 201, 20))
        self.int_register_label.setAlignment(QtCore.Qt.AlignCenter)
        self.int_register_label.setObjectName("int_register_label")

        self.ldst_buffer = QtWidgets.QTableWidget(self.centralwidget)
        self.ldst_buffer.setGeometry(QtCore.QRect(490, 537, 421, 117))#490, 540, 421, 131
        self.ldst_buffer.setRowCount(4)
        self.ldst_buffer.setColumnCount(7)
        self.ldst_buffer.setObjectName("ldst_buffer")
        self.ldst_buffer.horizontalHeader().setVisible(True)
        self.ldst_buffer.horizontalHeader().setDefaultSectionSize(59) #59
        self.ldst_buffer.horizontalHeader().setMinimumSectionSize(59)
        self.ldst_buffer.verticalHeader().setVisible(False)
        self.ldst_buffer.verticalHeader().setDefaultSectionSize(25) #25
        self.ldst_buffer.verticalHeader().setMinimumSectionSize(25)
        self.ldst_buffer_label = QtWidgets.QLabel(self.centralwidget)
        self.ldst_buffer_label.setGeometry(QtCore.QRect(570, 510, 241, 20))
        self.ldst_buffer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ldst_buffer_label.setObjectName("ldst_buffer_label")
        # ldst_entry = namedlist('ldst_entry','ldst_tag busy opcode address tag value issued')
        self.ldst_buffer.horizontalHeader().setFont(QtGui.QFont('Arial', 7))
        self.ldst_buffer.verticalHeader().setFont(QtGui.QFont('Arial', 7))
        self.ldst_buffer.setHorizontalHeaderLabels(['LDST TAG', 'BUSY' ,'OPCODE' ,'ADDRESS' ,'TAG' ,'VALUE' ,'ISSUED'])
        self.ldst_buffer.horizontalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.ldst_buffer.verticalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.ldst_buffer.horizontalHeader().setStretchLastSection(True)
        self.ldst_buffer.setStyleSheet("background-color: white; border: 1px solid black;")

        self.result_buffer = QtWidgets.QTableWidget(self.centralwidget)
        self.result_buffer.setGeometry(QtCore.QRect(220, 70, 248, 278))
        self.result_buffer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_buffer.setAutoFillBackground(True)
        self.result_buffer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_buffer.setRowCount(9)
        self.result_buffer.setColumnCount(4)
        self.result_buffer.setObjectName("result_buffer")
        self.result_buffer.horizontalHeader().setVisible(True)
        self.result_buffer.horizontalHeader().setDefaultSectionSize(51) #49
        self.result_buffer.horizontalHeader().setMinimumSectionSize(51) #49
        self.result_buffer.verticalHeader().setVisible(True)
        self.result_buffer.verticalHeader().setDefaultSectionSize(29)  #27
        self.result_buffer.verticalHeader().setMinimumSectionSize(29)  #27
        self.result_buffer_label = QtWidgets.QLabel(self.centralwidget)
        self.result_buffer_label.setGeometry(QtCore.QRect(240, 40, 201, 20))
        self.result_buffer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_buffer_label.setObjectName("result_buffer_label")
        # result_entry=namedlist('result_entry','busy tag result address')
        # self.result_buffer.setFont(QtGui.QFont('Arial', 7))
        self.result_buffer.horizontalHeader().setFont(QtGui.QFont('Arial', 7))
        self.result_buffer.verticalHeader().setFont(QtGui.QFont('Arial', 7))
        self.result_buffer.setHorizontalHeaderLabels(['BUSY' ,'TAG' ,'RESULT' ,'ADDRESS'])
        self.result_buffer.setVerticalHeaderLabels(['LD ST','FLT MUL','FLT ADD','INT MUL','INT ADD','SHIFT','COMP','XOR','NAND'])
        self.result_buffer.horizontalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.result_buffer.verticalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.result_buffer.setStyleSheet("background-color: white; border: 1px solid black;")

        # self.result_buffer.disconnect(self.result_buffer.horizontalHeader(), SIGNAL(sectionPressed(int)),this, SLOT(selectColumn(int)))
        # self.result_buffer.horizontalHeader().setStretchLastSection(True)
        # self.result_buffer.verticalHeader().setStretchLastSection(True)


        ##################
        self.fu_pipeline = QtWidgets.QTableWidget(self.centralwidget)
        self.fu_pipeline.setGeometry(QtCore.QRect(220, 386, 251, 269))
        self.fu_pipeline.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fu_pipeline.setAutoFillBackground(True)
        self.fu_pipeline.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fu_pipeline.setRowCount(9)
        self.fu_pipeline.setColumnCount(3)
        self.fu_pipeline.setObjectName("fu_pipeline")
        self.fu_pipeline.horizontalHeader().setVisible(True)
        self.fu_pipeline.horizontalHeader().setDefaultSectionSize(69) #62
        self.fu_pipeline.horizontalHeader().setMinimumSectionSize(69)
        self.fu_pipeline.verticalHeader().setVisible(True)
        self.fu_pipeline.verticalHeader().setDefaultSectionSize(28) #27
        self.fu_pipeline.verticalHeader().setMinimumSectionSize(28)
        self.fu_pipeline.setHorizontalHeaderLabels(['FETCH','DECODE','EXECUTE'])
        self.fu_pipeline.setVerticalHeaderLabels(['LD ST','FLT MUL','FLT ADD','INT MUL','INT ADD','SHIFT','COMP','XOR','NAND'])
        self.fu_pipeline.horizontalHeader().setFont(QtGui.QFont('Arial', 7))
        self.fu_pipeline.verticalHeader().setFont(QtGui.QFont('Arial', 7))
        self.fu_pipeline.horizontalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.fu_pipeline.verticalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.fu_pipeline.setStyleSheet("background-color: white; border: 1px solid black;")
        # self.fu_pipeline.setSelectionMode(QtGui.Qt.NoSelection)
        # self.fu_pipeline.setFocusPolicy(QtGui.Qt.NoFocus)
        # self.fu_pipeline.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)


        self.fu_pipeline_label = QtWidgets.QLabel(self.centralwidget)
        self.fu_pipeline_label.setGeometry(QtCore.QRect(240, 360, 201, 20))
        self.fu_pipeline_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.fu_pipeline_label.setObjectName("fu_pipeline_label")
        ############


        ############
        self.cycle_box = QtWidgets.QSpinBox(self.centralwidget)
        self.cycle_box.setGeometry(QtCore.QRect(90, 535, 111, 26))
        self.cycle_box.setObjectName("cycle_box")
        self.cycle_box_label = QtWidgets.QLabel(self.centralwidget)
        self.cycle_box_label.setGeometry(QtCore.QRect(10, 535, 71, 20))
        self.cycle_box_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cycle_box_label.setObjectName("cycle_box_label")
        self.cycle_box.valueChanged.connect(self.valuechange)
        self.cycle_box.setStyleSheet("background-color: white; ")
        ###########


        ##########
        self.cdb = QtWidgets.QTableWidget(self.centralwidget)
        self.cdb.setGeometry(QtCore.QRect(10, 603, 191, 51))
        self.cdb.setRowCount(1)
        self.cdb.setColumnCount(3)
        self.cdb.setObjectName("cdb")
        self.cdb.horizontalHeader().setVisible(True)
        self.cdb.horizontalHeader().setDefaultSectionSize(63)
        self.cdb.verticalHeader().setVisible(False)
        self.cdb.verticalHeader().setDefaultSectionSize(33) #24
        self.cdb.verticalHeader().setMinimumSectionSize(33) #24
        self.cdb_label = QtWidgets.QLabel(self.centralwidget)
        self.cdb_label.setGeometry(QtCore.QRect(10, 573, 191, 20))
        self.cdb_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cdb_label.setObjectName("cdb_label")

        self.cdb.setHorizontalHeaderLabels(['BUSY','TAG','RESULT'])
        self.cdb.horizontalHeader().setFont(QtGui.QFont('Arial', 7))
        self.cdb.horizontalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.cdb.verticalHeader().setStretchLastSection(True)
        self.cdb.setStyleSheet("background-color: white; border: 1px solid black;")
        #########


        self.load_button = QtWidgets.QPushButton(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(10, 270, 191, 25))
        self.load_button.setObjectName("load_button")
        self.load_button.clicked.connect(self.click)
        self.load_button.setStyleSheet("background-color:rgb(0,0,128); color:white")
        #self.load_button.setBackground(QtGui.QBrush(QtGui.QColor(36,160,237)))

        self.memory = QtWidgets.QTableWidget(self.centralwidget)
        self.memory.setGeometry(QtCore.QRect(10, 340, 191, 182))
        self.memory.setRowCount(256)
        self.memory.setColumnCount(1)
        self.memory.setObjectName("memory")
        self.memory.horizontalHeader().setVisible(False)
        self.memory.horizontalHeader().setDefaultSectionSize(140)
        self.memory.horizontalHeader().setMinimumSectionSize(140)
        self.memory.horizontalHeader().setStretchLastSection(True)
        self.memory.verticalHeader().setStretchLastSection(True)
        self.memory.setStyleSheet("background-color: white; border: 1px solid black;")
        self.memory.verticalHeader().setStyleSheet("background-color: darkgreen; color:white");
        self.memory.setVerticalHeaderLabels(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '220', '221', '222', '223', '224', '225', '226', '227', '228', '229', '230', '231', '232', '233', '234', '235', '236', '237', '238', '239', '240', '241', '242', '243', '244', '245', '246', '247', '248', '249', '250', '251', '252', '253', '254', '255'])
        self.Memory_label = QtWidgets.QLabel(self.centralwidget)
        self.Memory_label.setGeometry(QtCore.QRect(20, 310, 161, 20))
        self.Memory_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Memory_label.setObjectName("Memory_label")
        for i in range(self.memory.rowCount()):
            for j in range(self.memory.columnCount()):
                self.memory.setItem(i,j,QtWidgets.QTableWidgetItem(str(i+j)))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Computer Architecture Project"))
        self.title.setText(_translate("MainWindow", "Tomasulo Simulation "))
        self.rs_label.setText(_translate("MainWindow", "Reservation Stations"))
        self.ins_queue_label.setText(_translate("MainWindow", "Instruction Queue"))
        self.fp_register_label.setText(_translate("MainWindow", "FP Register"))
        self.int_register_label.setText(_translate("MainWindow", "INT Register"))
        self.ldst_buffer_label.setText(_translate("MainWindow", "Load/Store Buffer"))
        self.result_buffer_label.setText(_translate("MainWindow", "Result Buffer"))
        self.fu_pipeline_label.setText(_translate("MainWindow", "FU Pipeline Stages"))
        self.cycle_box_label.setText(_translate("MainWindow", "Cycle : "))
        self.cdb_label.setText(_translate("MainWindow", "Common Data Bus"))
        self.load_button.setText(_translate("MainWindow", "Load Instructions"))
        self.Memory_label.setText(_translate("MainWindow", "Memory"))
        self.credits_label.setText(_translate("MainWindow", "Done by: Firoz Mohammad CED17I017 | Vaibhav Singhal CED17I040"))

    def click(self):
        self.ins_queue.clear()

        with open("iq.txt") as file:
            self.instructions = file.read().splitlines()
        for i in range(len(self.instructions)):
            self.ins_queue.insertItem(i,self.instructions[i])

        # file=os.path.join(script_dir,"output/memory/memory@0.txt")
        # with open(file) as rs1:
        #     lines = rs1.read().splitlines()
        # for i in range(len(lines)):
        #     t=lines[i].split(' ')
        #     for j in range(len(t)):
        #         self.memory.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))

        filename=os.path.join(script_dir,"output/memory/memory@0.txt")
        f=open(filename,"w")
        for i in range(self.memory.rowCount()):
            for j in range(self.memory.columnCount()):
                f.write(str(self.memory.item(i,j).text())+"\n")
        f.close()

        cmd='python main.py'
        os.system(cmd)

        file=os.path.join(script_dir,"output/cycle.txt")
        with open(file) as rs1:
            lines = rs1.read().splitlines()
        cyc=int(lines[0])
        self.cycle_box.setMaximum(cyc)
        self.cycle_box.setMinimum(1)
        self.cycle_box.setValue(1)

    def valuechange(self):
      #self.cycle_box_label.setText(str(self.cycle_box.value()))
      cycle=self.cycle_box.value()

      ################ pc #######################
      file=os.path.join(script_dir,"output/pc/pc@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      pc=int(lines[0])
      if(pc!=-1):
          self.ins_queue.scrollToItem(self.ins_queue.item(pc))
      for i in range(len(self.instructions)):
          if(i==pc):
              self.ins_queue.item(i).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
          else:
              self.ins_queue.item(i).setBackground(QtGui.QBrush(QtGui.QColor(255,255,255)))


      ###########################################
      # with open("memory.txt") as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.memory.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))

      file=os.path.join(script_dir,"output/memory/memory@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/memory/memory@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
             self.memory.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
             # self.memory.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
             if(flag==1):
                 self.memory.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))


      ####################### rs ##########################

      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/int_add_rs/int_add_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/int_add_rs/int_add_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                  self.rs_table.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))



      file=os.path.join(script_dir,"output/int_mul_rs/int_mul_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/int_mul_rs/int_mul_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+3,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+3,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+3,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+3,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
                 # self.rs_table.item(i+3,j).setTextAlignment(QtGui.AlignHCenter)


      # file=os.path.join(script_dir,"output/float_add_rs/float_add_rs@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i+6,j,QtWidgets.QTableWidgetItem(t[j]))

      file=os.path.join(script_dir,"output/float_add_rs/float_add_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/float_add_rs/float_add_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+6,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+6,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+6,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+6,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
                 # self.rs_table.item(i+6,j).setTextAlignment(QtCore.Qt.AlignCenter)

      # file=os.path.join(script_dir,"output/float_mul_rs/float_mul_rs@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i+9,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/float_mul_rs/float_mul_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/float_mul_rs/float_mul_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+9,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+9,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+9,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+9,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))

      # file=os.path.join(script_dir,"output/shift_rs/shift_rs@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i+12,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/shift_rs/shift_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/shift_rs/shift_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+12,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+12,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+12,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+12,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))

      # file=os.path.join(script_dir,"output/comp_rs/comp_rs@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i+15,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/comp_rs/comp_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/comp_rs/comp_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+15,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+15,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+15,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+15,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))

      # file=os.path.join(script_dir,"output/nand_rs/nand_rs@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i+17,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/nand_rs/nand_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/nand_rs/nand_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+17,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+17,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+17,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+17,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))

      # file=os.path.join(script_dir,"output/xor_rs/xor_rs@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.rs_table.setItem(i+19,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/xor_rs/xor_rs@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/xor_rs/xor_rs@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.rs_table.setItem(i+19,j,QtWidgets.QTableWidgetItem(t[j]))
              self.rs_table.item(i+19,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.rs_table.item(i+19,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.rs_table.item(i+19,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
      ####################### rs end ######################

      ####################### ldst buffer ################
      # file=os.path.join(script_dir,"output/ldst_buffer/ldst_buffer@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.ldst_buffer.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/ldst_buffer/ldst_buffer@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/ldst_buffer/ldst_buffer@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.ldst_buffer.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.ldst_buffer.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.ldst_buffer.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[1])==1):
                 self.ldst_buffer.item(i,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
      ##################### ldst buffer end ##############

      #################### int register #################
      # file=os.path.join(script_dir,"output/int_register/int_register@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.int_register.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/int_register/int_register@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/int_register/int_register@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.int_register.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.int_register.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.int_register.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[0])==1):
                 self.int_register.item(i,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))

      ################### int register end ###############

      #################### fp register #################
      # file=os.path.join(script_dir,"output/fp_register/fp_register@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.fp_register.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/fp_register/fp_register@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/fp_register/fp_register@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fp_register.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fp_register.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.fp_register.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[0])==1):
                 self.fp_register.item(i,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
      ################### fp register end ###############

      ################### result buffer ################
      # file=os.path.join(script_dir,"output/result_buffer/result_buffer@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.result_buffer.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/result_buffer/result_buffer@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/result_buffer/result_buffer@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.result_buffer.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.result_buffer.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.result_buffer.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[0])==1):
                 self.result_buffer.item(i,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
      ################### result_buffer end ##################

      ################## cdb ##########################
      # file=os.path.join(script_dir,"output/cdb/cdb@"+str(cycle)+".txt")
      # with open(file) as rs1:
      #     lines = rs1.read().splitlines()
      # for i in range(len(lines)):
      #     t=lines[i].split(' ')
      #     for j in range(len(t)):
      #         self.cdb.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
      file=os.path.join(script_dir,"output/cdb/cdb@"+str(cycle)+".txt")
      file1=os.path.join(script_dir,"output/cdb/cdb@"+str(cycle-1)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      with open(file1) as rs2:
          lines1 = rs2.read().splitlines()
      flag=0
      for i in range(len(lines)):
          if(lines[i]!=lines1[i]):
             flag=1
          else:
             flag=0
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.cdb.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.cdb.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
              if(flag==1):
                 self.cdb.item(i,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
              if(int(t[0])==1):
                 self.cdb.item(i,j).setBackground(QtGui.QBrush(QtGui.QColor(188,245,188)))
      ################## cdb end #######################


      ##################### fu_pipeline ###############
      file=os.path.join(script_dir,"output/int_add_fu/int_add_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+4,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+4,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/int_mul_fu/int_mul_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+3,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+3,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/float_add_fu/float_add_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+2,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+2,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/float_mul_fu/float_mul_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+1,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+1,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/shift_fu/shift_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+5,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+5,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/comp_fu/comp_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+6,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+6,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/nand_fu/nand_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+8,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+8,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/xor_fu/xor_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i+7,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i+7,j).setTextAlignment(QtCore.Qt.AlignCenter)

      file=os.path.join(script_dir,"output/ldst_fu/ldst_fu@"+str(cycle)+".txt")
      with open(file) as rs1:
          lines = rs1.read().splitlines()
      for i in range(len(lines)):
          t=lines[i].split(' ')
          for j in range(len(t)):
              self.fu_pipeline.setItem(i,j,QtWidgets.QTableWidgetItem(t[j]))
              self.fu_pipeline.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
      ##################### fu_pipeline end ###########

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet("background-color:lightgray;")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    MainWindow.show()
    sys.exit(app.exec_())
