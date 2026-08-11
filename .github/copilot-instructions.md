<!-- Repository-level instructions for GitHub Copilot and Copilot Chat -->

# Copilot instructions for this repository

## Project Description

This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse, view, and download assignments directly from the portal.

## Project Structure

- [`assignments/`](../assignments/) Each homework assignment is stored in its own subfolder with a consistent structure.
- [`templates/`](../templates/) Reusable templates for new content
- [`assets/`](../assets/) Contains the website assets including CSS, JavaScript, images, and configuration files
- [`index.html`](../index.html) The main website page that serves as a static portal for browsing and viewing assignments. Content is configurable via [`config.json`](../config.json) file to dynamically generate assignment lists and details.

## Project Guidelines

- Maintain consistent styling across all pages
- Keep file and folder names descriptive and organized

## Educational Standards

When generating content for this project:

- **Learning-focused**: All content should be designed with clear learning objectives and appropriate difficulty levels
- **Student-friendly**: Use clear, encouraging language that motivates students

Purpose
- Help contributors and Copilot produce consistent, idiomatic code and useful suggestions.

Repository context
- Languages: Python (assignments, starter code), JavaScript (site scripts), HTML/CSS.
- Primary goals: small teaching assignments, readable starter code, no heavy external dependencies.

When writing code
- Prefer clarity and simplicity over cleverness.
- For Python: follow PEP 8 conventions and use type hints where helpful.
- For JavaScript: follow existing project style in `assets/js` and keep browser compatibility in mind.
- Keep functions small and focused; include brief docstrings or comments for non-obvious logic.

Testing and examples
- When suggesting code for assignments, include a short usage example or a simple test snippet.

Documentation and assignments
- Use plain language suitable for learners. Keep explanations concise and example-driven.
- When updating `templates/assignment-template.md`, preserve the template structure.

Commits and PRs
- Prefer concise, imperative commit messages (e.g., "Add input validation to parser").

Security and secrets
- Never suggest or include real secrets, credentials, or private keys in code or examples.

If unsure
- Ask clarifying questions before making large changes to assignment content or templates.

Thank you for helping keep this repository educational and approachable.
