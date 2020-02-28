
from flask_ask import statement, question

YES_WORDS = ["yes", "correct", "yup", "definitely"]

NO_WORDS = ["no", "nope", "incorrect", "wrong"]


class Labeler(object):
    def __init__(self):
        self.potential_food = None

    def get_intro_statement(self):
        return question("Welcome to leftover printer. First item?")

    def handle_statement(self, statement):
        """
        Handle whatever the person said to Alexa
        Stores context - whether you've already said a word
        and need to confirm before printing
        Returns the type of response to give to the user
        """
        if self.potential_food is None:
            if self._is_yes(statement) or self._is_no(statement):
                return question("Item to add?")
            self.potential_food = statement
            return self._gen_confirmation(statement)
        else:
            if self._is_yes(statement):
                # We should print the label!
                self._print_label(self.potential_food)
                self.potential_food = None
                return question("Printing label. Next item?")
            elif self._is_no(statement):
                self.potential_food = None
                return question("Cancelled. Next item?")
            else:
                return self._gen_confirmation(self.potential_food)

    def _gen_confirmation(self, potential_food):
        """
        Generate a confirmation question - asks if the food item was correctly identified
        """
        return question("{}, correct?".format(potential_food))

    def _print_label(self, potential_food):
        """
        Actually print out the label
        """
        pass

    def _is_yes(self, word):
        """
        Determine if word means "yes", so we can go ahead and print the label.
        """
        return word in YES_WORDS

    def _is_no(self, word):
        """
        Determine if the word means "no", we don't agree that this label should be printed.
        """
        return word in NO_WORDS
