<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dead by Daylight Character Directory</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>🩸 Dead by Daylight Directory</h1>
        <p>A website powered by a REST API</p>
    </header>
    <main>
        <!-- SEARCH & FILTER SECTION -->
        <section class="search">
            <div class="search-controls">
                <input type="text" id="searchInput" placeholder="Search survivors, killers, powers, perks...">
                <button onclick="searchCharacters(0)"> Search </button>
                <button class="secondary" onclick="loadCharacters(0, '')"> Show All </button>
            </div>
            
            <!-- ROLE FILTERS -->
            <div class="role-filters">
                <button class="filter-btn" onclick="loadCharacters(0, 'Survivor')"> Survivors </button>
                <button class="filter-btn" onclick="loadCharacters(0, 'Killer')"> Killers </button>
            </div>
        </section>

        <!-- CHARACTERS GRID SECTION -->
        <section>
            <h2>Survivors & Killers</h2>
            <div id="characterList" class="agent-list">
                Loading characters...
            </div>

            <!-- PAGINATION CONTROLS -->
            <div id="paginationContainer" class="pagination"></div>
        </section>
    </main>

    <!-- CHARACTER DETAILS MODAL -->
    <div id="characterModal" class="modal">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal()">&times;</span>
            <div id="modalBody"></div>
        </div>
    </div>

    <footer>
        <p>Data provided by the Dead by Daylight Character API</p>
    </footer>
    <script src="app.js"></script>
</body>
</html>
