from mycroft import MycroftSkill, intent_file_handler


class BadCalculator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('calculator.bad.intent')
    def handle_calculator_bad(self, message):
        self.speak_dialog('calculator.bad')

    def stop(self):
        self.speak_dialog("You can't stop me")

def create_skill():
    return BadCalculator()

