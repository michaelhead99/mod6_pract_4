# main.py

import tkinter as tk
from functions import fetch_content

def main():
    def on_fetch_button_click():
        url = url_entry.get()
        title, content, image_count = fetch_content(url)

        title_label.config(text=f"Page Title: {title}")
        content_label.config(text=f"First 200 Characters:\n{content}")
        image_count_label.config(text=f"Image Count: {image_count}")

    root = tk.Tk()
    root.title("Web Page Content Fetcher")

    url_label = tk.Label(root, text="Enter URL:")
    url_label.grid(row=0, column=0, padx=10, pady=10)

    url_entry = tk.Entry(root, width=40)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    fetch_button = tk.Button(root, text="Fetch Content", command=on_fetch_button_click)
    fetch_button.grid(row=0, column=2, padx=10, pady=10)

    title_label = tk.Label(root, text="Page Title:")
    title_label.grid(row=1, column=0, columnspan=3, pady=10)

    content_label = tk.Label(root, text="First 200 Characters:")
    content_label.grid(row=2, column=0, columnspan=3, pady=10)

    image_count_label = tk.Label(root, text="Image Count:")
    image_count_label.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
