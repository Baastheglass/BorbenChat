import google.generativeai as genai

class GenAIException():
    def __init__(self, exception):
        self.exception = exception

def construct_message(text, role = 'user'):
        return {'role' : role, 'parts' : text}
    
class chatBot:
    CHATBOT_NAME = "Borben"
    def __init__(self, api_key):
        self.genai = genai
        self.genai.configure(api_key = api_key)
        self.model = self.genai.GenerativeModel('gemini-pro')
        self.conversation = None
        self.api_key = api_key
        self.conversation_history = []
        self.preload_Conversation()
    
    def generationConfig(self, temperature):
        return genai.types.GenerationConfig(temperature = temperature)
    
    def clearConversation(self):
        self.conversation = self.model.start_chat(history = [])
    
    def start_Conversation(self):
        self.conversation = self.model.start_chat(history = self.conversation_history)
    
    def preload_Conversation(self, conversation_history = None):
        if(isinstance(conversation_history, list)):
            self.conversation_history = conversation_history
        else:
            self.conversation_history = [construct_message('From now on, return the output as a JSON object that can be loaded into python with they key as \'text\' . For example, {"text": "<output goes here>"}'),
                                         construct_message('{"text": "Sure, I can return the output as a regular JSON object with the key as `text`. Here is an example: {"text": "Your output"}.', 'model')]
    
    def send_Prompt(self, prompt, temperature = 0.1):
        if(temperature < 0 or temperature > 1):
            raise GenAIException('Temperature must be between 0 and 1')
        if not prompt:
            raise GenAIException('Prompt cannot be empty')
        try:
            response = self.conversation.send_message(
                content = prompt,
                generation_config = self.generationConfig(temperature = temperature)
            )
            response.resolve()
            self.conversation_history.append(construct_message(response.text, 'model'))
            return response.text + '\n' + '---' * 20
        except Exception as excep:
            raise GenAIException(excep.message)
        
    def history(self):
        conversation_history = [{'role': message.role, 'text': message.parts[0].text} for message in self.conversation.history]
        return conversation_history