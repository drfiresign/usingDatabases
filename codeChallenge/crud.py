from models import Challenge


def create_challenge(name, language, steps=1):
    challenge = Challenge(name=name, language=language, steps=steps)
