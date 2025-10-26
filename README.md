# security_and_cyberwarfare_5_encryption
https://github.com/Laura1062463/security_and_cyberwarfare_5_encryption.git

Instructies
Het doel is om een applicatie (app of webapp) te ontwikkelen waarmee gebruikers eenvoudig tekst kunnen versleutelen en ontsleutelen. De focus ligt hierbij op symmetrische encryptie.

Basisfunctionaliteiten:

• De applicatie moet een eenvoudige gebruikersinterface bieden voor zowel het versleutelen als ontsleutelen van tekst. Dit mag ook een command-line interface zijn.

• Het is verplicht om bestaande, goed geteste cryptografische libraries te gebruiken (bijvoorbeeld `cryptography` in Python of `crypto-js` in JavaScript). Houd hierbij rekening met het principe van "Don't roll your own crypto", aangezien cryptografie ongelooflijk moeilijk is om zelf correct te implementeren.

Stappenplan:

1. Onderzoek: Voer onderzoek uit naar zowel symmetrische als asymmetrische encryptie. Besteed hierbij ook aandacht aan de fundamentele cryptografieprincipes, zoals Kerckhoffs's Principe.

2. Implementatie: Implementeer de encryptie in de applicatie met behulp van een cryptografische library.

    ◦ Kies een specifiek, modern en veilig symmetrisch encryptiealgoritme (bijvoorbeeld AES-128, AES-192 of AES-256).

    ◦ Besteed expliciet aandacht aan sleutelbeheer: Bedenk en implementeer hoe de symmetrische sleutel binnen jouw applicatie wordt gegenereerd, opgeslagen en/of uitgewisseld.

Documentatie (kort verslag): Lever een kort verslag aan waarin u het volgende uitlegt en bediscussieert:

• Hoe de applicatie werkt.

• Welke encryptiemethoden en welk specifiek algoritme (met rechtvaardiging van de keuze) zijn gebruikt.

• Hoe de symmetrische sleutel in de applicatie wordt behandeld (generatie, opslag, uitwisseling) en bespreek de beveiligingsimplicaties van de gekozen methode. Houd in gedachten dat sleutelbeheer bij symmetrische encryptie een complex en nagenoeg onmogelijk vraagstuk kan zijn bij een groot aantal gebruikers.

• **Reflecteer op hoe jouw applicatie en de gekozen encryptiemethode zich verhouden tot Kerckhoffs's Principe** ("een versleutelingssysteem moet veilig zijn, zelfs als alle details van het systeem, behalve de sleutel, publiek bekend zijn").

**Op te leveren:** De resultaten moeten worden ingeleverd via een **GitHub repository** met een bijbehorende **README.md**. De README.md met bijbehorende link naar de Github Repo upload je in brightspace.