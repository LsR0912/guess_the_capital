# Guess the Capital

Guess the capital is an interactive quiz game built with Python and Tkinter. The game challenges users to guess the capital city of a randomly selected country, displays the country's flag, and provides additional information about each country.

## Features

- Randomly selects a country and displays its flag.
- Multiple-choice options for guessing the capital.
- Score tracking.
- Region selection to focus on specific parts of the world.
- "More Info" button to display detailed information and a map for the last country.

## Requirements

Install dependencies using pip:

```
pip install -r requirements.txt
```

Dependencies:
- `requests`
- `pywebview`
- `pillow`
- `tkinter` (usually included with Python)

## Usage

Run the main script:

```
python src/main.py
```

## Project Structure

```
requirements.txt
data/
    countries.json
src/
    country.py
    game_logic.py
    game.py
    info_window.py
    main.py
    utils/
        image_helper.py
```

- `src/main.py`: Entry point for the application.
- `src/game_logic.py`: Main game logic and GUI setup.
- `src/game.py`: Game state and logic.
- `src/country.py`: Country data model.
- `src/info_window.py`: Displays additional country information.
- `src/utils/image_helper.py`: Helper functions for image/flag handling.
- `data/countries.json`: Country data.

## How to Play

1. Start the game.
2. Select a region (optional).
3. Guess the capital city for the displayed country and flag.
4. Click "More Info" after each round to learn more about the previous country.

## License

MIT License
