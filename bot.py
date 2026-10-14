
import pyautogui
import pyperclip
import time

from gemini import generate_reply

# Step 1: Click the icon
pyautogui.click(2065, 1741)
time.sleep(1)

# Step 2: Select the chat history
pyautogui.moveTo(905, 574, duration=0.3)
pyautogui.dragTo(1923, 1542, duration=1)
time.sleep(0.5)

# Step 3: Copy the selected text
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Step 4: Save chat history
chat_history = pyperclip.paste()

if not chat_history.strip():
    raise ValueError("No chat history was copied.")

print("Copied chat history:")
print(chat_history)

# Step 5: Generate reply using Gemini
response = generate_reply(chat_history)

if not response or not response.strip():
    raise ValueError("Gemini returned an empty response.")

print("\nAryan's reply:")
print(response)

# Step 6: Copy the reply
pyperclip.copy(response)
time.sleep(0.3)

# Step 7: Click the target chatbox
pyautogui.click(1298, 1632)
time.sleep(0.5)

# Step 8: Paste the reply
pyautogui.hotkey("ctrl", "v")
time.sleep(0.5)

# Step 9: Send the reply
pyautogui.press("enter")

print("\nReply pasted and sent.")