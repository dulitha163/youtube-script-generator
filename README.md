# youtube-script-generator
Generate AI-powered YouTube scripts using Python

def generate_script(topic):
    intros = [
        f"Welcome back to the channel! Today, we’re diving into {topic}.",
        f"Hello everyone! In this video, we’ll explore {topic}.",
        f"Let’s talk about {topic} – something that’s trending right now!"
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

    script = f"{random.choice(intros)}\n\n{random.choice(middles)}\n\n{random.choice(outros)}"
    return script

if __name__ == "__main__":
    topic = input("Enter your video topic: ")
    script = generate_script(topic)
    print("\n--- Generated YouTube Script ---\n")
    print(script)
