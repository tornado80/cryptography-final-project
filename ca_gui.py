import base64

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from ca_window_ui import Ui_MainWindow
from certificate_authority import CertificateAuthority
from rsa_signature import RSASignature


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sign_push_button.clicked.connect(self.sign_push_button_clicked)
        private_key, public_key = RSASignature.generate_rsa()
        self.ca = CertificateAuthority(private_key, public_key)
        self.ca_public_key_plain_text_edit.setPlainText(
            self.ca.rsa_signature_scheme.convert_public_key_to_pem()
        )

    def sign_push_button_clicked(self):
        if self.user_public_key_plain_text_edit.toPlainText() == '':
            QMessageBox.critical(self, "Error", "You have not entered user's public key!")
        user_public_key = RSASignature.public_key_from_str(
            self.user_public_key_plain_text_edit.toPlainText()
        )
        self.signature_plain_text_edit.setPlainText(
            base64.b64encode(self.ca.issue_certificate(user_public_key)).decode('utf-8')
        )
        

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec_()