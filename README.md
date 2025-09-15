<body>
    <h1>Instrukcja uruchomienia projektu</h1>
    <ol>
        <li>
            <strong>Sklonuj repozytorium</strong><br>
            Pobierz to repozytorium do folderu, w którym masz już repozytorium: 
            <a href="https://github.com/statsbomb/open-data.git" target="_blank">StatsBomb Open Data</a>.
        </li>
        <li>
            <strong>Sprawdź strukturę folderów</strong><br>
            Po sklonowaniu powinieneś mieć w jednym katalogu dwa foldery:
            <ul>
                <li><code>mapper</code></li>
                <li><code>statsbomb-opendata</code></li>
            </ul>
            <div class="note">Punkt 1 i 2 są kluczowe, aby skrypty poprawnie odczytywały dane ze StatsBomb.</div>
        </li>
        <li>
            <strong>Przejdź do folderu projektu</strong><br>
            Otwórz terminal w folderze <code>mapper</code>.<br>
            W VS Code możesz wybrać, którego terminala używasz (np. Git Bash).
        </li>
        <li>
            <strong>Utwórz wirtualne środowisko</strong><br>
            <code>python3 -m venv venv</code><br>
            To utworzy katalog <code>venv/</code> z izolowanym środowiskiem Pythona.
        </li>
        <li>
            <strong>Aktywuj wirtualne środowisko</strong><br>
            <ul>
                <li><strong>Linux / macOS:</strong> <code>source venv/bin/activate</code></li>
                <li><strong>Windows (Git Bash / PowerShell):</strong> <code>source venv/Scripts/activate</code></li>
            </ul>
        </li>
        <li>
            <strong>Zainstaluj wymagane paczki</strong><br>
            <code>pip install -r requirements.txt</code>
        </li>
        <li>
            <strong>Uruchom skrypt</strong><br>
            <code>python3 run.py</code><br>
            <div class="note">Przed uruchomieniem zmień ligę i sezon w liniach 7, 8 i 15 w pliku <code>run.py</code>.</div>
        </li>
        <li>
            <strong>Sprawdź wyniki</strong><br>
            Dane zostaną zapisane w folderze <code>/data/</code> w postaci plików <code>.csv</code> i <code>.json</code>.
        </li>
    </ol>
</body>
</html>
