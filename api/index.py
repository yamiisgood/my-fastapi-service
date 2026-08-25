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

# COMPLETE AGENT DATA (WITH SKILLS 1-3)
agents = [
    {
        "id": 1,
        "name": "Brimstone",
        "Role": "Controller",
        "year": 2020,
        "origin": "United States",
        "skill_1": "Stim Beacon",
        "skill_2": "Incendiary",
        "skill_3": "Sky Smoke",
        "ultimate": "Orbital Strike",
        "description": "Joining from the USA, Brimstone's orbital arsenal ensures his squad always has the advantage."
    },
    {
        "id": 2,
        "name": "Viper",
        "Role": "Controller",
        "year": 2020,
        "origin": "United States",
        "skill_1": "Snake Bite",
        "skill_2": "Poison Cloud",
        "skill_3": "Toxic Screen",
        "ultimate": "Viper's Pit",
        "description": "The American chemist Viper deploys an array of poisonous chemical devices to control the battlefield."
    },
    {
        "id": 3,
        "name": "Omen",
        "Role": "Controller",
        "year": 2020,
        "origin": "Unknown",
        "skill_1": "Shrouded Step",
        "skill_2": "Paranoia",
        "skill_3": "Dark Cover",
        "ultimate": "From The Shadows",
        "description": "A phantom of a memory, Omen hunts in the shadows, blinding enemies and teleporting across the map."
    },
    {
        "id": 4,
        "name": "Killjoy",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "Germany",
        "skill_1": "Nanoswarm",
        "skill_2": "Alarmbot",
        "skill_3": "Turret",
        "ultimate": "Lockdown",
        "description": "The genius of Germany, Killjoy secures the battlefield using her arsenal of inventions."
    },
    {
        "id": 5,
        "name": "Cypher",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "Morocco",
        "skill_1": "Trapwire",
        "skill_2": "Cyber Cage",
        "skill_3": "Spycam",
        "ultimate": "Neural Theft",
        "description": "The Moroccan information broker, Cypher is a one-man surveillance network who keeps tabs on enemy movement."
    },
    {
        "id": 6,
        "name": "Sova",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Russia",
        "skill_1": "Owl Drone",
        "skill_2": "Shock Bolt",
        "skill_3": "Recon Bolt",
        "ultimate": "Hunter's Fury",
        "description": "Born from Russia's tundra, Sova tracks, finds, and eliminates enemies with ruthless efficiency."
    },
    {
        "id": 7,
        "name": "Sage",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "China",
        "skill_1": "Barrier Orb",
        "skill_2": "Slow Orb",
        "skill_3": "Healing Orb",
        "ultimate": "Resurrection",
        "description": "The stronghold of China, Sage assures safety for her team, reviving fallen allies and slowing pushes."
    },
    {
        "id": 8,
        "name": "Phoenix",
        "Role": "Duelist",
        "year": 2020,
        "origin": "United Kingdom",
        "skill_1": "Blaze",
        "skill_2": "Curveball",
        "skill_3": "Hot Hands",
        "ultimate": "Run It Back",
        "description": "Hailing from the UK, Phoenix's star power ignites the battlefield with flash and flare."
    },
    {
        "id": 9,
        "name": "Jett",
        "Role": "Duelist",
        "year": 2020,
        "origin": "South Korea",
        "skill_1": "Cloudburst",
        "skill_2": "Updraft",
        "skill_3": "Tailwind",
        "ultimate": "Blade Storm",
        "description": "Representing South Korea, Jett's agile fighting style allows her to take risks no one else can."
    },
    {
        "id": 10,
        "name": "Reyna",
        "Role": "Duelist",
        "year": 2020,
        "origin": "Mexico",
        "skill_1": "Leer",
        "skill_2": "Devour",
        "skill_3": "Dismiss",
        "ultimate": "Empress",
        "description": "Forged in Mexico, Reyna dominates single combat, popping off with each kill she scores."
    },
    {
        "id": 11,
        "name": "Raze",
        "Role": "Duelist",
        "year": 2020,
        "origin": "Brazil",
        "skill_1": "Boom Bot",
        "skill_2": "Blast Pack",
        "skill_3": "Paint Shells",
        "ultimate": "Showstopper",
        "description": "Raze explodes out of Brazil with her big personality, excelling at clearing tight spaces with explosives."
    },
    {
        "id": 12,
        "name": "Breach",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Sweden",
        "skill_1": "Aftershock",
        "skill_2": "Flashpoint",
        "skill_3": "Fault Line",
        "ultimate": "Rolling Thunder",
        "description": "The bionic Swede, Breach fires powerful kinetic blasts to aggressively clear a path through enemy territory."
    },
    {
        "id": 13,
        "name": "Skye",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Australia",
        "skill_1": "Regrowth",
        "skill_2": "Trailblazer",
        "skill_3": "Guiding Light",
        "ultimate": "Seekers",
        "description": "Hailing from Australia, Skye and her beasts jam-pack utility into enemy line of sight while healing her allies."
    },
    {
        "id": 14,
        "name": "Yoru",
        "Role": "Duelist",
        "year": 2021,
        "origin": "Japan",
        "skill_1": "Fakeout",
        "skill_2": "Blindside",
        "skill_3": "Gatecrash",
        "ultimate": "Dimensional Drift",
        "description": "Japanese native Yoru rips through reality to infiltrate enemy lines unseen."
    },
    {
        "id": 15,
        "name": "Astra",
        "Role": "Controller",
        "year": 2021,
        "origin": "Ghana",
        "skill_1": "Gravity Well",
        "skill_2": "Nova Pulse",
        "skill_3": "Nebula / Dissipate",
        "ultimate": "Cosmic Divide",
        "description": "Ghanaian Agent Astra harnesses the energies of the cosmos to reshape battlefields according to her vision."
    },
    {
        "id": 16,
        "name": "KAY/O",
        "Role": "Initiator",
        "year": 2021,
        "origin": "Alternate Timeline",
        "skill_1": "FRAG/ment",
        "skill_2": "FLASH/drive",
        "skill_3": "ZERO/point",
        "ultimate": "NULL/cmd",
        "description": "KAY/O is a machine of war built for one purpose: neutralizing radiants using suppression technology."
    },
    {
        "id": 17,
        "name": "Chamber",
        "Role": "Sentinel",
        "year": 2021,
        "origin": "France",
        "skill_1": "Trademark",
        "skill_2": "Headhunter",
        "skill_3": "Rendezvous",
        "ultimate": "Tour De Force",
        "description": "French weapons designer Chamber leverages custom marksmanship weaponry to hold lines with precision."
    },
    {
        "id": 18,
        "name": "Neon",
        "Role": "Duelist",
        "year": 2022,
        "origin": "Philippines",
        "skill_1": "Fast Lane",
        "skill_2": "Relay Bolt",
        "skill_3": "High Gear",
        "ultimate": "Overdrive",
        "description": "Filipino Agent Neon surges forward at shocking speeds, discharging bursts of bioelectric radiance."
    },
    {
        "id": 19,
        "name": "Fade",
        "Role": "Initiator",
        "year": 2022,
        "origin": "Turkey",
        "skill_1": "Prowler",
        "skill_2": "Seize",
        "skill_3": "Haunt",
        "ultimate": "Nightfall",
        "description": "Turkish bounty hunter Fade unleashes raw nightmare power to seize enemy secrets and track targets."
    },
    {
        "id": 20,
        "name": "Harbor",
        "Role": "Controller",
        "year": 2022,
        "origin": "India",
        "skill_1": "Cascade",
        "skill_2": "Cove",
        "skill_3": "High Tide",
        "ultimate": "Reckoning",
        "description": "Hailing from India, Harbor commands ancient water technology to shield allies and crush foes."
    },
    {
        "id": 21,
        "name": "Gekko",
        "Role": "Initiator",
        "year": 2023,
        "origin": "United States",
        "skill_1": "Mosh Pit",
        "skill_2": "Wingman",
        "skill_3": "Dizzy",
        "ultimate": "Thrash",
        "description": "Gekko the Angeleno leads a crew of calamitous creatures that bound forward to scatter enemies."
    },
    {
        "id": 22,
        "name": "Deadlock",
        "Role": "Sentinel",
        "year": 2023,
        "origin": "Norway",
        "skill_1": "GravNet",
        "skill_2": "Sonic Sensor",
        "skill_3": "Barrier Mesh",
        "ultimate": "Annihilation",
        "description": "Norwegian operative Deadlock deploys high-tech nanowire arrays to secure the battlefield from lethal assaults."
    },
    {
        "id": 23,
        "name": "Iso",
        "Role": "Duelist",
        "year": 2023,
        "origin": "China",
        "skill_1": "Contingency",
        "skill_2": "Undercut",
        "skill_3": "Double Tap",
        "ultimate": "Kill Contract",
        "description": "Chinese fixer Iso reconfigures ambient energy into bulletproof armor and drags enemies into 1v1 duels."
    },
    {
        "id": 24,
        "name": "Clove",
        "Role": "Controller",
        "year": 2024,
        "origin": "Scotland",
        "skill_1": "Pick-Me-Up",
        "skill_2": "Meddle",
        "skill_3": "Ruse",
        "ultimate": "Not Dead Yet",
        "description": "Scottish troublemaker Clove keeps enemies guessing even in death, controlling the site from beyond the grave."
    },
    {
        "id": 25,
        "name": "Vyse",
        "Role": "Sentinel",
        "year": 2024,
        "origin": "Unknown",
        "skill_1": "Razorvine",
        "skill_2": "Shear",
        "skill_3": "Arc Rose",
        "ultimate": "Steel Garden",
        "description": "The metallic mastermind Vyse isolates targets with liquid metal traps and disarms enemy primary weapons."
    },
    {
        "id": 26,
        "name": "Tejo",
        "Role": "Initiator",
        "year": 2025,
        "origin": "Colombia",
        "skill_1": "Stealth Drone",
        "skill_2": "Special Delivery",
        "skill_3": "Guided Salvo",
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
            f"{agent['skill_1']} "
            f"{agent['skill_2']} "
            f"{agent['skill_3']} "
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
