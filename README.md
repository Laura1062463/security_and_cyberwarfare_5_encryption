# Symmetrische Encryptie Applicatie  
**Auteur:** Laura van Zee  
**Vak:** Security & Cyberwarfare  
**Datum:** 4 november 2025  

---

## Inleiding
Deze applicatie is ontwikkeld in het kader van het vak *Security & Cyberwarfare* en laat zien hoe symmetrische encryptie in de praktijk werkt.  
Het doel is om op een veilige en begrijpelijke manier tekst te kunnen versleutelen en ontsleutelen met behulp van een betrouwbare cryptografische library.  

De implementatie gebruikt **AES-256-GCM**, een moderne en veilige standaard die vertrouwelijkheid én integriteit garandeert.  

---

## Functionaliteit
De applicatie is een **command-line tool** met de volgende mogelijkheden:

| Commando | Functie |
|-----------|----------|
| `gen-key` | Genereert een nieuwe 256-bit sleutel |
| `encrypt` | Versleutelt tekst met AES-256-GCM |
| `decrypt` | Ontsleutelt eerder versleutelde tekst |
| `save-key <pad>` | Slaat de sleutel versleuteld op met een wachtwoord |
| `load-key <pad>` | Laadt een opgeslagen sleutel na wachtwoordverificatie |

---

## Bestandsstructuur
encryption_app/
│
├── cipher.py # Klasse voor encryptie en decryptie (AES-256-GCM)
├── key_manager.py # Klasse voor sleutelbeheer
├── main.py # Command-line interface
└── requirements.txt # Benodigde Python libraries


---

## Installatie en gebruik

1. **Maak een virtual environment aan**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Mac/Linux
   .venv\Scripts\activate        # Windows

2. **Installeer requirements**
    pip install -r requirements.txt

3. **Run de applicatie**
    python main.py

4. **Bekijk beschikbare commands**
    python main.py -h

## Toelichting encryptiemethode

De applicatie maakt gebruik van AES-256 in Galois/Counter Mode (GCM) via de cryptography library.
AES is de huidige industriestandaard voor symmetrische encryptie en wordt wereldwijd gebruikt door o.a. overheden, banken en cloudproviders.

Reden voor keuze:

    AES-256 biedt een sleutelruimte van 2²⁵⁶ mogelijke sleutels.

    GCM voegt authenticatie toe, waardoor manipulatie van ciphertext kan worden gedetecteerd.

    De implementatie is efficiënt en wordt ondersteund door hardwareversnelling op de meeste moderne CPU’s.

## Sleutelbeheer

De beveiliging van het systeem hangt volledig af van het beheer van de sleutel.
In deze applicatie wordt dat als volgt aangepakt:

Generatie

De sleutel wordt willekeurig gegenereerd met os.urandom(32), wat cryptografisch veilige random bytes oplevert.

Opslag

Als de gebruiker dat wil, kan de sleutel worden versleuteld opgeslagen:

    Een wachtwoord wordt via PBKDF2-HMAC-SHA256 omgezet in een sleutelafgeleide.

    Daarmee wordt de echte AES-sleutel lokaal versleuteld en opgeslagen in JSON-vorm.

    De sleutel staat dus nooit in platte tekst op schijf.

Uitwisseling

De applicatie is bedoeld voor lokaal gebruik en bevat geen netwerkcomponent.
In een productieomgeving zou de sleuteluitwisseling bijvoorbeeld via asymmetrische encryptie (RSA-OAEP) of een Key Management System (KMS) verlopen.

## Beveiligingsimplicaties

De applicatie demonstreert veilige encryptie op kleine schaal.

Voor professioneel gebruik zouden er extra maatregelen nodig zijn, zoals:

    Automatische sleutelrotatie.

    Beveiligde opslag met HSM’s (Hardware Security Modules).

    Audit logs en toegangsbeheer.

## Kerckhoffs’s Principe

Volgens Kerckhoffs’s Principe (1883) moet een cryptografisch systeem veilig blijven, zelfs als alles over het systeem bekend is — behalve de sleutel.

Deze applicatie voldoet aan dat principe:

    De code en gebruikte algoritmen zijn volledig openbaar.

    De veiligheid berust uitsluitend op de geheimhouding van de sleutel.

    Zolang de sleutel veilig wordt bewaard, kan de data niet worden ontsleuteld.

Het gebruik van bekende en bewezen standaarden zoals AES-GCM en PBKDF2 past perfect binnen deze filosofie.

## Voorbeeld van gebruik

1. Genereer een sleutel

python main.py gen-key
# Output: Generated key (base64): 3e8a9b4c...


2. Encrypted tekst

python main.py encrypt
Enter key (hex): 3e8a9b4c...
Text to encrypt: hello world


3. Decrypted tekst

python main.py decrypt
Enter key (hex): 3e8a9b4c...
Paste encrypted JSON: {"nonce":"xyz","ciphertext":"abc"}
# Output: Decrypted: hello world

## Bronnen

Aumasson, J.-P. (2017). Serious Cryptography. No Starch Press.

Malten, E. (2022). Encryptie voor beginners 1: (A)symmetrische encryptie. Zivver.

Kerckhoffs, A. (1883). La Cryptographie Militaire. Journal des Sciences Militaires, 9, 5–38.

Python Software Foundation. (2024). cryptography library documentation. https://cryptography.io

© 2025 Laura van Zee – Hogeschool Rotterdam