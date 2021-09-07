from mycroft import MycroftSkill, intent_file_handler
import random

class BadCalculator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    _is_operator = lambda s: s in "+-*/"
    _is_digit = lambda s: s in "0123456789"

    def initialize(self):
        self.log.info("Bad calculator skill loaded!")
        self.register_entity_file('number.entity')
        self.register_entity_file('another_number.entity')
        self.register_entity_file('operator.entity')

    @intent_file_handler('calculator.request.intent')
    def handle_calculation_request(self, message):
        req = self._parse_request(message.data.get('number'), message.data.get('operator'), message.data.get('another_number'))
        
        if req is None:
            self.speak_dialog('calculator.confused')
            return

        a, o, b = req

        if a > 10 and b > 10: 
            self.speak_dialog('calculator.too.hard')
        else:
            ans = 0
            if o == '+':
                ans = a+b
            elif o == '-':
                ans = a-b
            elif o == '*':
                ans = a*b
            elif o == '/':
                ans = int(a/b)
            
            wrong_ans = ans + random.randint(1,10) if random.randint(0,1) else ans - random.randint(1,10)

            self.speak_dialog(
                'calculator.response',
                {'value': wrong_ans} 
            )
            


    def _parse_request(self, num1, op, num2):
        '''
            Takes the extracted entities and returns a tuple of (a,o,b) where the requested is `a o b`, None if fails to parse
            :type a  Int
            :type b  Int
            :type o  String     

            => A better way to do this is to match against a regexp               
        '''
        if num1 is None or num2 is None: return None

        try:
            # Operator is appended to num1, eg. num1 = "123 +"
            if BadCalculator._is_operator(num1[-1]):
                ao = num1.split()
                return (int(ao[0]), ao[1], int(num2))
            # Operator is on its own
            elif op is not None and BadCalculator._is_operator(op):
                return (int(num1), op, int(num2))
            else:
                return None
        except:
            return None
         

    def stop(self):
        # self.speak_dialog("You can't stop me")
        pass

def create_skill():
    return BadCalculator()

