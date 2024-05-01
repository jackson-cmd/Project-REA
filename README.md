# Project
## How to run it?
- Download the current folder 
- run `npm install`
- run `npm start`
- Open `localhost:8080` on your browsers.
## Run our automated experiment to get the threshold
- run `npm start`
- run `python main.py`
- It will write results to cpu_usage.csv automatically. For each API, you can change it from `pp.js`.
## Experiment
### Environment
Environment setup is discussed in the paper in details.
### Measure vector
20 experiments (Get average)
- Measure CPU usage
- Measure How long it takes for OS to kill it. (1 minutes max)
- Effects
  - Can change tab
  - Can close the tab
  - Can close browser
- Testing data are in the paper appendix
## Mitigation Tools - CPUWatch
- run `python cpuwatch.py`
- input `threshold` based on the experiment before
- If a warning occurs, check the vulnerable pages
