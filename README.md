# Receptář

Webová aplikace pro správu receptů postavená na frameworku Flask a databázi MongoDB.

## Obsah

- [Použité technologie](#použité-technologie)
- [Požadavky](#požadavky)
- [Architektura a závislosti](#architektura-a-závislosti)
- [Nasazení pomocí Docker Compose](#nasazení-pomocí-docker-compose)
- [Nasazení pomocí Ansible](#nasazení-pomocí-ansible)
- [Ověření funkčnosti](#ověření-funkčnosti)
- [Troubleshooting](#troubleshooting)

## Použité technologie

V projektu jsou použity následující technologie:

- **Python (Flask)**: Backend aplikace a webový framework.
- **MongoDB**: NoSQL databáze pro ukládání uživatelů a receptů.
- **Docker & Docker Compose**: Kontejnerizace aplikace a správa vícekontejnerového prostředí.
- **Ansible**: Automatizace nasazení aplikace na cílový server.
- **HTML/CSS/Bootstrap**: Frontend aplikace.

## Požadavky

Před nasazením aplikace je potřeba mít nainstalováno:

- **Docker** a **Docker Compose plugin**
- **Ansible** (pouze v případě automatizovaného nasazení)
- Přístupová práva (root nebo sudo) pro instalaci balíčků a spouštění kontejnerů.
- Síťové požadavky: Otevřený port `5000` pro webovou aplikaci a volitelně `27017` pro přímý přístup k databázi.

## Architektura a závislosti

Aplikace se skládá ze dvou hlavních služeb:
1.  **flask**: Kontejner s Python aplikací. Závisí na službě `mongodb`.
2.  **mongodb**: Databázový kontejner běžící na standardním portu `27017`.

Data v MongoDB jsou chráněna základní autentizací (admin/admin).

## Nasazení pomocí Docker Compose

Tato metoda je vhodná pro lokální vývoj nebo rychlé spuštění.

1.  Klonování repozitáře:
    ```bash
    git clone https://github.com/jelinekjakub/nsql_project.git
    cd nsql_project
    ```

2.  Sestavení a spuštění kontejnerů:
    ```bash
    docker-compose up --build -d
    ```

## Nasazení pomocí Ansible

Tato metoda automatizuje instalaci Dockeru a nasazení celé aplikace na vzdálený (nebo lokální) server.

1.  Upravte soubor `ansible/inventory.ini` a zadejte IP adresu cílového serveru.
2.  Spusťte playbook:
    ```bash
    cd ansible
    ansible-playbook -i inventory.ini deploy.yml
    ```
    *Poznámka: Playbook provede instalaci Dockeru, zkopíruje soubory aplikace do `/opt/flask-app` a spustí `docker compose up`.*

## Ověření funkčnosti

1.  Otevřete prohlížeč na adrese `http://localhost:5000`.
2.  Pro přihlášení použijte testovací údaje:
    - **Email:** `test@test.cz`
    - **Heslo:** `123456789`
3.  Po přihlášení byste měli vidět seznam receptů a mít možnost přidávat nové.

## Troubleshooting

- **Port 5000 je obsazen**: Změňte mapování portů v `docker-compose.yml` (např. na `"8080:5000"`).
- **Chyba připojení k MongoDB**: Ujistěte se, že kontejner `mongodb` běží (`docker ps`). Aplikace se připojuje pomocí názvu služby `mongodb`.
- **Ansible SSH chyba**: Ověřte, že máte nastavený SSH přístup na cílový server a správně vyplněné `inventory.ini`.
- **Problémy s právy**: Pokud Docker vyžaduje sudo, ujistěte se, že uživatel spouštějící Ansible má dostatečná oprávnění (playbook používá `become: true`).
