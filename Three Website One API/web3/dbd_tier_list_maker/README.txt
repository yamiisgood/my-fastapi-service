DBDLE - THREE MODE VERSION

PAGES
- index.html
  Main page / mode selection

- game.html
  Main game page

- style.css
  Shared styles for both pages

- app.js
  Game logic and API connection


MODES

Survivor:
game.html?mode=survivor

Only Survivor characters are loaded into the game pool.

Killer:
game.html?mode=killer

Only Killer characters are loaded into the game pool.

Mixed:
game.html?mode=mixed

Both Survivors and Killers are included.


HOW THE MODE SYSTEM WORKS

The home page passes the mode through the URL:

game.html?mode=survivor

JavaScript reads it with URLSearchParams.

It then filters the characters returned by the existing FastAPI.


API

https://my-fastapi-service-gi31.vercel.app/api/v1

No changes to index.py are required.


RUN

Use VS Code Live Server and open index.html.

RESULT POPUP
- Correct guess opens a popup result card.
- Give Up opens the same popup card.
- Popup shows character image, name, role/origin/DLC/year.
- Includes Play Again and Change Mode buttons.
- Can be closed with X or Escape.
