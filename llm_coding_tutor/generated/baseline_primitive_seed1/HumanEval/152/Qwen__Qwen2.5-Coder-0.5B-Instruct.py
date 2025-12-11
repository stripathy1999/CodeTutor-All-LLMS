def compare(game,guess):
    return [abs(score - guess) for score, guess in zip(game, guess)]
```