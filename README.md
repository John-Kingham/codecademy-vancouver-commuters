# Codecademy Vancouver Commuters Project
## Purpose
To practice creating and using graphs, breadth-first and depth-first search.

## Description
For this project, we imagine that the Vancouver public metro system wants a program that helps commuters get from one landmark to another as quickly as possible. It should do this by calculating the shortest route between metro stations close to each landmark. For the purposes of this project, we will assume it takes the same time to get from each station to each of its connected neighboring stations (i.e. the stations are unweighted).

## Requirements
1. As a tourist, I should be able to select two landmarks and be shown the shortest metro route between them, so I can efficiently plan my holiday in Vancouver.

## Architecture & high-level design
- Language: Python 3
- Paradigm: Procedural (functions, not classes)
- Main subsystems:
  - User interface:
    - Text via the terminal
  - Application logic:
    - A graph will be used to represent the metro stations and the links between them
    - A depth-first search will confirm that a route exists (or not)
    - A breadth-first search will return the shortest route
  - Database:
    - All data will be stored in Python data structures (dictionaries, lists, etc.)

## Progress
I'm using GitHub Issues to track my tasks and progress on this project.