# Form implementation generated from reading ui file '/Users/christophprenissl/Desktop/Datascience/Assignment/Task3_Project/imdb_software_actors/Layouts/detail.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 770)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1500, 770))
        Form.setMaximumSize(QtCore.QSize(1500, 770))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 0, 1461, 751))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.imageLabel.setMaximumSize(QtCore.QSize(150, 150))
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout.addWidget(self.imageLabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout_2.addWidget(self.nameLabel)
        self.genresLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.genresLabel.setObjectName("genresLabel")
        self.verticalLayout_2.addWidget(self.genresLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.avRatingLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.avRatingLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.avRatingLabel.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.Germany))
        self.avRatingLabel.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.avRatingLabel.setObjectName("avRatingLabel")
        self.verticalLayout_3.addWidget(self.avRatingLabel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.aboutLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.aboutLabel.setObjectName("aboutLabel")
        self.verticalLayout_4.addWidget(self.aboutLabel)
        self.aboutText = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.aboutText.setReadOnly(True)
        self.aboutText.setObjectName("aboutText")
        self.verticalLayout_4.addWidget(self.aboutText)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.awardsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.awardsLabel.setObjectName("awardsLabel")
        self.verticalLayout_5.addWidget(self.awardsLabel)
        self.awardsTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.awardsTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTriggers.NoEditTriggers)
        self.awardsTable.setColumnCount(3)
        self.awardsTable.setObjectName("awardsTable")
        self.awardsTable.setRowCount(0)
        self.verticalLayout_5.addWidget(self.awardsTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.topMoviesLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.topMoviesLabel.setObjectName("topMoviesLabel")
        self.verticalLayout_6.addWidget(self.topMoviesLabel)
        self.topMoviesTable = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.topMoviesTable.setEditTriggers(QtWidgets.QAbstractItemView.EditTriggers.NoEditTriggers)
        self.topMoviesTable.setColumnCount(3)
        self.topMoviesTable.setObjectName("topMoviesTable")
        self.topMoviesTable.setRowCount(0)
        self.verticalLayout_6.addWidget(self.topMoviesTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.moviesLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.moviesLabel.setObjectName("moviesLabel")
        self.verticalLayout_7.addWidget(self.moviesLabel)
        self.moviesTableView = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.moviesTableView.setEditTriggers(QtWidgets.QAbstractItemView.EditTriggers.NoEditTriggers)
        self.moviesTableView.setColumnCount(5)
        self.moviesTableView.setObjectName("moviesTableView")
        self.moviesTableView.setRowCount(0)
        self.verticalLayout_7.addWidget(self.moviesTableView)
        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.imageLabel.setText(_translate("Form", "Image"))
        self.nameLabel.setText(_translate("Form", "Name"))
        self.genresLabel.setText(_translate("Form", "Genres, Genre, Genre, ..."))
        self.avRatingLabel.setText(_translate("Form", "Star 9.99"))
        self.aboutLabel.setText(_translate("Form", "About"))
        self.aboutText.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here should be the about text</p></body></html>"))
        self.awardsLabel.setText(_translate("Form", "Awards"))
        self.topMoviesLabel.setText(_translate("Form", "Top 5 Movies"))
        self.moviesLabel.setText(_translate("Form", "All Movies"))
