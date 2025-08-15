import random

def generate_cat_story_script():
    intros = [
        "Welcome back to the channel! Today, I have the most heartwarming cat story to share with you.",
        "Hello cat lovers! Get ready for a story that will make you smile and maybe shed a happy tear.",
        "If you love cats as much as I do, you're going to absolutely love today's story!"
    ]

    story_beginnings = [
        "It all started when a little tabby cat wandered into someone's backyard, looking lost and hungry.",
        "This story begins with a rescue cat who had given up on finding a forever home.",
        "Meet Whiskers, a street cat who thought he'd never know what love felt like."
    ]

    story_middles = [
        "What happened next will restore your faith in humanity and show you just how amazing cats can be.",
        "The bond that formed between this cat and their new family is something truly special.",
        "This cat's transformation from scared and alone to confident and loved is incredible to witness."
    ]

    story_endings = [
        "Today, this once-homeless cat is living their best life, surrounded by love and comfort.",
        "The family says they rescued the cat, but honestly, I think the cat rescued them right back.",
        "This story proves that sometimes the best things in life come when you least expect them."
    ]

    outros = [
        "If this story touched your heart, please give it a thumbs up and share it with fellow cat lovers!",
        "Do you have a heartwarming cat story? Share it in the comments below – I'd love to hear it!",
        "Thanks for watching, and remember – every cat deserves a loving home. See you next time!"
    ]

    script = f"{random.choice(intros)}\n\n{random.choice(story_beginnings)}\n\n{random.choice(story_middles)}\n\n{random.choice(story_endings)}\n\n{random.choice(outros)}"
    return script

if __name__ == "__main__":
    script = generate_cat_story_script()
    print("\n--- Generated Cat Story YouTube Script ---\n")
    print(script)