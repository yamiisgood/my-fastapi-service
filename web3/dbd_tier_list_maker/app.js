const API_BASE_URL = "https://my-fastapi-service-gi31.vercel.app/api/v1";

const API_KEY = "student-api-key-123";

const params = new URLSearchParams(window.location.search);

let selectedMode = params.get("mode") || "mixed";

selectedMode = selectedMode.toLowerCase();

const datalist = document.getElementById("characterNames");

const guessForm = document.getElementById("guessForm");

const guessInput = document.getElementById("guessInput");

const guessRows = document.getElementById("guessRows");

const attemptCount = document.getElementById("attemptCount");

const giveUpBtn = document.getElementById("giveUpBtn");

const resultPanel = document.getElementById("resultPanel");

const resultEyebrow = document.getElementById("resultEyebrow");

const resultImage = document.getElementById("resultImage");

const resultName = document.getElementById("resultName");

const resultInfo = document.getElementById("resultInfo");

const playAgainBtn = document.getElementById("playAgainBtn");

const closeResultBtn = document.getElementById("closeResultBtn");

const gameModeTitle = document.getElementById("gameModeTitle");

const modeEyebrow = document.getElementById("modeEyebrow");

const modeDescription = document.getElementById("modeDescription");

let characters = [];
let activeCharacters = [];
let answer = null;
let attempts = 0;
let finished = false;
let guessedIds = new Set();

const difficultyOrder = {
    "Easy": 1,
    "Intermediate": 2,
    "Hard": 3,
    "Very Hard": 4
};

async function loadCharacters() {
    try {
        const response = await fetch(
            `${API_BASE_URL}/characters?limit=100&offset=0&sort_by=name&order=asc`,
            {
                headers: {
                    "x-api-key": API_KEY
                }
            }
        );

        if (!response.ok) {
            throw new Error(
                `API error: ${response.status}`
            );
        }

        const data = await response.json();

        characters = data.characters || [];

        if (characters.length === 0) {
            throw new Error(
                "No characters returned by API."
            );
        }

        configureMode();

        fillCharacterNames();

        startRound();
    }

    catch (error) {
        console.error(error);

        guessInput.placeholder = "API COULD NOT BE LOADED";

        guessInput.disabled = true;
    }
}

function configureMode() {
    if (selectedMode === "survivor") {
        activeCharacters =
            characters.filter(
                character =>
                    character.role === "Survivor"
            );

        modeEyebrow.textContent = "SURVIVOR ONLY";

        gameModeTitle.textContent = "SURVIVOR MODE";

        modeDescription.textContent = "Only Survivors can be the hidden answer.";
    }

    else if (selectedMode === "killer") {
        activeCharacters =
            characters.filter(
                character =>
                    character.role === "Killer"
            );

        modeEyebrow.textContent = "KILLER ONLY";

        gameModeTitle.textContent = "KILLER MODE";

        modeDescription.textContent = "Only Killers can be the hidden answer.";
    }

    else {
        selectedMode = "mixed";

        activeCharacters = [...characters];

        modeEyebrow.textContent = "SURVIVORS + KILLERS";

        gameModeTitle.textContent = "MIXED MODE";

        modeDescription.textContent = "Survivors and Killers are both included.";
    }
}

function fillCharacterNames() {
    datalist.innerHTML = "";

    activeCharacters.forEach(character => {
        const option = document.createElement("option");

        option.value = character.name;

        datalist.appendChild(option);
    });
}

function startRound() {
    answer =
        activeCharacters[
            Math.floor(
                Math.random() *
                activeCharacters.length
            )
        ];

    attempts = 0;

    finished = false;

    guessedIds = new Set();

    attemptCount.textContent = "0";

    guessRows.innerHTML = "";

    guessInput.value = "";

    guessInput.disabled = false;

    resultPanel.classList.add(
        "hidden"
    );

    setTimeout(
        () => guessInput.focus(),
        100
    );
}

guessForm.addEventListener(
    "submit",

    event => {
        event.preventDefault();

        if (finished) {
            return;
        }

        const typed =
            normalize(
                guessInput.value
            );

        const guessedCharacter =
            activeCharacters.find(
                character =>
                    normalize(character.name)
                    === typed
            );

        if (!guessedCharacter) {
            flashInvalid();

            return;
        }

        if (
            guessedIds.has(
                guessedCharacter.id
            )
        ) {
            flashInvalid(
                "YOU ALREADY GUESSED THAT CHARACTER"
            );

            return;
        }

        guessedIds.add(
            guessedCharacter.id
        );

        attempts++;

        attemptCount.textContent = attempts;

        addGuessRow(
            guessedCharacter
        );

        guessInput.value = "";

        if (
            guessedCharacter.id
            === answer.id
        ) {
            finishRound(true);
        }
    }
);

function addGuessRow(character) {
    const row = document.createElement("div");

    row.className = "guess-row";

    row.appendChild(
        makeCharacterCell(character)
    );

    row.appendChild(
        makeTextCell(
            character.role,
            compareText(
                character.role,
                answer.role
            )
        )
    );

    row.appendChild(
        makeTextCell(
            character.gender,
            compareText(
                character.gender,
                answer.gender
            )
        )
    );

    row.appendChild(
        makeTextCell(
            character.origin,
            compareMultiValue(
                character.origin,
                answer.origin
            )
        )
    );

    row.appendChild(
        makeTextCell(
            character.realm,
            compareText(
                character.realm,
                answer.realm
            )
        )
    );

    row.appendChild(
        makeTextCell(
            character.dlc,
            compareDlc(
                character.dlc,
                answer.dlc
            )
        )
    );

    row.appendChild(
        makeNumberCell(
            character.year,
            answer.year
        )
    );

    row.appendChild(
        makeDifficultyCell(
            character.difficulty,
            answer.difficulty
        )
    );

    guessRows.prepend(
        row
    );
}

function makeCharacterCell(character) {
    const cell = document.createElement("div");

    cell.className = "guess-cell character-cell";

    const image = document.createElement("img");

    image.src = character.image || "";

    image.alt = character.name;

    const label = document.createElement("span");

    label.textContent = character.name;

    cell.appendChild(image);

    cell.appendChild(label);

    return cell;
}

function makeTextCell(
    value,
    state
) {
    const cell = document.createElement("div");

    cell.className = `guess-cell ${state}`;

    cell.textContent = value || "N/A";

    return cell;
}

function makeNumberCell(
    guessValue,
    answerValue
) {
    const cell = document.createElement("div");

    if (
        guessValue === answerValue
    ) {
        cell.className = "guess-cell correct";

        cell.textContent = guessValue;

        return cell;
    }

    cell.className = "guess-cell wrong";

    cell.textContent = guessValue;

    const arrow = document.createElement("span");

    arrow.className = "direction-arrow";

    arrow.textContent =
        guessValue < answerValue
            ? "↑"
            : "↓";

    cell.appendChild(
        arrow
    );

    return cell;
}

function makeDifficultyCell(
    guessDifficulty,
    answerDifficulty
) {
    const guessValue =
        difficultyOrder[
            guessDifficulty
        ] || 0;

    const answerValue =
        difficultyOrder[
            answerDifficulty
        ] || 0;

    const cell = document.createElement("div");

    if (
        guessDifficulty
        === answerDifficulty
    ) {
        cell.className = "guess-cell correct";

        cell.textContent = guessDifficulty;

        return cell;
    }

    cell.className = "guess-cell wrong";

    cell.textContent = guessDifficulty;

    if (
        guessValue &&
        answerValue
    ) {
        const arrow = document.createElement("span");

        arrow.className = "direction-arrow";

        arrow.textContent =
            guessValue < answerValue
                ? "↑"
                : "↓";

        cell.appendChild(
            arrow
        );
    }

    return cell;
}

function compareText(
    guess,
    target
) {
    return normalize(guess)
        === normalize(target)

        ? "correct"

        : "wrong";
}

function compareMultiValue(
    guess,
    target
) {
    if (
        normalize(guess)
        === normalize(target)
    ) {
        return "correct";
    }

    const guessParts = splitMultiValue(guess);

    const targetParts = splitMultiValue(target);

    const overlap =
        guessParts.some(
            part =>
                targetParts.includes(part)
        );

    return overlap
        ? "partial"
        : "wrong";
}

function compareDlc(
    guess,
    target
) {
    if (
        normalize(guess)
        === normalize(target)
    ) {
        return "correct";
    }

    const guessText = normalize(guess);

    const targetText = normalize(target);

    if (
        guessText.includes(
            targetText
        )
        ||
        targetText.includes(
            guessText
        )
    ) {
        return "partial";
    }

    return "wrong";
}

function splitMultiValue(value) {
    return String(value || "")
        .toLowerCase()
        .split(/[,/&]/)
        .map(
            item => item.trim()
        )
        .filter(Boolean);
}

function normalize(value) {
    return String(value || "")
        .trim()
        .toLowerCase()
        .replace(
            /[’']/g,
            "'"
        )
        .replace(
            /\s+/g,
            " "
        );
}

function flashInvalid(
    message =
        "CHOOSE A VALID CHARACTER FOR THIS MODE"
) {
    const oldPlaceholder = guessInput.placeholder;

    guessInput.value = "";

    guessInput.placeholder = message;

    setTimeout(
        () => {
            guessInput.placeholder = oldPlaceholder;
        },
        1400
    );
}

giveUpBtn.addEventListener(
    "click",

    () => {
        if (finished) {
            return;
        }

        finishRound(false);
    }
);

function finishRound(won) {
    finished = true;

    guessInput.disabled = true;

    resultEyebrow.textContent =
        won
            ? "YOU FOUND THEM"
            : "THE FOG CLAIMED THIS ROUND";

    resultImage.src = answer.image || "";

    resultName.textContent = answer.name.toUpperCase();

    resultInfo.textContent =
        `${answer.role} • ` +
        `${answer.origin} • ` +
        `${answer.dlc} • ` +
        `${answer.year}`;

    resultPanel.classList.remove(
        "hidden"
    );
}

playAgainBtn.addEventListener(
    "click",

    () => {
        resultPanel.classList.add(
            "hidden"
        );

        startRound();

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    }
);

closeResultBtn.addEventListener(
    "click",

    () => {
        resultPanel.classList.add(
            "hidden"
        );
    }
);

document.addEventListener(
    "keydown",

    event => {
        if (
            event.key === "Escape" &&
            !resultPanel.classList.contains("hidden")
        ) {
            resultPanel.classList.add(
                "hidden"
            );
        }
    }
);

loadCharacters();