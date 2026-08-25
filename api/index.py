from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Valorant Agent Finder",
    description="A beginner-friendly REST API containing information about the Agents in Valorant.",
    version="1.0.0",
    root_path="/api"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# COMPLETE AGENT DATA (26 AGENTS)
agents = [
    {
        "id": 1,
        "name": "Brimstone",
        "Role": "Controller",
        "year": 2020,
        "origin": "United States",
        "ultimate": "Orbital Strike",
        "description": "Joining from the USA, Brimstone's orbital arsenal ensures his squad always has the advantage. His ability to deliver utility precisely and safely makes him the ultimate boots-on-the-ground commander."
    },
    {
        "id": 2,
        "name": "Viper",
        "Role": "Controller",
        "year": 2020,
        "origin": "United States",
        "ultimate": "Viper's Pit",
        "description": "The American chemist Viper deploys an array of poisonous chemical devices to control the battlefield and cripple the enemy's vision."
    },
    {
        "id": 3,
        "name": "Omen",
        "Role": "Controller",
        "year": 2020,
        "origin": "Unknown",
        "ultimate": "From The Shadows",
        "description": "A phantom of a memory, Omen hunts in the shadows, blinding enemies, teleporting across the battlefield, and leaving paranoia in his wake."
    },
    {
        "id": 4,
        "name": "Killjoy",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "Germany",
        "ultimate": "Lockdown",
        "description": "The genius of Germany, Killjoy secures the battlefield easefully using her arsenal of inventions and automated defenses."
    },
    {
        "id": 5,
        "name": "Cypher",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "Morocco",
        "ultimate": "Neural Theft",
        "description": "The Moroccan information broker, Cypher is a one-man surveillance network who keeps tabs on the enemy's every move."
    },
    {
        "id": 6,
        "name": "Sova",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Russia",
        "ultimate": "Hunter's Fury",
        "description": "Born from the eternal winter of Russia's tundra, Sova tracks, finds, and eliminates enemies with ruthless efficiency and precision."
    },
    {
        "id": 7,
        "name": "Sage",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "China",
        "ultimate": "Resurrection",
        "description": "The stronghold of China, Sage assures safety for herself and her team wherever she goes, reviving fallen allies and slowing down enemy pushes."
    },
    {
        "id": 8,
        "name": "Phoenix",
        "Role": "Duelist",
        "year": 2020,
        "origin": "United Kingdom",
        "ultimate": "Run It Back",
        "description": "Hailing from the UK, Phoenix's star power shines through in his fighting style, igniting the battlefield with flash and flare."
    },
    {
        "id": 9,
        "name": "Jett",
        "Role": "Duelist",
        "year": 2020,
        "origin": "South Korea",
        "ultimate": "Blade Storm",
        "description": "Representing South Korea, Jett's agile and evasive fighting style allows her to take risks no one else can, cutting enemies up with lethal precision."
    },
    {
        "id": 10,
        "name": "Reyna",
        "Role": "Duelist",
        "year": 2020,
        "origin": "Mexico",
        "ultimate": "Empress",
        "description": "Forged in the heart of Mexico, Reyna dominates single combat, popping off with each kill she scores."
    },
    {
        "id": 11,
        "name": "Raze",
        "Role": "Duelist",
        "year": 2020,
        "origin": "Brazil",
        "ultimate": "Showstopper",
        "description": "Raze explodes out of Brazil with her big personality and big guns, excelling at clearing tight spaces with high explosives."
    },
    {
        "id": 12,
        "name": "Breach",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Sweden",
        "ultimate": "Rolling Thunder",
        "description": "The bionic Swede, Breach fires powerful, targeted kinetic blasts to aggressively clear a path through enemy territory."
    },
    {
        "id": 13,
        "name": "Skye",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Australia",
        "ultimate": "Seekers",
        "description": "Hailing from Australia, Skye and her band of beasts jam-pack utility into enemy line of sight while healing her allies."
    },
    {
        "id": 14,
        "name": "Yoru",
        "Role": "Duelist",
        "year": 2021,
        "origin": "Japan",
        "ultimate": "Dimensional Drift",
        "description": "Japanese native Yoru rips through reality to infiltrate enemy lines unseen, employing deception and aggression."
    },
    {
        "id": 15,
        "name": "Astra",
        "Role": "Controller",
        "year": 2021,
        "origin": "Ghana",
        "ultimate": "Cosmic Divide",
        "description": "Ghanaian Agent Astra harnesses the energies of the cosmos to reshape battlefields according to her strategic vision."
    },
    {
        "id": 16,
        "name": "KAY/O",
        "Role": "Initiator",
        "year": 2021,
        "origin": "Alternate Timeline",
        "ultimate": "NULL/cmd",
        "description": "KAY/O is a machine of war built for one purpose: neutralizing radiants using suppression technology."
    },
    {
        "id": 17,
        "name": "Chamber",
        "Role": "Sentinel",
        "year": 2021,
        "origin": "France",
        "ultimate": "Tour De Force",
        "description": "Well-dressed and well-armed, French weapons designer Chamber leverages custom marksmanship weaponry to hold lines."
    },
    {
        "id": 18,
        "name": "Neon",
        "Role": "Duelist",
        "year": 2022,
        "origin": "Philippines",
        "ultimate": "Overdrive",
        "description": "Filipino Agent Neon surges forward at shocking speeds, discharging bursts of bioelectric radiance."
    },
    {
        "id": 19,
        "name": "Fade",
        "Role": "Initiator",
        "year": 2022,
        "origin": "Turkey",
        "ultimate": "Nightfall",
        "description": "Turkish bounty hunter Fade unleashes the power of raw nightmare to seize enemy secrets and track targets."
    },
    {
        "id": 20,
        "name": "Harbor",
        "Role": "Controller",
        "year": 2022,
        "origin": "India",
        "ultimate": "Reckoning",
        "description": "Hailing from India’s coast, Harbor commands ancient technology with power over water to shield allies and crush foes."
    },
    {
        "id": 21,
        "name": "Gekko",
        "Role": "Initiator",
        "year": 2023,
        "origin": "United States",
        "ultimate": "Thrash",
        "description": "Gekko the Angeleno leads a tight-knit crew of calamitous creatures that bound forward to scatter enemies."
    },
    {
        "id": 22,
        "name": "Deadlock",
        "Role": "Sentinel",
        "year": 2023,
        "origin": "Norway",
        "ultimate": "Annihilation",
        "description": "Norwegian operative Deadlock deploys high-tech nanowire arrays to secure the battlefield from lethal assaults."
    },
    {
        "id": 23,
        "name": "Iso",
        "Role": "Duelist",
        "year": 2023,
        "origin": "China",
        "ultimate": "Kill Contract",
        "description": "Chinese fixer Iso enters a flow state to reconfigure ambient energy into bulletproof armor and drag enemies into 1v1 duels."
    },
    {
        "id": 24,
        "name": "Clove",
        "Role": "Controller",
        "year": 2024,
        "origin": "Scotland",
        "ultimate": "Not Dead Yet",
        "description": "Scottish troublemaker Clove keeps enemies guessing even in death, controlling the site from beyond the grave."
    },
    {
        "id": 25,
        "name": "Vyse",
        "Role": "Sentinel",
        "year": 2024,
        "origin": "Unknown",
        "ultimate": "Steel Garden",
        "description": "The metallic mastermind Vyse isolates targets with liquid metal traps and disarms enemy primary weapons."
    },
    {
        "id": 26,
        "name": "Tejo",
        "Role": "Initiator",
        "year": 2025,
        "origin": "Colombia",
        "ultimate": "Armageddon",
        "description": "A veteran intelligence consultant from Colombia whose ballistic guidance systems force enemies off key choke points."
    }
]

# HOME
@app.get("/")
def home():
    return {
        "message": "Welcome to the Valorant Agents API!",
        "endpoints": [
            "/api/agents",
            "/api/agents/{agent_id}",
            "/api/agents/search"
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
def search_agents(q: str = Query(..., min_length=1)):
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
