import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Saturn", "Venus"],
        "answer": "Mars"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")
        
        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar()
        
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=350, font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected_option, value="", font=("Arial", 12))
            rb.pack(anchor='w', padx=50)
            self.options.append(rb)
        
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

    def load_question(self):
        q = questions[self.current_question]
        self.question_label.config(text=q["question"])
        self.selected_option.set(None)
        
        for i, option in enumerate(q["options"]):
            self.options[i].config(text=option, value=option)

    def next_question(self):
        if not self.selected_option.get():
            messagebox.showwarning("Select an option", "Please select an answer before continuing.")
            return
        
        correct_answer = questions[self.current_question]["answer"]
        if self.selected_option.get() == correct_answer:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question == len(questions):
            messagebox.showinfo("Quiz Completed", f"You scored {self.score} out of {len(questions)}!")
            self.root.destroy()
        else:
            self.load_question()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
