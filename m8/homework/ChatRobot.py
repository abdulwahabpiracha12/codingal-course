# Base class: Robot
class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def introduce(self):
        print("Hello! I am {}, version {}.".format(self.name, self.version))


# Derived class: ChatRobot (inherits from Robot)
class ChatRobot(Robot):
    def __init__(self, name, version, language, purpose):
        super().__init__(name, version)
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
    def __init__(self, organization):
        self.organization = organization

    def introduce_creator(self):
        print("I was created by {}.".format(self.organization))


# Main Program
if __name__ == "__main__":
    # Create objects
    creator = Creator("OpenAI")
    chatgpt = ChatRobot("ChatGPT", "5.0", "English & many more", "to assist and provide knowledge")

    # Robot introduction
    chatgpt.introduce()
    creator.introduce_creator()

    # Example interaction
    chatgpt.answer_question("What is Artificial Intelligence?")