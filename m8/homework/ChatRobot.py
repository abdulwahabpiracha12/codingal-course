# Base class: Robot
class Robot:
    def _init_(self, name, version):
        self.name = name
        self.version = version

    def introduce(self):
        print("Hello! I am {}, version {}.".format(self.name, self.version))


# Derived class: ChatRobot (inherits from Robot)
class ChatRobot(Robot):
    def _init_(self, name, version, language, purpose):
        super()._init_(name, version)
        self.language = language
        self.purpose = purpose

    def introduce(self):
        super().introduce()
        print("I can communicate in {}.".format(self.language))
        print("My purpose is {}.".format(self.purpose))

    def answer_question(self, question):
        print("You asked: {}".format(question))
        print("I will try my best to answer it using my knowledge.")


# Another class to represent Creator
class Creator:
    def _init_(self, organization):
        self.organization = organization

    def introduce_creator(self):
        print("I was created by {}.".format(self.organization))


# Main Program
if _name_ == "_main_":
    # Create objects
    creator = Creator("OpenAI")
    chatgpt = ChatRobot("ChatGPT", "5.0", "English & many more", "to assist and provide knowledge")

    # Robot introduction
    chatgpt.introduce()
    creator.introduce_creator()

    # Example interaction
    chatgpt.answer_question("What is Artificial Intelligence?")