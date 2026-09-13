const API_URL = "https://my-fastapi-service-gi31.vercel.app";

let currentPage = 0;
const limit = 10;
let currentRole = "";
let currentQuery = "";

const fetchOptions = {
    cache: "no-store",
    headers: {
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache"
    }
};

// GET ALL CHARACTERS
async function loadCharacters(page = 0, role = "") {
    try {
        currentPage = parseInt(page, 10);
        currentRole = role;
        currentQuery = "";
        
        const offset = currentPage * limit;
        let url = `${API_URL}/characters?limit=${limit}&offset=${offset}`;
        
        if (role) {
            url += `&role=${encodeURIComponent(role)}`;
        }

        const response = await fetch(url, fetchOptions);
        const data = await response.json();
        
        displayCharacters(data.characters);
        updatePaginationControls(data.total, currentPage);
    } catch (error) {
        console.error("Error loading characters:", error);
        const container = document.getElementById("characterList") || document.getElementById("agentList");
        if (container) {
            container.innerHTML = "<p>Unable to connect to the API.</p>";
        }
    }
}

// DISPLAY CHARACTERS IN GRID
function displayCharacters(characters) {
    const listContainer = document.getElementById("characterList") || document.getElementById("agentList");
    if (!listContainer) return;
    
    listContainer.innerHTML = "";

    if (!characters || characters.length === 0) {
        listContainer.innerHTML = "<p>No characters found in the fog.</p>";
        return;
    }

    characters.forEach(character => {
        const card = document.createElement("div");
        card.className = "agent-card";
        card.onclick = () => viewCharacter(character.id);
        
        // Image support with fallback placeholder
        const imageUrl = character.image || 'https://via.placeholder.com/300x400/090a0c/a82424?text=DBD+Entity';

        card.innerHTML = `
            <div class="agent-year">${character.character_code}</div>
            <div class="card-portrait">
                <img src="${imageUrl}" alt="${character.name}" loading="lazy" onerror="this.src='https://via.placeholder.com/300x400/090a0c/a82424?text=DBD+Entity'">
            </div>
            <div class="card-content">
                <h3>${character.name}</h3>
                <p class="agent-origin">${character.role} • ${character.realm}</p>
                <button onclick="event.stopPropagation(); viewCharacter(${character.id})">View Details</button>
            </div>
        `;
        listContainer.appendChild(card);
    });
}

// GET SINGLE CHARACTER FOR MODAL
async function viewCharacter(id) {
    try {
        const response = await fetch(`${API_URL}/characters/${id}`, fetchOptions);
        if (!response.ok) throw new Error("Character not found");

        const character = await response.json();
        const modalBody = document.getElementById("modalBody");
        if (!modalBody) return;

        const imageUrl = character.image || 'https://via.placeholder.com/300x400/090a0c/a82424?text=DBD+Entity';
        const powerSection = character.power && character.power !== "None"
            ? `<p><strong>Power:</strong> ${character.power}</p>`
            : `<p><strong>Power:</strong> N/A (Survivor)</p>`;

        modalBody.innerHTML = `
            <div class="modal-body-layout">
                <img src="${imageUrl}" alt="${character.name}" class="modal-portrait" onerror="this.src='https://via.placeholder.com/300x400/090a0c/a82424?text=DBD+Entity'">
                <div class="modal-header">
                    <h2>${character.name} <span style="font-size: 0.85rem; color: #808792;">[${character.character_code}]</span></h2>
                    <p class="agent-origin">${character.role} • ${character.gender} • ${character.origin}</p>
                    <p style="font-size: 0.85rem; color: #808792; margin-top: 0.4rem;">
                        <strong>Difficulty:</strong> ${character.difficulty} | <strong>Released:</strong> ${character.year}
                    </p>
                </div>
            </div>
            
            <p style="line-height: 1.6;">${character.description}</p>

            <div class="skills-list">
                <p><strong>Realm:</strong> ${character.realm}</p>
                <p><strong>DLC Chapter:</strong> ${character.dlc}</p>
                ${powerSection}
                <p><strong>Perk 1:</strong> ${character.perk_1 || 'N/A'}</p>
                <p><strong>Perk 2:</strong> ${character.perk_2 || 'N/A'}</p>
                <p><strong>Perk 3:</strong> ${character.perk_3 || 'N/A'}</p>
            </div>
        `;

        const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
        if (modal) modal.style.display = "flex";
    } catch (error) {
        console.error("Error fetching character details:", error);
        alert("Unable to retrieve character details.");
    }
}

// CLOSE MODAL
function closeModal() {
    const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
    if (modal) modal.style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById("agentModal") || document.getElementById("characterModal");
    if (modal && event.target === modal) modal.style.display = "none";
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
        currentPage = parseInt(page, 10);
        currentQuery = query;
        const offset = currentPage * limit;

        const response = await fetch(
            `${API_URL}/characters/search?q=${encodeURIComponent(query)}&limit=${limit}&offset=${offset}`,
            fetchOptions
        );
        const data = await response.json();
        
        displayCharacters(data.results);
        updatePaginationControls(data.total, currentPage);
    } catch (error) {
        console.error("Search failed:", error);
        alert("Search failed.");
    }
}

// RENDER PAGINATION BUTTONS
function updatePaginationControls(totalItems, page) {
    const paginationContainer = document.getElementById("paginationContainer");
    if (!paginationContainer) return;

    const totalPages = Math.ceil(totalItems / limit);
    const prevDisabled = page <= 0 ? 'disabled' : '';
    const nextDisabled = (page + 1) >= totalPages ? 'disabled' : '';

    paginationContainer.innerHTML = `
        <button ${prevDisabled} onclick="changePage(${page - 1})">Previous</button>
        <span>Page ${page + 1} of ${totalPages || 1}</span>
        <button ${nextDisabled} onclick="changePage(${page + 1})">Next</button>
    `;
}

function changePage(newPage) {
    if (newPage < 0) return;
    if (currentQuery) {
        searchCharacters(newPage);
    } else {
        loadCharacters(newPage, currentRole);
    }
}

// INITIAL LOAD
loadCharacters(0);
