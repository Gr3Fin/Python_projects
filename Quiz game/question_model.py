# --- Create a class for a new_question object ---


class Question:

    def __init__(self, q_text, q_answer, q_category, q_lvl):
        self.text = q_text
        self.answer = q_answer
        self.category = q_category
        self.lvl = q_lvl
