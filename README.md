# NBA Graph App

A Django-based web application that uses Neo4j as a graph database to model and visualize relationships between NBA players, teams, and coaches.

## Features

- Add and manage:
  - Players
  - Teams
  - Coaches
- Create and visualize relationships:
  - `PLAYS_FOR`: Player -> Team
  - `COACHES`: Coach -> Player
  - `COACHES_FOR`: Coach -> Team
  - `TEAMMATES`: Player <-> Player
  - `PLAYED_AGAINST`: Player -> Team (as a rival)
- Simulate graph connections visually (e.g., *Player --- PLAYS_FOR ---> Team*)
- Centralized Home interface to navigate through the app

## Tech Stack

- **Backend**: Django, Python
- **Database**: Neo4j (via `neomodel`)
- **Frontend**: HTML/CSS (Bootstrap optional)

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/nba-graph-app.git
cd nba-graph-app
```

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up Neo4j**

- Install Neo4j Desktop or run Neo4j locally using Docker
- Set the following environment variables (you can also set them in `.env`):

```bash
export NEO4J_BOLT_URL=bolt://localhost:7687
export NEO4J_USERNAME=neo4j
export NEO4J_PASSWORD=your_password
```

5. **Run the Django development server**

```bash
python manage.py runserver
```

6. **Access the app**

Visit `http://localhost:8000` in your browser.

## Folder Structure

```plaintext
neo4j_django/
├── neoapp/               # Django app with models, views, forms, templates
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── nbaapp/
│           ├── home.html
│           ├── player_list.html
│           ├── team_list.html
│           ├── coach_list.html
│           ├── assign_player_to_team.html
│           ├── assign_coach_to_team.html
│           └── assign_coach_to_player.html
├── manage.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Add graph visualization using D3.js or vis.js
- Add authentication system for admin access
- Export/Import player and team data
- Improve UI with advanced styles

---

Made with ❤️ for graph database exploration.

---

**License**: MIT

