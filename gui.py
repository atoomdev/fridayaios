import tkinter as tk

class FridayGUI:
    """Simple GUI showing an animated face and recognized text."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Friday")

        # Create two simple frames with different colors as a basic animation
        frame1 = tk.PhotoImage(width=128, height=128)
        frame1.put("#00aaff", to=(0, 0, 128, 128))
        frame2 = tk.PhotoImage(width=128, height=128)
        frame2.put("#0055aa", to=(0, 0, 128, 128))
        self.frames = [frame1, frame2]

        self.image_label = tk.Label(self.root, image=self.frames[0])
        self.image_label.pack(pady=10)

        self.heard_var = tk.StringVar()
        self.response_var = tk.StringVar()

        tk.Label(self.root, textvariable=self.heard_var).pack()
        tk.Label(self.root, textvariable=self.response_var, fg="green").pack()

        controls = tk.Frame(self.root)
        controls.pack(pady=5)
        self.start_btn = tk.Button(controls, text="Start", command=self.start)
        self.stop_btn = tk.Button(controls, text="Stop", command=self.stop, state=tk.DISABLED)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        self.running = False
        self._animate_index = 0
        self.animate()

    def animate(self):
        self.image_label.configure(image=self.frames[self._animate_index])
        self._animate_index = (self._animate_index + 1) % len(self.frames)
        self.root.after(400, self.animate)

    def start(self):
        self.running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

    def stop(self):
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

    def update_text(self, text):
        self.heard_var.set(f"Heard: {text}")

    def update_response(self, resp):
        self.response_var.set(f"Response: {resp}")

    def mainloop(self):
        self.root.mainloop()
