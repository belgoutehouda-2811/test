full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # --- Validation ---
    if not isinstance(name, str):
        return 'The character name should be a string'

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    stats = {'STR': strength, 'INT': intelligence, 'CHA': charisma}
    for stat in stats.values():
        if not isinstance(stat, int):
            return 'All stats should be integers'
        if stat < 1:
            return 'All stats should be no less than 1'
        if stat > 4:
            return 'All stats should be no more than 4'

    if sum(stats.values()) != 7:
        return 'The character should start with 7 points'

    # --- Stat bar helper ---
    def stat_bar(value):
        return full_dot * value + empty_dot * (10 - value)

    # --- Final output ---
    return f"{name}\nSTR {stat_bar(strength)}\nINT {stat_bar(intelligence)}\nCHA {stat_bar(charisma)}"