const API_URL = "https://my-fastapi-service-gi31.vercel.app/api";

let currentPage = 0;
const limit = 10;
let currentRole = "";
let currentQuery = "";

// GET ALL CHARACTERS (WITH PAGINATION AND OPTIONAL ROLE FILTER)
async function loadCharacters(page = 0, role = "") {
    try {
        currentPage = page;
        currentRole = role;
        currentQuery = ""; // Reset search when loading main list
        
        const offset = page * limit;
        let url = `${API_URL}/characters?limit=${limit}&offset=${offset}`;
        
        if (role) {
            url += `&role=${encodeURIComponent(role)}`;
        }

        const response = await fetch(url);
        const data = await response.json();
        
        displayCharacters(data.characters);
        updatePaginationControls(data.total, page);
    } catch (error) {
        console.error("Error loading characters:", error);
        const container = document.getElementById("characterList") || document.getElementById("agentList");
        if (container) {
            container.innerHTML = "<p>Unable to connect to the API.</p>";
        }
    }
}

// DISPLAY CHARACTERS IN GRID / CARDS
function displayCharacters(characters) {
    const listContainer = document.getElementById("characterList") || document.getElementById("agentList");
    if (!listContainer) return;
    
    listContainer.innerHTML = "";

    if (!characters || characters.length === 0) {
        listContainer.innerHTML = "<p>No characters found.</p>";
        return;
    }

    characters.forEach(character => {
        const card = document.createElement("div");
        card.className = "agent-card";
        
        // Display specific power info if present
        const powerDisplay = character.power && character.power !== "None" 
            ? `<p><strong>Power:</strong> ${character.power}</p>` 
            : "";

        card.innerHTML = `
            <div class="agent-year">${character.character_code}</div>
            <h3>${character.name} (${character.role})</h3>
            <p class="agent-origin"><strong>Origin:</strong> ${character.origin} | <strong>Realm:</strong> ${character.realm}</p>
            <p><strong>DLC:</strong> ${character.dlc} (${character.year})</p>
            ${powerDisplay}
            <p><strong>Perks:</strong> ${character.perk_1}, ${character.perk_2}, ${character.perk_3}</p>
            <p>${character.description}</p>
            <button onclick="viewCharacter(${character.id})">View Details</button>
        `;
        listContainer.appendChild(card);
    });
}

// GET SINGLE CHARACTER FOR MODAL VIEW
async function viewCharacter(id) {
    try {
        const response = await fetch(`${API_URL}/characters/${id}`);
        if (!response.ok) throw new Error("Character not found");

        const character = await response.json();

        const modalBody = document.getElementById("modalBody");
        if (!modalBody) return;

        // Render Power conditionally if character is a Killer
        const powerSection = character.power && character.power !== "None"
            ? `<p><strong>Power:</strong> ${character.power}</p>`
            : `<p><strong>Power:</strong> N/A (Survivor)</p>`;

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
                ${powerSection}
                <p><strong>Perk 1:</strong> ${character.perk_1 || 'N/A'}</p>
                <p><strong>Perk 2:</strong> ${character.perk_2 || 'N/A'}</p>
                <p><strong>Perk 3:</strong> ${character.perk_3 || 'N/A'}</p>
            </div>
        `;

        const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
        if (modal) {
            modal.style.display = "flex";
        }
    } catch (error) {
        console.error("Error fetching character details:", error);
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

// CLOSE MODAL WHEN CLICKING OUTSIDE BOUNDS
window.onclick = function(event) {
    const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
    if (modal && event.target === modal) {
        modal.style.display = "none";
    }
};

// SEARCH CHARACTERS
async function searchCharacters(page = 0) {
    const searchInput = document.getElementById("searchInput");
    const query = searchInput ? searchInput.value.trim() : "";
    
    if (!query) {
        loadCharacters(0, currentRole);
        return;
    }

    try {
        currentPage = page;
        currentQuery = query;
        const offset = page * limit;

        const response = await fetch(`${API_URL}/characters/search?q=${encodeURIComponent(query)}&limit=${limit}&offset=${offset}`);
        const data = await response.json();
        
        displayCharacters(data.results);
        updatePaginationControls(data.total, page);
    } catch (error) {
        console.error("Search failed:", error);
        alert("Search failed.");
    }
}

// OPTIONAL: PAGINATION UI CONTROLLER (Updates pagination buttons if present in your DOM)
function updatePaginationControls(totalItems, page) {
    const paginationContainer = document.getElementById("paginationContainer");
    if (!paginationContainer) return;

    const totalPages = Math.ceil(totalItems / limit);
    
    paginationContainer.innerHTML = `
        <button ${page === 0 ? 'disabled' : ''} onclick="changePage(${page - 1})">Previous</button>
        <span>Page ${page + 1} of ${totalPages || 1}</span>
        <button ${(page + 1) >= totalPages ? 'disabled' : ''} onclick="changePage(${page + 1})">Next</button>
    `;
}

function changePage(newPage) {
    if (currentQuery) {
        searchCharacters(newPage);
    } else {
        loadCharacters(newPage, currentRole);
    }
}

// BACKWARD COMPATIBILITY ALIASES
function searchAgents() {
    searchCharacters();
}

function loadAgents() {
    loadCharacters();
}

function viewAgent(id) {
    viewCharacter(id);
}

// INITIALIZATION
loadCharacters();
