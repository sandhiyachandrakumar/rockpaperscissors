from django.shortcuts import render
from .models import GameResult  # Importing the model to save game data
import random

def play_game(request):
    result = ""
    user_choice = "" 
    computer_choice = ""

    if request.method == "POST":
        user_choice = request.POST['choice']
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "Draw!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
        else:
            result = "Computer wins!"

        # ✅ Save to database only after POST is confirmed
        GameResult.objects.create(
            user_choice=user_choice,
            computer_choice=computer_choice,
            result=result
        )

    # Finally render the template with context
    return render(request, 'play.html', {
        'result': result,
        'user_choice': user_choice,
        'computer_choice': computer_choice,
    })
