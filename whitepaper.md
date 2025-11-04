### Introductie			
				
In het kader van het vak Security & Cyberwarfare doe ik onderzoek naar moderne vormen van encryptie. Digitale beveiliging speelt een steeds grotere rol in zowel persoonlijke als professionele omgevingen, en encryptie vormt daarin een belangrijk middel om gegevens te beschermen tegen ongeautoriseerde toegang.
Deze whitepaper beschrijft de theoretische achtergrond van encryptie en de toepassing ervan in een zelf ontwikkelde applicatie. Het doel is om inzicht te krijgen in hoe encryptie werkt, welke methoden veilig zijn en hoe deze in de praktijk kunnen worden geïmplementeerd.			
		
		
### Inleiding	
				
In deze whitepaper presenteer ik mijn onderzoek naar zowel symmetrische als asymmetrische encryptie. Daarbij besteed ik specifieke aandacht aan fundamentele cryptografieprincipes, waaronder het Kerckhoffs’s principe.

Het doel van dit onderzoek is om beter te begrijpen hoe moderne encryptietechnieken bijdragen aan databeveiliging en hoe deze in een praktische toepassing kunnen worden ingezet. De focus ligt op symmetrische encryptie, omdat dit type algoritme efficiënt en geschikt is voor situaties waarin snelheid en eenvoud belangrijk zijn.

De opzet van dit project bestaat uit twee delen: een onderzoeksdeel en een implementatiedeel. In het onderzoeksdeel wordt theoretische kennis verzameld over encryptie, sleutelbeheer en Kerckhoffs’s principe. Deze kennis vormt de basis voor het ontwikkelen van een applicatie waarmee gebruikers tekst kunnen versleutelen en ontsleutelen met behulp van een bestaande, goed geteste cryptografische library (cryptography in Python).

In deze whitepaper wordt eerst de theoretische achtergrond van encryptie besproken, gevolgd door een toelichting op de gekozen encryptiemethode en de implementatie van de applicatie. Tot slot wordt gereflecteerd op de beveiliging en de toepassing van Kerckhoffs’s principe binnen het ontwikkelde systeem.
 

### Theoretisch kader

Wat is encryptie?

Encryptie is een belangrijk onderdeel van cryptografie en zorgt ervoor dat gegevens onleesbaar worden gemaakt voor iedereen die niet over de juiste sleutel beschikt. Het proces gebruikt een algoritme, ook wel cipher genoemd, en een geheime sleutel. Alleen met deze sleutel kan de oorspronkelijke informatie weer worden hersteld; zonder de sleutel is het vrijwel onmogelijk om iets uit de versleutelde data te achterhalen. (Aumasson, November 2017)

Er bestaan verschillende vormen van encryptie, waarvan de meest gebruikte symmetrische encryptie is. Hierbij gebruiken de verzender en de ontvanger dezelfde sleutel om gegevens te versleutelen en weer te ontsleutelen. De sleutel moet vooraf worden uitgewisseld en veilig worden bewaard. Een belangrijk aandachtspunt is dat als iemand anders toegang krijgt tot deze sleutel, de beveiliging volledig wordt doorbroken. (Malten, 2022) Symmetrische encryptie wordt vaak gebruikt in toepassingen waarbij een gebruiker zelf de sleutel beheert, bijvoorbeeld bij versleutelde back-ups in de cloud.
Een andere belangrijke vorm is asymmetrische encryptie. Hierbij wordt gebruikgemaakt van een sleutel paar: een publieke en een privésleutel. De verzender versleutelt de gegevens met de publieke sleutel van de ontvanger, die vervolgens alleen kan ontsleutelen met zijn of haar privésleutel. Hierdoor hoeft de sleutel niet vooraf gedeeld te worden, wat het sleutelbeheer vereenvoudigt. (Malten, 2022) Voor tweerichtingscommunicatie zijn echter twee sleutelparen nodig, één voor elke deelnemer. Een concreet voorbeeld is dat Laura een bericht aan Diederik verstuurt: zij gebruikt Diederiks publieke sleutel om het bericht te versleutelen, en Diederik kan het met zijn privésleutel weer lezen.


Symmetrische encryptie

Symmetrische encryptie is de meest gebruikte vorm van encryptie en vormt de basis van veel praktische toepassingen. Bij deze methode gebruiken zowel de verzender als de ontvanger dezelfde sleutel om gegevens te versleutelen en weer te ontsleutelen. De sleutel moet vooraf veilig worden gedeeld en geheim worden gehouden; wie de sleutel in handen krijgt, kan immers alle versleutelde informatie lezen. (Malten, 2022)
Een belangrijk voordeel van symmetrische encryptie is de snelheid en efficiëntie: het algoritme kan grote hoeveelheden data relatief snel verwerken. Een nadeel is echter het sleutelbeheer: naarmate het aantal gebruikers of communicatiepartners toeneemt, wordt het steeds moeilijker om sleutels veilig uit te wisselen en op te slaan. Daarom worden vaak extra technieken toegepast, zoals het genereren van willekeurige sleutels, het gebruik van salts, of het afleiden van de sleutel uit een wachtwoord via een key derivation function (KDF). (Aumasson, November 2017)
Symmetrische encryptie wordt bijvoorbeeld gebruikt bij versleutelde opslag van bestanden, back-ups in de cloud en beveiligde communicatiekanalen waarbij de sleutel veilig kan worden beheerd door de deelnemende partijen. Veelgebruikte algoritmes zijn AES (Advanced Encryption Standard) en ChaCha20, die bekendstaan om hun veiligheid en efficiëntie. (Aumasson, November 2017)

Asymmetrische encryptie

Asymmetrische encryptie, ook wel public-key encryptie genoemd, werkt met een paar van sleutels: een publieke sleutel en een privésleutel. In tegenstelling tot symmetrische encryptie gebruiken de verzender en ontvanger niet dezelfde sleutel. De verzender versleutelt de gegevens met de publieke sleutel van de ontvanger, en alleen de bijbehorende privésleutel kan de informatie weer ontsleutelen. Hierdoor hoeven de sleutels vooraf niet veilig te worden uitgewisseld, wat het beheer van sleutels aanzienlijk vereenvoudigt. (Malten, 2022)

Voor tweerichtingscommunicatie zijn echter twee sleutelparen nodig, één voor elke deelnemer. Een veelgebruikt voorbeeld is dat Laura een bericht aan Diederik wil sturen. Laura gebruikt Diederiks publieke sleutel om het bericht te versleutelen. Wanneer Diederik het bericht ontvangt, kan hij het ontsleutelen met zijn privésleutel en het bericht lezen. Omdat de privésleutel geheim blijft, kan niemand anders de boodschap decoderen, zelfs niet als de publieke sleutel bekend is. (Malten, 2022)

Asymmetrische encryptie wordt vaak gebruikt voor het uitwisselen van sleutels bij beveiligde communicatie, digitale handtekeningen en het opzetten van versleutelde verbindingen via protocollen zoals TLS/SSL. Bekende algoritmes zijn RSA en elliptic curve cryptography (ECC), die beide bekendstaan om hun veiligheid bij correcte implementatie. (Aumasson, November 2017)
 

### Implementatie van de applicatie


Om de theorie in de praktijk te brengen heb ik een eenvoudige Python-applicatie gemaakt die tekst kan versleutelen en ontsleutelen met symmetrische encryptie. Hiervoor gebruik ik de cryptography library, een moderne en veelgebruikte Python library voor veilige cryptografie.
De applicatie maakt gebruik van AES-256-GCM (Advanced Encryption Standard, 256-bit key, Galois/Counter Mode).
Ik heb voor dit algoritme gekozen omdat AES wereldwijd de standaard is binnen de industrie en GCM niet alleen vertrouwelijkheid, maar ook integriteitscontrole biedt. Dat betekent dat de applicatie niet alleen de inhoud van het bericht beschermt, maar ook voorkomt dat iemand ongemerkt iets aan de versleutelde data verandert.
De werking van de applicatie is eenvoudig.
Eerst wordt een willekeurige sleutel aangemaakt met os.urandom(). Vervolgens voert de gebruiker een bericht in dat met AES-GCM wordt versleuteld. De uitvoer bestaat uit de ciphertext en een nonce (een unieke waarde die voor elke encryptie nieuw wordt gegenereerd).
Met dezelfde sleutel en nonce kan de oorspronkelijke tekst weer worden hersteld.
Deze opzet laat goed zien hoe moderne symmetrische encryptie werkt. De veiligheid hangt volledig af van de sleutel en niet van de broncode of het algoritme zelf.
 

### Sleutelbeheer

Sleutelbeheer is een belangrijk onderdeel van cryptografie. In mijn applicatie heb ik dit op een eenvoudige maar veilige manier uitgewerkt.


Generatie:

De sleutel wordt aangemaakt met os.urandom(32). Dit levert een willekeurige sleutel van 256 bits, wat voldoende is voor AES-256. Omdat de sleutel cryptografisch willekeurig wordt gegenereerd, is deze niet te raden of te voorspellen.


Opslag:

Voor korte sessies blijft de sleutel alleen in het geheugen aanwezig. Wanneer de sleutel langer moet worden bewaard, kan deze lokaal worden opgeslagen in een versleuteld bestand. Daarvoor gebruik ik een key derivation function (PBKDF2-HMAC-SHA256) die uit een wachtwoord een afgeleide sleutel maakt. Die afgeleide sleutel wordt vervolgens gebruikt om de originele sleutel te versleutelen, zodat deze nooit in platte tekst op schijf staat.


Uitwisseling:

Als de sleutel moet worden gedeeld met een andere gebruiker kan dat veilig door middel van RSA-OAEP. Daarbij wordt de symmetrische sleutel ingepakt met de publieke sleutel van de ontvanger. Alleen de ontvanger met de juiste private key kan de sleutel dan weer ontcijferen.


Beveiligingsimplicaties:

Deze aanpak is voldoende voor een kleine demo of persoonlijke toepassing, maar in een professionele omgeving is sleutelbeheer veel complexer. Bij grote aantallen gebruikers wordt het handmatig beheren en delen van sleutels onpraktisch. In dat geval is een Key Management System (KMS) of Hardware Security Module (HSM) nodig. Sleutels moeten bovendien regelmatig worden vernieuwd en mogen nooit in logbestanden of versiebeheer terechtkomen.


### Reflectie op Kerckhoffs’s principe

De opzet van deze applicatie sluit goed aan bij Kerckhoffs’s principe. Dit principe stelt dat een cryptografisch systeem veilig moet blijven, zelfs als alle details van het systeem openbaar zijn, zolang de sleutel geheim blijft (Kerckhoffs, 1883).
De algoritmen die ik gebruik, zoals AES-GCM, RSA-OAEP en PBKDF2-HMAC-SHA256, zijn allemaal publieke standaarden. Hun werking is volledig bekend en uitgebreid getest door de internationale cryptografiegemeenschap. De veiligheid van mijn applicatie hangt dus alleen af van de bescherming van de sleutel.
Als iemand de sleutel weet te bemachtigen, is de beveiliging meteen verbroken, maar zonder de sleutel is het praktisch onmogelijk om iets te ontsleutelen. Dat laat goed zien waarom Kerckhoffs’s principe nog steeds relevant is. Veiligheid berust niet op geheimhouding van de methode, maar op de correcte toepassing van open, betrouwbare standaarden.


### Conclusie

Tijdens dit project heb ik geleerd hoe de theorie van cryptografie kan worden toegepast in een echte implementatie. Ik begrijp nu beter hoe symmetrische en asymmetrische encryptie samenwerken en waarom sleutelbeheer zo belangrijk is. De implementatie met AES-256-GCM laat zien dat veilige encryptie goed te realiseren is met bestaande libraries, zolang er zorgvuldig met sleutels wordt omgegaan.
Kerckhoffs’s principe heeft me laten zien dat echte veiligheid niet draait om geheimhouding van de technologie, maar om transparantie en correct gebruik van bewezen technieken. Dat maakt moderne cryptografie niet alleen krachtig, maar ook betrouwbaar.
 

### Literatuurlijst

Aumasson, J.-P. (2017). Serious cryptography: A practical introduction to modern encryption. No Starch Press.
Kerckhoffs, A. (1883). La cryptographie militaire. Journal des Sciences Militaires, 9, 5–38.
Malten, E. (2022). Encryptie voor beginners 1: (A)symmetrische encryptie. Zivver. https://www.zivver.com/ 
 

