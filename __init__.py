from mycroft import MycroftSkill, intent_file_handler


class SynonymFinder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('finder.synonym.intent')
    def handle_finder_synonym(self, message):
        self.speak_dialog('finder.synonym')


def create_skill():
    return SynonymFinder()

