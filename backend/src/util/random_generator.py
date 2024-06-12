from secrets import randbelow


def generate_survey_code(survey_code_length=6):
    return "".join(str(randbelow(10)) for _ in range(survey_code_length))
