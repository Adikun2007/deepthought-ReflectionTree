# Daily Reflection Tree – DeepThought Assignment

## Overview
This project is a simple, structured reflection tool built using a deterministic decision tree. Instead of using AI or open-ended input, it guides the user through a fixed set of questions to help them reflect on their day in a clear and focused way.

The system is designed to simulate thoughtful reflection by asking targeted questions and analyzing responses across three key behavioral axes:

- Locus of Control → Did you feel in control or driven by circumstances?
- Contribution vs Entitlement → Were you focused on giving or expecting?
- Perspective (Self vs Others) → Did you think mostly about yourself, your team, or others?

At the end, the system generates a short summary based on your answers.

## Structure
    ├── tree/
    │   └── ReflectionTree.json    # Decision tree structure    
    │
    ├── agent/
    │   └── CLI_agent.py           # CLI-based reflection program
    │
    └── write-up.md                # Explanation of design decisions

## How It Works
The entire flow is defined in a JSON file as a tree of nodes
Each node represents one of the following:
- Question
- Decision (branching logic)
- Reflection (conditional feedback)
- Summary
The Python script reads this JSON and moves step-by-step through the tree
Based on your answers, it:
- Tracks signals across the three axes
- Chooses the next node deterministically
- Displays reflections only when conditions match
Finally, it prints a personalized summary using your dominant patterns

## How to Run
1. Go to the agent folder:
    cd agent
2. Run the script:
    python CLI_agent.py
3. Answer the questions by entering the option number

## Features
### Deterministic flow
    -> No randomness or AI — same inputs always lead to the same outputs
### Structured reflection
    -> Questions are designed to guide thinking without overwhelming the user
### Signal-based tracking
    -> Each answer updates internal signals across predefined axes
### Conditional reflections
    -> Feedback is shown only when certain patterns are detected
### Final summary generation
    -> A short summary is created using the dominant signals

## Design Philosophy
The goal of this project is to show that meaningful reflection doesn’t always require AI.
By carefully designing questions and decision logic, we can create a system that feels thoughtful and guided while remaining fully deterministic.

### This also makes the system:
    -> Easy to debug
    -> Transparent in behavior
    -> Consistent in output