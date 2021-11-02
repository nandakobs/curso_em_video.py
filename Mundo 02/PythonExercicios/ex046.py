from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
emojiss = emoji.emojize(':tada:', use_aliases=True)
print(emojiss * 20)