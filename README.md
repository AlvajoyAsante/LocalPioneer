# Local Pioneer
A community volunteering web application

## About the Project
This submission is for the HackNC 2024 project. Local Pioneer is a social application designed to connect members of a community and promote involvement in community service and addressing shared issues. In many cases, our cities and towns are too vast and fragmented to effectively advocate for service or tackle problems together. This platform will allow users to develop genuine connections with others in their specific communities of interest, as well as discover opportunities to enhance their skills through volunteer work and participate in events dedicated to improving their communities.

## Local Pioneer Installation Instructions

### 1. Have python and pip installed on your command line

### 2. Run "pip install -r requirements.txt" in the repository
If you already have all of the requirements installed, this is optional.

### 3. Run "python run.py" in the repository or equivalent for your machine

### 4. Go to the local host provided by Flask in the console on a web browser

## Table of Contents
- [TechStack](#techstack)
- [Usage](#usage)
- [Credits](#credits)
- [Contributors](#contributors)
- [License](#license)

## TechStack
### Front End
- ${\textsf{\color{green}Bootstrap}}$
- ${\textsf{\color{green}HTML}}$
- ${\textsf{\color{green}CSS}}$
### Back End
- ${\textsf{\color{orange}Flask}}$
- ${\textsf{\color{orange}SQL Alchemy}}$

## Usage
This is a prototype of a web application. It will be deployed temporarily as a demo for the HackNC presentation. At most you can review our code for inspiration or to have a technical understanding of our project.

## Credits
### API Usage
#### Leaflet
Leaflet's map API was utilized in the making of this project and would be used to complete the following.
- **Map Initialization:** The map, centered on the US, is created with L.map, using OpenStreetMap tiles for interactive visuals.
- **Event Radius and Type Filters:** Users select a search radius (10–100 miles). L.circle draws a radius on the map, showing event boundaries. Checkboxes allow filtering by event type. Only relevant events within the radius are shown.
- **Marker Display:** Event markers appear on the map. "Display All Pins" shows all events, bypassing the radius filter.

#### Nominatim
Nominatim's API was used to fetch the coordinates for each address.
- **User Address:** Fetches address in address bar and transposes the map location to that address' coordinates.
- **Address Search and Geocoding:** Users enter an address, which is geocoded via the Nominatim API. The map centers on the location when "Search" is clicked.

### AI Usage
Generative AI was used in the code base of the project, typically to expedite the learning and development process of the applications. The use of AI - ChatGPT was used in creating HTML templates for developers to then adjust and implement, and AI generated art from Pixlr for the logo of our project. AI would be used to help improve manually written material as well.

AI Used - ChatGPT 4o, Blackbox, Claude 3.5 Sonnet

AI-Assisted Content:  
logo.png - Image generation  
map.html - JavaScript and some CSS  
routes.py -  API Routes in Python  
'__init__'.py - Placeholder Data in Python  



## Contributors
### Alvajoy Asante
**Computer Science Student** at University of North Carolina at Charlotte | Class of 2026<br>
Contacts: aasante@charlotte.edu | github.com/AlvajoyAsante

### Ayemhenre Isikhuemhen
**Computer Science Student** at University of North Carolina at Charlotte | Class of 2026<br>
Contacts: aisikhue@charlotte.edu | github.com/Taotlema

### Connor Floyd
**Computer Science Student** at University of South Carolina at Beaufort | Class of 2027<br>
Contacts: connorwfloyd@gmail.com | github.com/xenoyle

### Eisa Chaudhary
**Computer Science Student** at University of South Carolina at Beaufort | Class of 2025<br>
Contacts: EISA@email.uscb.edu | github.com/Eisa2003

## License
CC0-1.0, CC-BY-4.0, and CC-BY-SA-4.0 are open licenses used for non-software material ranging from datasets to videos. Note that Creative Commons does not recommend its licenses be used for software or hardware.
