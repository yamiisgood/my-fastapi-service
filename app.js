const API_URL = "https://my-fastapi-service-eight.vercel.app/api";


// GET ALL AGENTS
async function loadAgents() {
    try {
        const response = await fetch(`${API_URL}/agents`);
        const data = await response.json();
        displayAgents(data.agents);
    }

    catch (error) {
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
            <button onclick="viewAgent(${agent.id})"> View Details</button>
        `;

        agentList.appendChild(card);
    });

}

// GET ONE AGENT
async function viewAgent(id) {

    try {
        const response = await fetch(`${API_URL}/agents/${id}`);
        const agent = await response.json();

        alert(`
            ${agent.name} - ${agent.Role} (${agent.year})
            Origin:
            ${agent.origin}

            Ultimate Ability:
            ${agent.ultimate}

            Description:
            ${agent.description}
        `);
    }
    catch (error) {
        console.error(error);
        alert("Unable to retrieve agent.");
    }

}

// SEARCH
async function searchAgents() {

    const query = document.getElementById("searchInput").value;
    if (!query) {
        loadAgents();
        return;
    }
    try {
        const response = 
            await fetch(`${API_URL}/agents/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayAgents(data.results);
    }

    catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}

loadAgents();
