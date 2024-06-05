class EventHandler:
    '''Connection between gui and logic from Translator'''
    def __init__(self, gui, translator) -> None:
        self.gui = gui
        self.translator = translator
        self.gui.translateButton.clicked.connect(self.do_event)
        
    
    def do_event(self):
        if self.gui.changeLang.currentText() == "Русский - Шотыну":
            user_input = self.gui.originalText.toPlainText()
            answer = self.translator.encrypt(user_input)
            self.gui.translatedText.setText(answer)
            
        if self.gui.changeLang.currentText() == "Шотыну - Русский":
            user_input = self.gui.originalText.toPlainText()
            answer = self.translator.decrypt(user_input)
            self.gui.translatedText.setText(answer) 
            