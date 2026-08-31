const API_URL = "https://my-fastapi-service-gi31.vercel.app/api";

// GET ALL CHARACTERS
async function loadCharacters() {
    try {
        const response = await fetch(`${API_URL}/characters`);
        const data = await response.json();
        displayCharacters(data.characters);
    } catch (error) {
        console.error(error);
        const container = document.getElementById("characterList") || document.getElementById("agentList");
        if (container) {
            container.innerHTML = "Unable to connect to the API.";
        }
    }
}

// DISPLAY CHARACTERS
function displayCharacters(characters) {
    const listContainer = document.getElementById("characterList") || document.getElementById("agentList");
    if (!listContainer) return;
    
    listContainer.innerHTML = "";

    characters.forEach(character => {
        const card = document.createElement("div");
        card.className = "agent-card";
        card.innerHTML = `
            <div class="agent-year">${character.character_code}</div>
            <h3>${character.name} (${character.role})</h3>
            <p class="agent-origin"><strong>Origin:</strong> ${character.origin} | <strong>Realm:</strong> ${character.realm}</p>
            <p><strong>DLC:</strong> ${character.dlc} (${character.year})</p>
            <p><strong>Perks / Power:</strong> ${character.perk_1}, ${character.perk_2}, ${character.perk_3}</p>
            <p>${character.description}</p>
            <button onclick="viewCharacter(${character.id})">View Details</button>
        `;
        listContainer.appendChild(card);
    });
}

// GET ONE CHARACTER (DISPLAY IN MODAL WITH ALL 14 DETAILS)
async function viewCharacter(id) {
    try {
        const response = await fetch(`${API_URL}/characters/${id}`);
        const character = await response.json();

        const modalBody = document.getElementById("modalBody");
        if (!modalBody) return;

        modalBody.innerHTML = `
            <div class="modal-header">
                <h2>${character.name} <span style="font-size: 0.9rem; color: #768079;">[${character.character_code}]</span></h2>
                <p class="agent-origin">${character.role} • ${character.gender} • ${character.origin}</p>
                <p style="font-size: 0.85rem; color: #768079; margin-top: 0.2rem;">
                    <strong>Difficulty:</strong> ${character.difficulty} | <strong>Released:</strong> ${character.year}
                </p>
            </div>
            
            <p style="margin-top: 1rem;">${character.description}</p>

            <div class="skills-list" style="margin-top: 1rem;">
                <p><strong>Realm:</strong> ${character.realm}</p>
                <p><strong>DLC Chapter:</strong> ${character.dlc}</p>
                <p><strong>Perk / Power 1:</strong> ${character.perk_1 || 'N/A'}</p>
                <p><strong>Perk / Power 2:</strong> ${character.perk_2 || 'N/A'}</p>
                <p><strong>Perk / Power 3:</strong> ${character.perk_3 || 'N/A'}</p>
            </div>
        `;

        const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
        if (modal) {
            modal.style.display = "flex";
        }
    } catch (error) {
        console.error(error);
        alert("Unable to retrieve character details.");
    }
}

// CLOSE MODAL
function closeModal() {
    const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
    if (modal) {
        modal.style.display = "none";
    }
}

// CLOSE MODAL WHEN CLICKING OUTSIDE BOX
window.onclick = function(event) {
    const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
    if (modal && event.target === modal) {
        modal.style.display = "none";
    }
};

// SEARCH CHARACTERS
async function searchCharacters() {
    const searchInput = document.getElementById("searchInput");
    const query = searchInput ? searchInput.value : "";
    
    if (!query) {
        loadCharacters();
        return;
    }
    try {
        const response = await fetch(`${API_URL}/characters/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayCharacters(data.results);
    } catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}

// ALIAS FUNCTIONS FOR BACKWARD COMPATIBILITY WITH EXISTING HTML
function searchAgents() {
    searchCharacters();
}

function loadAgents() {
    loadCharacters();
}

function viewAgent(id) {
    viewCharacter(id);
}

// INITIAL LOAD
loadCharacters();
