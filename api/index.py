from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Valorant Agent Finder",
    description="A beginner-friendly REST API containing information about the Agents in Valorant.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AGENT DATA
agents = [

    {
        "id": 1,
        "name": "Omen",
        "Role": "Controller",
        "year": 2020,
        "origin": "Unknown",
        "ultimate": "From The Shadows",
        "description": "A phantom of a memory, Omen hunts in the shadows, blinding enemies, teleporting across the battlefield, and leaving paranoia in his wake as foes scramble to uncover where he will strike next."
    },

    {
        "id": 2,
        "name": "Neon",
        "Role": "Duelist",
        "year": 2022,
        "origin": "Philippines",
        "ultimate": "Overdrive",
        "description": "Filipino Agent Neon surges forward at shocking speeds, discharging bursts of bioelectric radiance as fast as her body generates it."
    },

    {
        "id": 3,
        "name": "Deadlock",
        "Role": "Sentinel",
        "year": 2023,
        "origin": "Norway",
        "ultimate": "Annihilation",
        "description": "Norwegian operative Deadlock deploys an array of cutting-edge nanowire to secure the battlefield from even the most lethal assault."
    },

    {
        "id": 4,
        "name": "Tejo",
        "Role": "Initiator",
        "year": 2025,
        "origin": "Colombia",
        "ultimate": "Armageddon",
        "description": "A veteran intelligence consultant from Colombia, Tejo's ballistic guidance system pressures the enemy to relinquish their ground—or their lives."
    },

    {
        "id": 5,
        "name": "Yoru",
        "Role": "Duelist",
        "year": 2021,
        "origin": "Japan",
        "ultimate": "Dimensional Drift",
        "description": "Japanese native Yoru rips through reality to infiltrate enemy lines unseen. Employing deception and aggression in equal measure, he takes targets down before they even know where to look."
    },

    {
        "id": 6,
        "name": "Gekko",
        "Role": "Initiator",
        "year": 2023,
        "origin": "United States",
        "ultimate": "Thrash",
        "description": "Gekko the Angeleno leads a tight-knit crew of calamitous creatures. His buddies bound forward, scattering enemies out of the way, with Gekko chasing them down to regroup and go again."
    }

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Valorant Agents API!",
        "endpoints": [
            "/agents",
            "/agents/{agent_id}",
            "/agents/search"
        ]
    }


# GET ALL AGENTS
@app.get("/agents")
def get_agents():

    return {
        "count": len(agents),
        "agents": agents
    }


# SEARCH AGENTS 
@app.get("/agents/search")
def search_agents( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for agent in agents:
        searchable_text = (
            f"{agent['name']} "
            f"{agent['Role']} "
            f"{agent['year']} "
            f"{agent['origin']} "
            f"{agent['ultimate']}"
        ).lower()

        if q in searchable_text:
            results.append(agent)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }


# GET ONE AGENT
@app.get("/agents/{agent_id}")
def get_agent(agent_id: int):

    for agent in agents:

        if agent["id"] == agent_id:
            return agent

    raise HTTPException(
        status_code=404,
        detail="Agent not found."
    )
