# GPA calculator
This is a small command line GPA calculator

## Python and requirements
This project is written with Python 3.10.4, but it will probably work with other versions as well.

You will need to run the command 'pip -r requirements.txt' to install all additional libraries into your enviroment

## csv structure

The csv consists of 3 columns:<br/>
```
    Name  --  is the Subjects Name
    Grade  --  must be: 'A', 'B', 'C', 'D', 'E', 'Pass'
    Points  --  is the subjects credit
```
## Commands
```
py .\gpa_calculator.py --help  --  Brings up the help menu in the command line
py .\gpa_calculator.py add  --  Adds a grade to the list 
py .\gpa_calculator.py show  --  Shows current grades in list 
py .\gpa_calculator.py remove  --  Removes the last entry to the list 
py .\gpa_calculator.py calc  --  Calculates your current GPA 
```
---

If you find any mistakes/improvments, create an issue or send me an e-mail [mail](mailto:admin@sivert.me?subject=[GitHub]%13GPA-calculator)

## Git tutorial (in Norwegian)

**Git clone:** Bruk ‘git clone %repo%’ for å klone et git-prosjekt til din lokale datamaskin. Erstatt %repo% med en link til GitHub eller GitLab-mappen. 


**Git checkout:** For å opprette en ny branch; skriv kommandoen ‘git checkout -b "my-branch", der "my-branch" er navnet på den nye branchen.

Dersom en ønsker å bytte branch, kan dette gjøres ved å kjøre kommandoen ‘git checkout "my-branch", der "my-branch" er navnet på den branchen du ønsker å bytte til.

Merk at en bør være i riktig branch før en begynner å gjøre endringer. Dette er ikke et absolutt krav, men gjør prosessen mye enklere. 


**Sende endringer til GitHub/GitLab:** Når du er i ønsket branch og er ferdig med å gjøre endringer, kan du sende dette til GitLab eller GitHub. Følgende kommandoer bør kjøres i riktig rekkefølge, og en bør ikke foreta noen endringer i løpet av denne prosessen:


'git pull' oppdaterer den branchen man er i 


'git add .' legger alle filene med endringer i en pakke som skal sendes til Git 


'git stage .' fryser filene som er lagt i pakken


'git commit -m "my-message"' ferdigstiller pakken. Bytt ut "my-message" med en beskrivende kommentar som forklarer hva som er gjort av endringer


'git push' sender den ferdigstilte pakken til GitHub eller GitLab-serveren


Dersom du ønsker å sende opp en ny branch som enda ikke eksisterer i GitHub eller GitLab-repository, er det nødvendig å kjøre kommandoen 'git push -u origin "my-branch", der "my-branch" er navnet på den branchen du nettopp laget.
