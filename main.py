import re

from backend.email_phishing.email_phishing_service import send_emails
from backend.email_scrapper.email_scrapper_service import execute_email_scrapper
from backend.payload.payload_service import open_terminal
from backend.port_scanner.port_scanner import port_scanner_service
from backend.utils.file_helper import get_os_homepath
from backend.wifi_cracking.wifi_cracking_service import get_all_discovered_networks, try_and_break
import validators
from ui_interface import *
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import *
import traceback, sys


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):

        try:
            result = self.fn(*self.args)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


WIFIpressedButtonOption = ''
network_list = []
current_file_path = ''
payload_option = ''





class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.mainPages.setCurrentIndex(9)
        self.ui.addFileBtn.hide()
        self.ui.exitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()

        self.threadpool = QThreadPool()

        self.ui.browse_file_1.clicked.connect(self.browse_files)
        self.ui.browse_file_2.clicked.connect(self.browse_files)

        self.ui.infoGatheringBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.attacksMenu.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.wifiCrackingBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        self.ui.addFileBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())


        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        self.ui.closePopupBtn.clicked.connect(lambda: self.ui.popupContainer.collapseMenu())


        self.ui.port_scanner_goto.clicked.connect(lambda: [self.ui.mainPages.setCurrentIndex(2)] )
        self.ui.email_scraper_goto.clicked.connect(lambda: [self.ui.mainPages.setCurrentIndex(0)])
        self.ui.fhishing_goto.clicked.connect(lambda: [self.ui.mainPages.setCurrentIndex(7)])

        self.ui.openTerminalButton.clicked.connect(lambda: open_terminal())
        self.ui.openAddFileEmailMenuBtn.clicked.connect(lambda: [ self.ui.addAFilePages.setCurrentIndex(1), self.ui.rightMenuContainer.expandMenu()])

        self.ui.dictionary_wifi_goto.clicked.connect(lambda: [self.make_action('load_wifi_content')])
        self.ui.start_port_scan_btn.clicked.connect(lambda: self.make_action('port_scan'))
        self.ui.email_scrapper_button.clicked.connect(lambda: self.make_action('email_scrapper'))
        self.ui.fast_wifi_button.clicked.connect(lambda:[self.change_wifi_option('fast'), self.make_action('wifi_crack')])
        self.ui.intensive_wifi_button.clicked.connect(lambda: [self.change_wifi_option('intensive'), self.make_action('wifi_crack')])
        self.ui.custom_wifi_button.clicked.connect(lambda: [self.change_wifi_option('custom'),self.make_action('wifi_crack')])
        self.ui.option32BitBtn.clicked.connect(
            lambda: [self.change_payload_option('32'), self.make_action('send_emails')])
        self.ui.option64BitBtn.clicked.connect(
            lambda: [self.change_payload_option('64'), self.make_action('send_emails')])
    def change_wifi_option(self, option):
        global WIFIpressedButtonOption
        WIFIpressedButtonOption = option

    def change_payload_option(self, option):
        global payload_option
        payload_option = option
    def browse_files(self):
        global current_file_path
        home_path = get_os_homepath()
        current_file_path = QFileDialog.getOpenFileName(self,'Choose a file', home_path)[0]

    def check_current_file_path_for_emails(self):
        global current_file_path
        if current_file_path != "":
            if 'Dream_Catcher_Outputs' in current_file_path:
                if 'email_scrapper' in current_file_path:
                    return True
        else:
            return False

    def thread_get_wifi_networks_complete(self, s):
        text_template = """ <html><head/><body><p><img src=":/Icons/Icons/chevron-left.svg"/><img src=":/Icons/Icons/rss.svg"/><img src=":/Icons/Icons/chevron-right.svg"/><span style=" font-size:14pt; color:#d2602a;">Name: </span><span style=" font-weight:600; color:#ffffff;">placeholder_wifi_name</span></p><p><br/></p><p><br/></p></body></html>"""
        text = ""
        for network in s:
            text += text_template.replace("placeholder_wifi_name", network)
        self.ui.discovered_wifi_text.setText(text)

    def thread_port_scan_complete(self, s):
        text_template = """<html><head/><body><p><span style=" color:#d2602a;">Port: </span><span style=" color:#ffffff;">placeholder_port</span></p><p><span style=" color:#d2602a;">Port Type: </span><span style=" color:#ffffff;">placeholder_port_type</span></p><p><span style=" color:#d2602a;">Status: </span><span style=" color:#ffffff;">placeholder_port_status</span></p><p><span style=" color:#d2602a;">Protocol: </span><span style=" color:#ffffff;">placeholder_port_protocol</span></p><p><span style=" color:#d2602a;">Product: </span><span style=" color:#ffffff;">placeholder_port_product</span><br/></p><p><br/></p></body></html> """
        text = ""
        for index in range(len(s["port"])):
            text += text_template.replace("placeholder_port_type", s["port_type"][index]).replace("placeholder_port_status", s["status"][index]).replace("placeholder_port_protocol", s["protocol"][index]).replace("placeholder_port_product", s["product"][index]).replace("placeholder_port", s["port"][index])
        self.ui.port_scanner_result_txt.setText(text)

    def thread_emai_scrapper_complete(self, s):
        emailText = ''
        phoneText = ''
        for email in s['emails']:
            emailText += email + '\n'
        for phone in s['phone_numbers']:
            phoneText += phone + '\n'
        self.ui.emails.setText(emailText)
        self.ui.phones.setText(phoneText)

    def thread_wifi_cracker_complete(self, s):
        section_one_text = """<html><head/><body><p><span style=" color:#d2602a;">Result: </span><span style=" color:#ffffff;">placeholder_result</span></p><p><span style=" color:#d2602a;">Number of tries: </span><span style=" color:#ffffff;">placeholder_no_tries</span></p><p><span style=" color:#d2602a;">Time elapsed: </span><span style=" color:#ffffff;">placeholder_time_elapsed</span></p><p><br/></p></body></html>"""
        section_two_text = """<html><head/><body><p><img src=":/Icons/Icons/wifi.svg"/><span style=" color:#d2602a;">WIFI Name: </span><span style=" color:#ffffff;">placeholder_wifi_name</span></p></body></html>"""
        section_three_text = """<html><head/><body><p><img src=":/Icons/Icons/key.svg"/><span style=" color:#d2602a;">Password: </span><span style=" color:#ffffff;">placeholder_password</span></p></body></html>"""
        text_1 = ''
        text_2 = ''
        text_3 = ''
        text_1 += section_one_text.replace("placeholder_result", s["output"]).replace("placeholder_no_tries", s["number_of_tries"]).replace("placeholder_time_elapsed", str(s["time_elapsed"]))
        text_2 += section_two_text.replace("placeholder_wifi_name", s["wifi_name"])
        text_3 += section_three_text.replace("placeholder_password", s["password"])
        self.ui.section_1.setText(text_1)
        self.ui.section_2.setText(text_2)
        self.ui.section_3.setText(text_3)

    def thread_send_emails_complete(self, s):
        text_template = """<html><head/><body><p align="center">Output: <span style=" color:#d2602a;">output_placeholder</span></p></body></html>"""
        text = text_template.replace('output_placeholder', s)

        self.ui.output_email_send.setText(text)

    def check_email_regex(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email)):
            return True
        else:
            return False
    def make_action(self,action):
        valid = False
        error_reson = ''
        parsedDomain = ''
        txt = ''
        if action == "send_emails":
            at_least_one_error = False
            email_field = str(self.ui.email_field.text())
            email_field = email_field.strip()

            password_field = str(self.ui.password_field.text())
            password_field = password_field.strip()

            body_text_edit = str(self.ui.body_text_edit.toPlainText())
            body_text_edit = body_text_edit.strip()

            subject_line_edit = str(self.ui.subject_line_edit.text())
            subject_line_edit = subject_line_edit.strip()

            to_line_edit = str(self.ui.to_line_edit.text())
            to_line_edit = to_line_edit.strip()
            valid = True
            if not email_field or not password_field:
                error_reson = 'credentials_not_provided'
                valid = False
                at_least_one_error = True
            if not body_text_edit:
                error_reson = 'body_empty'
                valid = False
                at_least_one_error = True
            if not subject_line_edit:
                error_reson = 'subject_empty'
                valid = False
                at_least_one_error = True
            if not to_line_edit and current_file_path == '':
                error_reson = 'to_empty'
                valid = False
                at_least_one_error = True
            if not self.check_current_file_path_for_emails():
                error_reson = 'invalid_emails_file'
                valid = False
                at_least_one_error = True
            if not self.check_email_regex(email_field):
                error_reson = 'invalid_email'
                valid = False
                at_least_one_error = True
            if self.check_current_file_path_for_emails() and not at_least_one_error:
                valid = True
            global payload_option
            txt = email_field+"~"+action+"~"+password_field+"~"+current_file_path+"~"+subject_line_edit+"~"+body_text_edit+"~"+payload_option+'~'+to_line_edit
        if action == "load_wifi_content":
            valid = True
        if action == "port_scan":
            txt = str(self.ui.port_scan_domain.text())
            parsedDomain = txt.replace(" ", "")
            parsedDomain = 'https://' + parsedDomain
            valid = validators.url(parsedDomain)
        if action == "wifi_crack":
            txt = str(self.ui.wifi_address_name_text_edit.text())
            txt = txt.strip()
            global network_list
            if txt in network_list:
                valid = True
            else:
                valid = False
        if action == "email_scrapper":
            txt = str(self.ui.address_edit_email_scrapper.text())
            parsedDomain = txt.replace(" ", "")
            parsedDomain = 'https://'+ parsedDomain
            valid = validators.url(parsedDomain)
        if valid:
            movie = QMovie('Icons/LoaderIcon.gif')
            self.ui.loader_label.setMovie(movie)
            movie.start()
            self.ui.mainPages.setCurrentIndex(4)
            if action == "load_wifi_content":
                self.make_thread_action('begin'+"~"+action)
            if action == "port_scan" or action == "email_scrapper":
                parsedDomain = ''.join(parsedDomain.split("//")[1:])
                self.make_thread_action(parsedDomain+"~"+action)
            if action == "wifi_crack":
                self.make_thread_action(txt+"~"+action+"~"+WIFIpressedButtonOption+"~"+current_file_path)
            if action == "send_emails":
                self.make_thread_action(txt)

        else:
            if action == "port_scan" or action == "email_scrapper":
                self.ui.popup_txt.setText("The domain provided is not a valid URL, please try again")
                self.ui.popupContainer.expandMenu()
                self.ui.port_scan_domain.setText("")
                self.ui.address_edit_email_scrapper.setText("")
            elif action == 'wifi_crack':
                self.ui.popup_txt.setText("The WIFI you are trying to crack is not shown in the scans")
                self.ui.popupContainer.expandMenu()
                self.ui.wifi_address_name_text_edit.setText("")
            elif action == 'send_emails':
                if error_reson == 'credentials_not_provided':
                    self.ui.popup_txt.setText("Email and Password fields can not be blank")
                if error_reson == 'body_empty':
                    self.ui.popup_txt.setText("The body of the email can not be blank")
                if error_reson == 'subject_empty':
                    self.ui.popup_txt.setText("Please provide a subject to the email as it can not be blank")
                if error_reson == 'to_empty':
                    self.ui.popup_txt.setText("To field can not be empty")
                if error_reson == 'invalid_emails_file':
                    self.ui.popup_txt.setText("The file you provided is not one resulting from a Dream Catcher Crawl. Please provide a file that resulted from a scan and is located in the Dream_Catcher_Outputs folder")
                if error_reson == 'invalid_email':
                    self.ui.popup_txt.setText("The email you provided seems to not be valid")
                self.ui.popupContainer.expandMenu()
                self.ui.email_field.setText("")
                self.ui.password_field.setText("")
                self.ui.to_line_edit.setText("")
                self.ui.subject_line_edit.setText("")
                self.ui.body_text_edit.setText("")

    def set_page_output(self, index):
        if index == 5:
            self.ui.addAFilePages.setCurrentIndex(0)
            self.ui.rightMenuContainer.expandMenu()
        self.ui.mainPages.setCurrentIndex(index)

    def make_thread_action(self, arguments):
        # Pass the function to execute
        action = arguments.split("~")[1]
        if action == "send_emails":
            worker = Worker(send_emails, arguments)
            worker.signals.result.connect(self.thread_send_emails_complete)
            worker.signals.finished.connect(lambda: self.set_page_output(8))
            self.threadpool.start(worker)
        if action == "load_wifi_content":
            worker = Worker(get_all_discovered_networks)
            worker.signals.result.connect(self.thread_get_wifi_networks_complete)
            worker.signals.finished.connect(lambda: self.set_page_output(5))
            self.threadpool.start(worker)
        if action == "port_scan":
            domain = arguments.split("~")[0]
            worker = Worker(port_scanner_service, domain)
            worker.signals.result.connect(self.thread_port_scan_complete)
            worker.signals.finished.connect(lambda: self.set_page_output(3))
            # Execute
            self.threadpool.start(worker)
        if action == "email_scrapper":
            domain = arguments.split("~")[0]
            worker = Worker(execute_email_scrapper, domain)
            worker.signals.result.connect(self.thread_emai_scrapper_complete)
            worker.signals.finished.connect(lambda: self.set_page_output(1))
            # Execute
            self.threadpool.start(worker)

        if action == "wifi_crack":
            worker = Worker(try_and_break, arguments)
            worker.signals.result.connect(self.thread_wifi_cracker_complete)
            worker.signals.finished.connect(lambda: self.set_page_output(6))
            # Execute
            self.threadpool.start(worker)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()
