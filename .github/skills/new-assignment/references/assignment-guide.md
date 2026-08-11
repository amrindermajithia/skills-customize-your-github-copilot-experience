# Assignment Guide

This guide helps contributors choose an appropriate difficulty, scope, and decide when to include starter code or data files for new programming assignments.

## Purpose

Provide consistent, classroom-friendly guidance so assignments are clear, focused, and solvable within the target timeframe.

## Difficulty & Scope

- Target a single primary concept (e.g., loops, functions, file I/O) with 1–2 secondary concepts.
- Beginner assignments: 30–60 minutes expected work. Keep instructions explicit and provide examples.
- Intermediate assignments: 1–2 hours expected work. Allow students to design small components or helper functions.
- Advanced assignments: 2+ hours or multi-day projects. Split into subtasks and include acceptance criteria.
- Keep scope small: one assignment should not require building an entire application unless explicitly framed as a multi-part project.

## When to Include Starter Code

- Include starter code when:
  - The environment setup or boilerplate is non-trivial (e.g., reading files, setting up a small data set).
  - You want all students to start from a common scaffold (function signatures, basic tests).
- Avoid heavy starter code that solves the core problem; provide only helpful scaffolding (I/O helpers, sample dataset loader, function stubs).

## File Types & Attachments

- Common attachments: `starter-code.py`, `data.csv`, `sample_input.txt`, `tests.py`.
- Name attachments clearly and register them using the provided scripts in `.github/skills/new-assignment/scripts/`.

## Template & Structure

- Use the repository assignment template at `templates/assignment-template.md` and create the assignment as `assignments/<id>/README.md`.
- Provide a short `🎯 Objective`, then `📝 Tasks` with measurable `Requirements` for each task.

## Acceptance Checklist (Before Publishing)

- README follows the template and includes example input/output where helpful.
- Starter code (if provided) runs without errors and does not contain the full solution.
- All attachments are registered via the helper scripts and appear in `config.json`.
- Assignment metadata (`id`, `title`, `description`, `dueDate`) is present and accurate.

## Examples

- Beginner: "Implement a function that counts word frequency in a text file." (include small `sample.txt`)
- Intermediate: "Build a command-line Hangman game" (include minimal `starter-code.py` with function stubs)

If you need a starter-code template or a small test harness, ask and I can generate one.

# Assignment Design Guide

Guidance for designing assignment content — what to teach and how to scope it. For formatting and markdown structure, the project's instruction files handle that automatically.

## Difficulty & Scope

- Target 2–4 tasks per assignment that build on each other
- Start with something a student can finish in under 10 minutes, then add complexity
- The last task can be a stretch goal, but earlier tasks should build confidence
- Stick to one core concept per assignment (e.g., "loops", not "loops + file I/O + error handling")

## Starter Code

Include starter code when:

- The assignment needs boilerplate the student shouldn't write from scratch
- You want students to follow a specific function signature or structure

Skip it when the point is writing something from scratch (e.g., "write a script that…").

## Example Topics by Difficulty

- **Beginner**: variables, conditionals, loops, string formatting
- **Intermediate**: functions, lists/dicts, file I/O, basic classes
- **Advanced**: APIs, data analysis, testing, web frameworks

