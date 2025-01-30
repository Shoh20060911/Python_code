# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:13:43 2025

@author: Shohjahon
"""

import json
import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

class FlashcardApp:
    def __init__(self, filename="flashcards.json"):
        self.filename = filename
        self.flashcards = self.load_flashcards()

    def load_flashcards(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Flashcard(q, a) for q, a in data.items()]
        except FileNotFoundError:
            return []

    def save_flashcards(self):
        with open(self.filename, "w") as file:
            json.dump({card.question: card.answer for card in self.flashcards}, file)

    def add_flashcard(self, question, answer):
        self.flashcards.append(Flashcard(question, answer))
        self.save_flashcards()

    def quiz(self):
        if not self.flashcards:
            print("No flashcards available.")
            return

        card = random.choice(self.flashcards)
        print(f"Question: {card.question}")
        user_answer = input("Your answer: ")

        if card.check_answer(user_answer):
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer is: {card.answer}")

# Running the program
app = FlashcardApp()

while True:
    print("\n1. Add Flashcard\n2. Quiz Yourself\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        q = input("Enter question: ")
        a = input("Enter answer: ")
        app.add_flashcard(q, a)
        print("Flashcard added!")
    elif choice == "2":
        app.quiz()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
