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

# COMPLETE AGENT DATA (WITH AGENT NUMBER, CODE NAME, SIGNATURE & ULT POINTS)
agents = [
    {
        "id": 1,
        "agent_number": "01",
        "name": "Brimstone",
        "code_name": "Sarge",
        "Role": "Controller",
        "year": 2020,
        "origin": "United States",
        "skill_1": "Stim Beacon",
        "skill_2": "Incendiary",
        "signature": "Sky Smoke",
        "ultimate": "Orbital Strike",
        "ult_points": 8,
        "description": "Joining from the USA, Brimstone's orbital arsenal ensures his squad always has the advantage."
    },
    {
        "id": 2,
        "agent_number": "02",
        "name": "Viper",
        "code_name": "Panda",
        "Role": "Controller",
        "year": 2020,
        "origin": "United States",
        "skill_1": "Snake Bite",
        "skill_2": "Poison Cloud",
        "signature": "Toxic Screen",
        "ultimate": "Viper's Pit",
        "ult_points": 9,
        "description": "The American chemist Viper deploys an array of poisonous chemical devices to control the battlefield."
    },
    {
        "id": 3,
        "agent_number": "03",
        "name": "Omen",
        "code_name": "Wraith",
        "Role": "Controller",
        "year": 2020,
        "origin": "Unknown",
        "skill_1": "Shrouded Step",
        "skill_2": "Paranoia",
        "signature": "Dark Cover",
        "ultimate": "From The Shadows",
        "ult_points": 7,
        "description": "A phantom of a memory, Omen hunts in the shadows, blinding enemies and teleporting across the map."
    },
    {
        "id": 4,
        "agent_number": "04",
        "name": "Killjoy",
        "code_name": "Playmaker",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "Germany",
        "skill_1": "Nanoswarm",
        "skill_2": "Alarmbot",
        "signature": "Turret",
        "ultimate": "Lockdown",
        "ult_points": 9,
        "description": "The genius of Germany, Killjoy secures the battlefield using her arsenal of inventions."
    },
    {
        "id": 5,
        "agent_number": "05",
        "name": "Cypher",
        "code_name": "Gumshoe",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "Morocco",
        "skill_1": "Trapwire",
        "skill_2": "Cyber Cage",
        "signature": "Spycam",
        "ultimate": "Neural Theft",
        "ult_points": 6,
        "description": "The Moroccan information broker, Cypher is a one-man surveillance network who keeps tabs on enemy movement."
    },
    {
        "id": 6,
        "agent_number": "06",
        "name": "Sova",
        "code_name": "Hunter",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Russia",
        "skill_1": "Owl Drone",
        "skill_2": "Shock Bolt",
        "signature": "Recon Bolt",
        "ultimate": "Hunter's Fury",
        "ult_points": 8,
        "description": "Born from Russia's tundra, Sova tracks, finds, and eliminates enemies with ruthless efficiency."
    },
    {
        "id": 7,
        "agent_number": "07",
        "name": "Sage",
        "code_name": "Thorne",
        "Role": "Sentinel",
        "year": 2020,
        "origin": "China",
        "skill_1": "Barrier Orb",
        "skill_2": "Slow Orb",
        "signature": "Healing Orb",
        "ultimate": "Resurrection",
        "ult_points": 8,
        "description": "The stronghold of China, Sage assures safety for her team, reviving fallen allies and slowing pushes."
    },
    {
        "id": 8,
        "agent_number": "08",
        "name": "Phoenix",
        "code_name": "Firebird",
        "Role": "Duelist",
        "year": 2020,
        "origin": "United Kingdom",
        "skill_1": "Blaze",
        "skill_2": "Curveball",
        "signature": "Hot Hands",
        "ultimate": "Run It Back",
        "ult_points": 6,
        "description": "Hailing from the UK, Phoenix's star power ignites the battlefield with flash and flare."
    },
    {
        "id": 9,
        "agent_number": "09",
        "name": "Jett",
        "code_name": "Wushu",
        "Role": "Duelist",
        "year": 2020,
        "origin": "South Korea",
        "skill_1": "Cloudburst",
        "skill_2": "Updraft",
        "signature": "Tailwind",
        "ultimate": "Blade Storm",
        "ult_points": 8,
        "description": "Representing South Korea, Jett's agile fighting style allows her to take risks no one else can."
    },
    {
        "id": 10,
        "agent_number": "11",
        "name": "Reyna",
        "code_name": "Vampire",
        "Role": "Duelist",
        "year": 2020,
        "origin": "Mexico",
        "skill_1": "Leer",
        "skill_2": "Devour",
        "signature": "Dismiss",
        "ultimate": "Empress",
        "ult_points": 8,
        "description": "Forged in Mexico, Reyna dominates single combat, popping off with each kill she scores."
    },
    {
        "id": 11,
        "agent_number": "12",
        "name": "Raze",
        "code_name": "Clay",
        "Role": "Duelist",
        "year": 2020,
        "origin": "Brazil",
        "skill_1": "Boom Bot",
        "skill_2": "Blast Pack",
        "signature": "Paint Shells",
        "ultimate": "Showstopper",
        "ult_points": 8,
        "description": "Raze explodes out of Brazil with her big personality, excelling at clearing tight spaces with explosives."
    },
    {
        "id": 12,
        "agent_number": "13",
        "name": "Breach",
        "code_name": "Breaker",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Sweden",
        "skill_1": "Aftershock",
        "skill_2": "Flashpoint",
        "signature": "Fault Line",
        "ultimate": "Rolling Thunder",
        "ult_points": 9,
        "description": "The bionic Swede, Breach fires powerful kinetic blasts to aggressively clear a path through enemy territory."
    },
    {
        "id": 13,
        "agent_number": "14",
        "name": "Skye",
        "code_name": "Guide",
        "Role": "Initiator",
        "year": 2020,
        "origin": "Australia",
        "skill_1": "Regrowth",
        "skill_2": "Trailblazer",
        "signature": "Guiding Light",
        "ultimate": "Seekers",
        "ult_points": 8,
        "description": "Hailing from Australia, Skye and her beasts jam-pack utility into enemy line of sight while healing her allies."
    },
    {
        "id": 14,
        "agent_number": "15",
        "name": "Yoru",
        "code_name": "Stealth",
        "Role": "Duelist",
        "year": 2021,
        "origin": "Japan",
        "skill_1": "Fakeout",
        "skill_2": "Blindside",
        "signature": "Gatecrash",
        "ultimate": "Dimensional Drift",
        "ult_points": 7,
        "description": "Japanese native Yoru rips through reality to infiltrate enemy lines unseen."
    },
    {
        "id": 15,
        "agent_number": "16",
        "name": "Astra",
        "code_name": "Rift",
        "Role": "Controller",
        "year": 2021,
        "origin": "Ghana",
        "skill_1": "Gravity Well",
        "skill_2": "Nova Pulse",
        "signature": "Nebula / Dissipate",
        "ultimate": "Cosmic Divide",
        "ult_points": 7,
        "description": "Ghanaian Agent Astra harnesses the energies of the cosmos to reshape battlefields according to her vision."
    },
    {
        "id": 16,
        "agent_number": "17",
        "name": "KAY/O",
        "code_name": "Grenadier",
        "Role": "Initiator",
        "year": 2021,
        "origin": "Alternate Timeline",
        "skill_1": "FRAG/ment",
        "skill_2": "FLASH/drive",
        "signature": "ZERO/point",
        "ultimate": "NULL/cmd",
        "ult_points": 8,
        "description": "KAY/O is a machine of war built for one purpose: neutralizing radiants using suppression technology."
    },
    {
        "id": 17,
        "agent_number": "18",
        "name": "Chamber",
        "code_name": "Deadeye",
        "Role": "Sentinel",
        "year": 2021,
        "origin": "France",
        "skill_1": "Trademark",
        "skill_2": "Headhunter",
        "signature": "Rendezvous",
        "ultimate": "Tour De Force",
        "ult_points": 8,
        "description": "French weapons designer Chamber leverages custom marksmanship weaponry to hold lines with precision."
    },
    {
        "id": 18,
        "agent_number": "19",
        "name": "Neon",
        "code_name": "Sprinter",
        "Role": "Duelist",
        "year": 2022,
        "origin": "Philippines",
        "skill_1": "Fast Lane",
        "skill_2": "Relay Bolt",
        "signature": "High Gear",
        "ultimate": "Overdrive",
        "ult_points": 8,
        "description": "Filipino Agent Neon surges forward at shocking speeds, discharging bursts of bioelectric radiance."
    },
    {
        "id": 19,
        "agent_number": "20",
        "name": "Fade",
        "code_name": "BountyHunter",
        "Role": "Initiator",
        "year": 2022,
        "origin": "Turkey",
        "skill_1": "Prowler",
        "skill_2": "Seize",
        "signature": "Haunt",
        "ultimate": "Nightfall",
        "ult_points": 8,
        "description": "Turkish bounty hunter Fade unleashes raw nightmare power to seize enemy secrets and track targets."
    },
    {
        "id": 20,
        "agent_number": "21",
        "name": "Harbor",
        "code_name": "Mage",
        "Role": "Controller",
        "year": 2022,
        "origin": "India",
        "skill_1": "Cascade",
        "skill_2": "Cove",
        "signature": "High Tide",
        "ultimate": "Reckoning",
        "ult_points": 7,
        "description": "Hailing from India, Harbor commands ancient water technology to shield allies and crush foes."
    },
    {
        "id": 21,
        "agent_number": "22",
        "name": "Gekko",
        "code_name": "Grotto",
        "Role": "Initiator",
        "year": 2023,
        "origin": "United States",
        "skill_1": "Mosh Pit",
        "skill_2": "Wingman",
        "signature": "Dizzy",
        "ultimate": "Thrash",
        "ult_points": 8,
        "description": "Gekko the Angeleno leads a crew of calamitous creatures that bound forward to scatter enemies."
    },
    {
        "id": 22,
        "agent_number": "23",
        "name": "Deadlock",
        "code_name": "Cable",
        "Role": "Sentinel",
        "year": 2023,
        "origin": "Norway",
        "skill_1": "GravNet",
        "skill_2": "Sonic Sensor",
        "signature": "Barrier Mesh",
        "ultimate": "Annihilation",
        "ult_points": 8,
        "description": "Norwegian operative Deadlock deploys high-tech nanowire arrays to secure the battlefield from lethal assaults."
    },
    {
        "id": 23,
        "agent_number": "24",
        "name": "Iso",
        "code_name": "Serape",
        "Role": "Duelist",
        "year": 2023,
        "origin": "China",
        "skill_1": "Contingency",
        "skill_2": "Undercut",
        "signature": "Double Tap",
        "ultimate": "Kill Contract",
        "ult_points": 8,
        "description": "Chinese fixer Iso reconfigures ambient energy into bulletproof armor and drags enemies into 1v1 duels."
    },
    {
        "id": 24,
        "agent_number": "25",
        "name": "Clove",
        "code_name": "Frog",
        "Role": "Controller",
        "year": 2024,
        "origin": "Scotland",
        "skill_1": "Pick-Me-Up",
        "skill_2": "Meddle",
        "signature": "Ruse",
        "ultimate": "Not Dead Yet",
        "ult_points": 8,
        "description": "Scottish troublemaker Clove keeps enemies guessing even in death, controlling the site from beyond the grave."
    },
    {
        "id": 25,
        "agent_number": "26",
        "name": "Vyse",
        "code_name": "Metal",
        "Role": "Sentinel",
        "year": 2024,
        "origin": "Unknown",
        "skill_1": "Razorvine",
        "skill_2": "Shear",
        "signature": "Arc Rose",
        "ultimate": "Steel Garden",
        "ult_points": 8,
        "description": "The metallic mastermind Vyse isolates targets with liquid metal traps and disarms enemy primary weapons."
    },
    {
        "id": 26,
        "agent_number": "27",
        "name": "Tejo",
        "code_name": "Ballistic",
        "Role": "Initiator",
        "year": 2025,
        "origin": "Colombia",
        "skill_1": "Stealth Drone",
        "skill_2": "Special Delivery",
        "signature": "Guided Salvo",
        "ultimate": "Armageddon",
        "ult_points": 8,
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
            f"{agent['agent_number']} "
            f"{agent['name']} "
            f"{agent['code_name']} "
            f"{agent['Role']} "
            f"{agent['year']} "
            f"{agent['origin']} "
            f"{agent['skill_1']} "
            f"{agent['skill_2']} "
            f"{agent['signature']} "
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
