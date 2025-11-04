# Symmetrische Encryptie Applicatie  

**Auteur:** Laura van Zee  
**Vak:** Security & Cyberwarfare  
**Datum:** 4 november 2025  

---

## Inleiding
Deze applicatie laat zien hoe symmetrische encryptie in de praktijk werkt.  
Het doel is om op een veilige en begrijpelijke manier tekst te versleutelen en ontsleutelen met een betrouwbare cryptografische library.  

De implementatie gebruikt **AES-256-GCM**, een moderne en veilige standaard die zowel vertrouwelijkheid als integriteit garandeert.  

---

## Functionaliteit
De applicatie is een **command-line tool** met de volgende commands:

|  Command  | Functie |
|-----------|---------|
| `gen-key` | Genereert een nieuwe 256-bit sleutel |
| `encrypt` | Versleutelt tekst met AES-256-GCM |
| `decrypt` | Ontsleutelt eerder versleutelde tekst |
| `save-key <pad>` | Slaat de sleutel versleuteld op met een wachtwoord |
| `load-key <pad>` | Laadt een opgeslagen sleutel na wachtwoordverificatie |
| `demo` | Laat automatisch een voorbeeld zien van key-gen, encryptie en decryptie |

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
```

2. **Installeer requirements** 

pip install -r requirements.txt

3. **Run de demo (alles automatisch)**

python main.py demo

4. **Bekijk andere commands**

python main.py -h


## Toelichting encryptiemethode

De applicatie maakt gebruik van AES-256 in Galois/Counter Mode (GCM) via de cryptography library.
Reden voor keuze:

    AES-256 biedt een enorme sleutelruimte (2²⁵⁶ mogelijke sleutels).
    GCM voegt authenticatie toe, waardoor manipulatie van ciphertext kan worden gedetecteerd.
    Efficiënt en ondersteund door hardwareversnelling op moderne CPU’s.

## Sleutelbeheer

    Generatie: willekeurig via os.urandom(32)

    Opslag: optioneel versleuteld met PBKDF2-HMAC-SHA256 en JSON

    Uitwisseling: lokaal, voor netwerkgebruik kan RSA-OAEP of KMS worden gebruikt

De beveiliging hangt volledig af van geheimhouding van de sleutel.

## Beveiligingsimplicaties

Deze applicatie demonstreert veilige encryptie op kleine schaal.
Voor professioneel gebruik zouden extra maatregelen nodig zijn:

    Automatische sleutelrotatie
    Beveiligde opslag met HSM’s (Hardware Security Modules)
    Audit logs en toegangsbeheer

## Kerckhoffs’s Principe
Volgens Kerckhoffs’s Principe (1883) moet een cryptografisch systeem veilig blijven, zelfs als alles over het systeem bekend is — behalve de sleutel.
Deze applicatie voldoet hieraan:

    De code en algoritmen zijn volledig openbaar
    Veiligheid berust uitsluitend op geheimhouding van de sleutel
    Gebruik van bewezen standaarden zoals AES-GCM en PBKDF2 past binnen dit principe

## Voorbeeld van gebruik
1. **Genereer een sleutel**

python main.py gen-key
# Output: Generated key (hex): 3e8a9b4c...

2. **Versleutel tekst**

python main.py encrypt
Enter key (hex): 3e8a9b4c...
Text to encrypt: hello world
# Output: {"nonce":"xyz","ciphertext":"abc"}

3. **Ontsleutel tekst**

python main.py decrypt
Enter key (hex): 3e8a9b4c...
Paste encrypted JSON: {"nonce":"xyz","ciphertext":"abc"}
# Output: Decrypted: hello world

4. **Snel demo-overzicht**

python main.py demo
# Genereert sleutel, encryptie, decryptie en print alle resultaten automatisch


## Bronnen
Aumasson, J.-P. (2017). Serious Cryptography. No Starch Press.
Malten, E. (2022). Encryptie voor beginners 1: (A)symmetrische encryptie. Zivver.
Kerckhoffs, A. (1883). La Cryptographie Militaire. Journal des Sciences Militaires, 9, 5–38.
Python Software Foundation. (2024). cryptography library documentation. https://cryptography.io

© 2025 Laura van Zee – Hogeschool Rotterdam