import base64

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ca_window_ui import Ui_MainWindow
from certificate_authority import CertificateAuthority
from rsa_signature import RSASignature
from utils import load_default_private_and_private_key


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, private_key_pem):
        super().__init__()
        self.setupUi(self)
        self.sign_push_button.clicked.connect(self.sign_push_button_clicked)
        self.ca = CertificateAuthority()
        self.ca.set_private_key_and_public_key(
            *load_default_private_and_private_key(private_key_pem)
        )
        self.ca.rsa_signature_scheme.save_public_key("ca_pub.pem")
        self.ca_public_key_plain_text_edit.setPlainText(
            self.ca.rsa_signature_scheme.convert_public_key_to_pem()
        )

    def sign_push_button_clicked(self):
        if self.user_public_key_plain_text_edit.toPlainText() == '':
            QMessageBox.critical(self, "Error", "You have not entered user's public key!")
            return
        user_public_key = RSASignature.public_key_from_str(
            self.user_public_key_plain_text_edit.toPlainText()
        )
        self.signature_plain_text_edit.setPlainText(
            base64.b64encode(self.ca.issue_certificate(user_public_key)).decode('utf-8')
        )


if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow("ca.pem")
    main_window.show()
    app.exec_()