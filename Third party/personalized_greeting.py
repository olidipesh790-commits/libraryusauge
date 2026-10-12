import emoji

name = input("Enter your name: ").strip()
print(emoji.emojize(f"Hello {name}! :smile:"))
print(emoji.emojize("Keep learning Python! :thumbs_up:"))

activity = input("What is your favorite activity? ").strip()
print(emoji.emojize(f"Wow, {activity} sounds great, {name}! :red_heart: Enjoy it! :party_popper:"))