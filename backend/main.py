import json
import os
import re
import sqlite3
import cv2
import sys
import uuid
import numpy as np
from sql import *
from datetime import datetime

import cvzone
from ultralytics.utils import *
from ultralytics import YOLO

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from dashboard.ui_dashboard import Ui_MainWindow
from launcher.ui_launcher import Ui_Launcher

GLOBAL_STATE = 0
counter = 0


class Main(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_main = Ui_MainWindow()
        self.timer = QTimer()
        self.ui_main.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.ui_main.btn_connect.clicked.connect(self.start_webcam)
        self.ui_main.btn_disconnect.clicked.connect(self.stop_webcam)

        self.ui_main.btn_cart.clicked.connect(self.stop_webcam)

        self.ui_main.btn_close.clicked.connect(self.close)
        self.ui_main.btn_minimize.clicked.connect(self.showMinimized)

        self.ui_main.btn_home.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.home))
        self.ui_main.btn_cart.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.cart))
        self.ui_main.btn_update.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.update))
        self.ui_main.btn_receipt.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.receipt))

        self.ui_main.btn_receipt.clicked.connect(self.render_products_to_text_area)
        self.ui_main.btn_receipt.clicked.connect(self.generate_receipt_id_on_receipt_btn_click)

        self.set_mall_details(self.read_mall_details(self.resource_path('mall_details.txt')))

        self.ui_main.btn_add_product.clicked.connect(self.insert_product)
        self.ui_main.btn_update_product.clicked.connect(self.update_product)
        self.ui_main.btn_reload_ui.clicked.connect(self.product_page_interface_reload)

        self.ui_main.btn_clear_cart.clicked.connect(self.clear_cart_items)

        self.product_table(
            self.query_products_list("SELECT product_name,product_price FROM tb_products ORDER BY product_name ASC"))
        self.ui_main.tableWidget.itemSelectionChanged.connect(self.handle_table_selection_change)

        self.model = YOLO(self.resource_path('best.pt'))

        self.product_categories = self.read_product_classes(self.resource_path('labels.txt'))

        self.images_directory = self.change_current_dir_to_new_dir('images')

        self.ui_main.quantity.textChanged.connect(self.quantity_field_listener)
        self.ui_main.tableWidget_receipt.itemSelectionChanged.connect(self.handle_cart_table_selection_change)

        self.ui_main.btn_remove_item_from_cart.clicked.connect(self.remove_product_from_cart)


        self.items = {}
        self.product_names: list = []
        self.price_quantity_subtotal: list = []
        self.selected_row = None

    def read_json_file(self, path):
        with open(path, 'r') as content:
            json_data = json.load(content)
        return json_data

    def string_formater(self, value):
        return "\'{}\'".format(value)

    def validate_price(self, pattern, value):
        return bool(re.match(pattern, value))

    def product_page_alert(self, message):
        self.ui_main.label_notification_products.setText(message)

    def insert_product(self):
        secret = self.read_json_file(self.resource_path('secret.json'))
        if secret['secret'] == self.ui_main.admin_secret.text():
            db = sqlite3.connect(self.resource_path('shopping.db'))
            cursor = db.cursor()
            name = self.ui_main.productName.text()
            price = self.ui_main.productPrice_.text()
            details = self.query_products_data(
                f"SELECT * FROM tb_products WHERE product_name={self.string_formater(name)}")
            if not details:
                if self.validate_price("^[0-9]+$", price) and name:
                    cursor.execute("INSERT INTO tb_products(product_name,product_price) VALUES(?,?)",
                                   (self.ui_main.productName.text(), price))
                    db.commit()
                    self.product_page_alert("Product inserted successfully")
                    self.product_table(self.query_products_list(
                        "SELECT product_name,product_price FROM tb_products ORDER BY product_name ASC"))
                else:
                    self.product_page_alert("Invalid price or product name")
            else:
                self.product_page_alert("Product already exists")
        else:
            self.product_page_alert("Operation not allowed!")

    def update_product(self):
        secret = self.read_json_file(self.resource_path('secret.json'))
        if secret['secret'] == self.ui_main.admin_secret.text():
            db = sqlite3.connect(self.resource_path('shopping.db'))
            cursor = db.cursor()
            name = self.ui_main.productName.text()
            price = self.ui_main.productPrice_.text()
            if self.validate_price("^[0-9]+$", price) and name:
                cursor.execute("UPDATE  tb_products SET product_price=? WHERE product_name=?",
                               (price, self.ui_main.productName.text()))
                db.commit()
                self.product_page_alert("Product price updated!")
                self.product_table(self.query_products_list(
                    "SELECT product_name,product_price FROM tb_products ORDER BY product_name ASC"))
            else:
                self.product_page_alert("Invalid price or product name")
        else:
            self.product_page_alert("Operation not allowed!")

    def change_current_dir_to_new_dir(self, folder_name):
        current_dir = os.getcwd()
        construct_new_path = os.path.join(current_dir, folder_name)
        os.chdir(construct_new_path)
        images_dir = os.getcwd()
        return images_dir

    def get_image_path(self, product_name: str):
        return os.path.join(self.images_directory, product_name + '.jpg')

    def fetch_product_from_database(self, product_class):
        product_details = self.query_products_data(
            f"SELECT product_name,product_price FROM tb_products WHERE product_name={self.string_formater(product_class)}")
        if len(product_details) > 0:
            self.ui_main.itemName.setText((product_details[0]))
            self.ui_main.itemPrice.setText(str(product_details[1]))
            self.ui_main.image.setPixmap(QPixmap.fromImage(self.get_image_path(product_details[0])))
            self.ui_main.image.setScaledContents(True)
            self.show_info("Product available!")
        else:
            self.show_info("Oops! product not available!")

    def handle_table_selection_change(self):
        selected_items = self.ui_main.tableWidget.selectedItems()
        if len(selected_items) > 0:
            selected_row = selected_items[0].row()
            items_in_row = []
            for col in range(self.ui_main.tableWidget.columnCount()):
                item = self.ui_main.tableWidget.item(selected_row, col)
                items_in_row.append(item.text())
            self.ui_main.productName.setText(items_in_row[0]), self.ui_main.productPrice_.setText(items_in_row[1])

    def handle_cart_table_selection_change(self):
        selected_items = self.ui_main.tableWidget_receipt.selectedItems()
        if len(selected_items) > 0:
            self.selected_row = selected_items[0].row()
            items_in_row = []
            for col in range(self.ui_main.tableWidget_receipt.columnCount()):
                item = self.ui_main.tableWidget_receipt.item(self.selected_row, col)
                items_in_row.append(item.text())
            self.destructure_table_value(items_in_row)

    def product_table(self, records: list):
        self.ui_main.tableWidget.setAutoScroll(True)
        self.ui_main.tableWidget.setAutoScrollMargin(2)
        self.ui_main.tableWidget.setTabKeyNavigation(True)
        self.ui_main.tableWidget.setColumnWidth(0, 280)
        self.ui_main.tableWidget.setColumnWidth(1, 100)
        self.ui_main.tableWidget.setRowCount(len(records))
        self.ui_main.tableWidget.verticalHeader().setVisible(True)
        row_count = 0
        for item in records:
            self.ui_main.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(item[0])))
            self.ui_main.tableWidget.setItem(row_count, 1, QTableWidgetItem(str(item[1])))
            row_count = row_count + 1

    def cart_items_table(self, records: list):
        self.ui_main.tableWidget_receipt.setAutoScroll(True)
        self.ui_main.tableWidget_receipt.setAutoScrollMargin(2)
        self.ui_main.tableWidget_receipt.setTabKeyNavigation(True)
        self.ui_main.tableWidget_receipt.setColumnWidth(0, 230)
        self.ui_main.tableWidget_receipt.setColumnWidth(1, 100)
        self.ui_main.tableWidget_receipt.setColumnWidth(2, 80)
        self.ui_main.tableWidget_receipt.setColumnWidth(3, 80)
        self.ui_main.tableWidget_receipt.setRowCount(len(records))
        self.ui_main.tableWidget_receipt.verticalHeader().setVisible(True)
        row_count = 0
        for item in records:
            self.ui_main.tableWidget_receipt.setItem(row_count, 0, QTableWidgetItem(str(item[0])))
            self.ui_main.tableWidget_receipt.setItem(row_count, 1, QTableWidgetItem(str(item[1])))
            self.ui_main.tableWidget_receipt.setItem(row_count, 2, QTableWidgetItem(str(item[2])))
            self.ui_main.tableWidget_receipt.setItem(row_count, 3, QTableWidgetItem(str(item[3])))
            row_count = row_count + 1

    def query_products_list(self, query: str):
        db = sqlite3.connect(self.resource_path('shopping.db'))
        cursor = db.cursor()
        cursor.execute(query)
        cursor = cursor.fetchall()
        db.commit()
        details = []
        if cursor:
            for item in cursor:
                details.append(item)
        return details

    def query_products_data(self, query):
        db = sqlite3.connect(self.resource_path('shopping.db'))
        cursor = db.cursor()
        cursor.execute(query)
        details = cursor.fetchone()
        db.commit()
        cursor.close()
        db_data = []
        if details:
            for data in details:
                db_data.append(data)
        return db_data

    def generate_receipt_id_on_receipt_btn_click(self):
        self.number = uuid.uuid1()
        self.number = str(self.number).split('-')
        with open(self.resource_path('mall_details.txt'), 'r') as content:
            details = content.read()
        return str(details).replace('dateStamp', datetime.now().date().strftime('%d-%m-%Y')).replace('receiptNumber', f'{self.number[0]}-{self.number[1]}')

    def read_mall_details(self, filepath):
        number = uuid.uuid1()
        number = str(number).split('-')
        with open(filepath, 'r') as content:
            details = content.read()
        return str(details).replace('dateStamp', datetime.now().date().strftime('%d-%m-%Y')).replace('receiptNumber', f'{number[0]}-{number[1]}')

    def read_product_classes(self, filepath):
        with open(filepath, 'r') as content:
            categories = content.read().split(',')
        return categories

    def set_mall_details(self, data):
        self.ui_main.textEdit.append(data)

    def product_page_interface_reload(self):
        self.ui_main.productName.clear()
        self.ui_main.productPrice_.clear()
        self.ui_main.label_notification_products.setText("Notification")

    def set_product_page_combobox_items(self, items: dict):
        self.ui_main.cartProducts.addItems(items)

    def clear_cart_items(self):
        self.items.clear()
        self.ui_main.cartTotalItemsTopBAr.clear()

    def destructure_cart_items(self):
        product_names: list = []
        price_quantity_subtotal: list = []
        for key, value in self.items.items():
            product_names.append(key)
            price_quantity_subtotal.append(value)
        return product_names, price_quantity_subtotal

    def add_item_to_cart(self, product_name: str, product_price: int, quantity: int):
        if self.ui_main.itemName.text() != "Name" and self.ui_main.itemPrice.text() != "Price":
            self.items[product_name] = [product_name, product_price, quantity, product_price*quantity]
            self.ui_main.cartTotalItemsTopBAr.setText(str(len(self.items)))
            return self.items
        else:
            pass

    def destructure_table_value(self, product_details: list):
        self.ui_main.cartProductName.setText(product_details[0])
        self.ui_main.productPrice.setText(product_details[1])
        self.ui_main.quantity.setText(product_details[2])
        self.ui_main.prouctSubAmount.setText(product_details[3])

    def quantity_field_listener(self):
        price = self.ui_main.productPrice.text()
        quantity = self.ui_main.quantity.text()
        if self.validate_price("^[0-9]+$", quantity) and price != 'Price':
            if int(quantity) != 0:
                self.price_quantity_subtotal[self.selected_row][2] = quantity
                self.price_quantity_subtotal[self.selected_row][3] = int(price)*int(quantity)
                self.ui_main.prouctSubAmount.setText(str(int(price)*int(quantity)))
                self.cart_items_table(self.price_quantity_subtotal)
                self.retrieve_current_amount_per_item_and_sum(self.price_quantity_subtotal)
            else:
                self.ui_main.cart_notification.setText("Oops! quantity can't\nbe zero.")
        else:
            pass

    def retrieve_current_amount_per_item_and_sum(self, products: list):
        price_list: list = []
        if len(products) > 0:
            for item in range(len(products)):
                price_list.append(int(products[item][3]))
            self.ui_main.cartTotalAmount.setText(f'Grand Total: ${np.sum(price_list)}.00')
        else:
            pass

    def render_products_to_text_area(self):
        self.ui_main.textEdit.clear()
        self.set_mall_details(self.read_mall_details(self.resource_path('mall_details.txt')))
        if len(self.price_quantity_subtotal) > 0:
            for item in self.price_quantity_subtotal:
                if len(item[0]) > 21:
                    self.set_mall_details(f"     "
                                          f"{item[0]}                               "
                                          f"{item[2]}                         "
                                          f"{item[1]}                            "
                                          f"{item[3]}"
                                          )
                    self.set_mall_details("============================================================")
                else:
                    spaces = 40-len(item[0])
                    self.set_mall_details(f"     "
                                          f"{str(item[0]).ljust(spaces)}                               "
                                          f"{item[2]}                         "
                                          f"{item[1]}                            "
                                          f"{item[3]}"
                                          )
                    self.set_mall_details("============================================================")

            self.set_mall_details(f"                                                                                             Total: ${self.ui_main.cartTotalAmount.text()}")
            self.set_mall_details("                                                                                      ========================")
        else:
            pass

    def remove_product_from_cart(self):
        price = self.ui_main.productPrice.text()
        if price != "Price":
            self.price_quantity_subtotal.pop(self.selected_row)
            self.cart_items_table(self.price_quantity_subtotal)
            self.retrieve_current_amount_per_item_and_sum(self.price_quantity_subtotal)
            self.ui_main.cartProductName.setText("Product name")
            self.ui_main.productPrice.setText("Price")
            self.ui_main.quantity.setText('')
            self.ui_main.prouctSubAmount.setText("Amount")
            self.ui_main.cartTotalItemsTopBAr.setText(str(len(self.price_quantity_subtotal)))
            self.ui_main.cart_notification.setText("Item removed from\ncart.")
        else:
            pass

    def start_webcam(self):
        self.show_info("Starting webcam in\nprogress.")
        self.system_capture = cv2.VideoCapture(0)
        self.show_info("Starting webcam in\nprogress.")
        self.system_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 280)
        self.system_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 450)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)
        self.show_info("Starting webcam in\nprogress.")

    def update_frame(self):
        ret, self.frame = self.system_capture.read()
        self.frame = cv2.flip(self.frame, 1)
        results = self.model(self.frame, stream=True)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cvzone.cornerRect(self.frame, (x1, y1, x2 - x1, y2 - y1))
                products_trained_categories_index = int(box.cls[0])
                product_name = self.product_categories[products_trained_categories_index]
                self.fetch_product_from_database(product_name)
                self.add_item_to_cart(product_name=self.ui_main.itemName.text(), product_price=self.ui_main.itemPrice.text(), quantity=1)
                self.product_names, self.price_quantity_subtotal = self.destructure_cart_items()
                self.cart_items_table(self.price_quantity_subtotal)
                self.retrieve_current_amount_per_item_and_sum(self.price_quantity_subtotal)
        self.display_feed(self.frame, 1)

    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui_main.cameraFeed.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui_main.cameraFeed.setScaledContents(True)

    def stop_webcam(self):
        if self.timer.isActive():
            self.show_info("Disconnecting from\nwebcam.")
            self.ui_main.cameraFeed.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui_main.cameraFeed.setScaledContents(False)
            self.timer.stop()
        else:
            self.show_info("Oops! no camera\nin use.")

    def show_info(self, content: str):
        self.ui_main.label_notification.setText(content)

    def resource_path(self, relative_path):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))
        return path

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()

class Launcher(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_Launcher()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()
        self.create_database_table()

    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 50:
            self.timer.stop()
            self.close()
            self.main = Main()
            self.main.show()
        counter += 1

    def resource_path(self, relative_path):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path))
        return path

    def create_database_table(self):
        db = sqlite3.connect(self.resource_path('shopping.db'))
        cursor = db.cursor()
        cursor.execute(create_table())
        db.commit()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Launcher()
    sys.exit(application.exec_())
