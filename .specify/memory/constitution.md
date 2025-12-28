# Phase-I Todo Console App Constitution

## Core Principles

### I. Spec-Driven Development
Every feature MUST begin with a documented specification. No implementation without a spec.
All work traces through: Spec → Plan → Tasks → Implementation → Verification.
The specification serves as the authoritative source for requirements and acceptance criteria.

### II. Clean Code
Code MUST be readable, maintainable, and well-structured. Follow PEP 8 guidelines.
Meaningful naming, appropriate abstraction, and self-documenting code are non-negotiable.
Code is written for humans first, machines second.

### III. CLI-First Interface
The application operates exclusively through a command-line interface.
All functionality MUST be accessible via CLI arguments with clear, consistent syntax.
User experience prioritizes simplicity and discoverability.

### IV. Memory-Only Storage
No persistent storage mechanisms are permitted. All data exists in-memory only.
Data is lost when the application exits. No file-based or database persistence.
This constraint simplifies design and ensures stateless operation.

### V. Minimal Dependencies
Use UV for all package management. External dependencies MUST be justified by need.
Prefer standard library solutions where available. Each added dependency increases maintenance burden.

## Technical Constraints

- Python 3.13+ required
- UV package manager for dependency management
- In-memory data storage only (no files, no databases)
- CLI-only interface (no GUI, no web)
- Single command invocation for all operations

## Development Workflow

1. **Specification**: Document feature requirements in spec.md
2. **Planning**: Create architecture decisions in plan.md
3. **Tasking**: Break down work into testable tasks in tasks.md
4. **Implementation**: Red-Green-Refactor cycle with passing tests
5. **Verification**: Validate against specification acceptance criteria

All changes MUST trace back to documented requirements. No untracked work.

## Governance

This constitution supersedes all other development practices within the project.

**Amendment Procedure**: Changes require documentation of rationale, impact assessment, and updated specifications.

**Compliance**: All PRs and reviews MUST verify adherence to these principles. Deviations require explicit justification.

**Version**: 1.0.0 | **Ratified**: 2025-12-28 | **Last Amended**: 2025-12-28
