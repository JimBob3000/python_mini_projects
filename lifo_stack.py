from collections import deque


url_history = deque()

print("EXAMLE LIFO STACK OF A BROWSER BACK BUTTON\n")

print("Opening browser, adding google homepage url")
url_history.appendleft("https://google.co.uk/")

print("User searched for 'Python', adding url")
url_history.appendleft("https://google.co.uk/search?q=python")

print("User clicked a link to 'python.org', adding url")
url_history.appendleft("https://python.org")

print("User clicked the 'about' button, adding url\n")
url_history.appendleft("https://python.org/about/")

print(f"CURRENT HISTORY:\n {url_history}\n")

print("User clicked the browser back button, popping url")
url_history.popleft()

print(f"User is sent to: {url_history[0]}\n")
