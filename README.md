# Project
## How to run it?
- Download the current folder 
- run `npm install`
- run `npm start`
- Open `localhost:8080` on your browsers.
## Run our automated experiment to get threshold
- run `npm start`
- run `python main.py`
- It will write results to cpu_usage.csv automatically. For each API, you can change it from `pp.js`.
## Experiment
20 experiments (Get average)
- Measure CPU usage
- Measure How long it takes to OS to kill it? (1 minutes max)
- Effects
  - Can change tab
  - Can close tab
  - Can close browser
