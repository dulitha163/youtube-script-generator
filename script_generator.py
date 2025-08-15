import random

def generate_script(topic):
    intros = [
        f"Welcome back to the channel! Today, we're diving into {topic}.",
        f"Hello everyone! In this video, we'll explore {topic}.",
        f"Let's talk about {topic} – something that's trending right now!"
    ]

    middles = [
        f"{topic} is changing the way we work, live, and interact with technology.",
        f"There are many reasons why {topic} is important today.",
        f"In recent years, {topic} has gained massive attention globally."
    ]

    outros = [
        "If you enjoyed this video, don't forget to like and subscribe!",
        "Thanks for watching – see you in the next one!",
        "Leave a comment below on what you want us to cover next!"
    ]

    script = f"{intros[random.randint(0, len(intros)-1)]}\n\n{middles[random.randint(0, len(middles)-1)]}\n\n{outros[random.randint(0, len(outros)-1)]}"
    return script

if __name__ == "__main__":
    topic = input("Enter your video topic: ")
    script = generate_script(topic)
    print("\n--- Generated YouTube Script ---\n")
    print(script)