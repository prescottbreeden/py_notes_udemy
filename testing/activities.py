def eat(food, is_healthy):
    if is_healthy:
        return f"I'm eating {food}, because my body is a temple"
    return f"I'm eating {food}, because YOLO"


def nap(num_hours):
    if num_hours < 3:
        return f"I'm feeling refreshed after my {num_hours} hour nap"
    return f"Ugh I overslept. I didn't mean to nap for {num_hours} hours"
