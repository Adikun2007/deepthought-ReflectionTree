# Design Write-up

## Approach

The main goal of this project was to turn something abstract like daily reflection into a structured and deterministic system.

Instead of relying on open-ended questions or AI, I designed a decision tree that guides the user step by step. The idea was to make reflection feel simple and accessible, while still being meaningful.

A key decision was to focus on what the user did rather than what they think about themselves. This helps avoid vague or biased answers and keeps the reflection grounded in real actions.

----------------------------------------------------------------------------------------------------

## Question Design

The questions are designed around everyday situations rather than direct psychological labels.

For example:

    -> Instead of asking “Do you take responsibility?”, the system asks what the user actually did when faced with a challenge.
    -> Instead of asking “Are you helpful?”, it asks how they behaved in interactions.

This approach makes the responses:
    - More honest
    - Easier to answer
    - Less influenced by what the user thinks is the “right” answer

All questions are multiple-choice to keep the flow fast and reduce cognitive load.

----------------------------------------------------------------------------------------------------

## Branching Logic

The tree starts by identifying the general tone of the user’s day (e.g., productive, draining). Based on this, it branches into slightly different paths.

However, instead of creating a very deep or complex tree, the flow converges again after the initial branching. This keeps the experience:

-   Simple
-   Predictable
-   Not too long or exhausting

Each answer contributes to internal “signals” across three axes. These signals are then used later for reflections and the final summary.

----------------------------------------------------------------------------------------------------

## Psychological Concepts Used

The system is inspired by a few well-known psychological ideas:

- Locus of Control
    -> Whether a person feels in control of outcomes or influenced by external factors
- Growth Mindset (implicit)
    -> Reflected through actions like adapting, trying new approaches, or seeking help
- Contribution vs Entitlement
    -> Whether the focus is on giving value or expecting recognition
- Perspective-taking
    -> Whether the user’s thinking is centered on themselves, their team, or others

These concepts are not directly mentioned to the user but are embedded in the options and signals.

----------------------------------------------------------------------------------------------------

## Trade-offs

While designing the system, I made a few conscious trade-offs:

### Simplicity over depth
    -> A deeper tree could provide more accuracy, but it would also make the experience longer and more tiring
### Fixed options over flexibility
    -> Using predefined answers ensures consistency, but limits personalization
### Neutral options included
    -> Some options are intentionally neutral to avoid forcing users into extreme choices

The goal was to balance meaningful reflection with usability.

# --------------------------------------- THANK YOU ------------------------------------------------