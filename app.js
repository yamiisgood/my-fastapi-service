const API_URL = "https://my-fastapi-service-gi31.vercel.app/api";

// GET ALL AGENTS
async function loadAgents() {
    try {
        const response = await fetch(`${API_URL}/agents`);
        const data = await response.json();
        displayAgents(data.agents);
    } catch (error) {
        console.error(error);
        document.getElementById("agentList").innerHTML = "Unable to connect to the API.";
    }
}

// DISPLAY AGENTS
function displayAgents(agents) {
    const agentList = document.getElementById("agentList");
    agentList.innerHTML = "";

    agents.forEach(agent => {
        const card = document.createElement("div");
        card.className = "agent-card";
        card.innerHTML = `
            <div class="agent-year">${agent.year}</div>
            <h3>${agent.name} (${agent.Role})</h3>
            <p class="agent-origin">Origin: ${agent.origin}</p>
            <p><strong>Ultimate:</strong> ${agent.ultimate}</p>
            <p>${agent.description}</p>
            <button onclick="viewAgent(${agent.id})">View Details</button>
        `;
        agentList.appendChild(card);
    });
}

// GET ONE AGENT (DISPLAY IN MODAL)
async function viewAgent(id) {
    try {
        const response = await fetch(`${API_URL}/agents/${id}`);
        const agent = await response.json();

        const modalBody = document.getElementById("modalBody");
        modalBody.innerHTML = `
            <div class="modal-header">
                <h2>${agent.name} <span style="font-size: 0.9rem; color: #768079;">(#${agent.agent_number})</span></h2>
                <p class="agent-origin">${agent.Role} • ${agent.origin} (${agent.year})</p>
                <p style="font-size: 0.8rem; color: #768079; margin-top: 0.2rem;">Code Name: ${agent.code_name}</p>
            </div>
            
            <p>${agent.description}</p>

            <div class="skills-list">
                <p><strong>Ability 1:</strong> ${agent.skill_1 || 'N/A'}</p>
                <p><strong>Ability 2:</strong> ${agent.skill_2 || 'N/A'}</p>
                <p><strong>Signature:</strong> ${agent.signature || 'N/A'}</p>
                <p><strong>Ultimate:</strong> ${agent.ultimate || 'N/A'} (${agent.ult_points || 8} Points)</p>
            </div>
        `;

        document.getElementById("agentModal").style.display = "flex";
    } catch (error) {
        console.error(error);
        alert("Unable to retrieve agent details.");
    }
}

// CLOSE MODAL
function closeModal() {
    document.getElementById("agentModal").style.display = "none";
}

// CLOSE MODAL WHEN CLICKING OUTSIDE BOX
window.onclick = function(event) {
    const modal = document.getElementById("agentModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

// SEARCH AGENTS
async function searchAgents() {
    const query = document.getElementById("searchInput").value;
    if (!query) {
        loadAgents();
        return;
    }
    try {
        const response = await fetch(`${API_URL}/agents/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayAgents(data.results);
    } catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}

loadAgents();
