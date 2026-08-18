# Voting App

A simple Flask API where users cast votes for candidates by visiting a URL,
and view live results as JSON. Built as a two-version project with Git
branching to practice a real development workflow.

## Installation and Setup
1. `git clone https://github.com/arupchakraborty7-dot/voting-app.git`
2. `cd voting-app`
3. `python app.py`
4. Visit `http://localhost:5000`

## API Endpoint Reference
Endpoint	Method	Description	Example Response
`/`	home()	Welcome message	Welcome to the App
`/health`	health()	Health check	App is running
`/vote/<name>`	vote(name)	Casts a vote for `name`	Vote recorded for Alice. Total votes: 1
`/results`	results()	Returns all vote counts	{"Alice": 2, "Bob": 1}
`/reset`	reset()	Clears all votes	All votes have been reset

## Git Workflow
All development happened on the `dev` branch. Once a feature was complete
and tested locally, `dev` was merged into `main`, and `main` was pushed to
GitHub. This kept `main` always stable and deployable.

## Version History
| Version | Included |
|---|---|
| v1 | `/` and `/health` endpoints |
| v2 | `/vote/<name>`, `/results`, `/reset` endpoints |
