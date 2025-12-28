---
description: "Task list template for feature implementation"
---

# Tasks: Todo CLI Features

**Input**: Design documents from `/specs/001-todo-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

**Status**: ALL TASKS COMPLETED ✅

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `task.py`, `todo_manager.py`, `main.py` at repository root
- **Tests**: `tests/test_task.py`, `tests/test_todo_manager.py`, `tests/test_cli.py`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize UV project with Python 3.13 in pyproject.toml
- [x] T002 [P] Create empty task.py with Task class skeleton
- [x] T003 [P] Create empty todo_manager.py with TodoManager class skeleton

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [US1][US2][US3][US4][US5] Implement Task class in task.py with id, title, description, is_complete fields
- [x] T005 [US1][US2][US3][US4][US5] Implement TodoManager class in todo_manager.py with _tasks list and _next_id counter

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Task (Priority: P1) MVP

**Goal**: Users can create new tasks with title and optional description, receiving a unique ID

**Independent Test**: Can be fully tested by running add command and verifying task appears with unique ID

- [x] T006 [P] [US1] Implement add_task method in todo_manager.py (adds task with auto-increment ID)
- [x] T007 [P] [US1] Add title validation (reject empty titles with error message)
- [x] T008 [US1] Write unit tests for add_task in tests/test_todo_manager.py

**Checkpoint**: User Story 1 complete - users can add tasks

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1) MVP

**Goal**: Users can see all tasks with ID, title, description, and status

**Independent Test**: Can be fully tested by adding tasks and verifying view displays all correctly

- [x] T009 [P] [US2] Implement list_tasks method in todo_manager.py (returns all tasks in creation order)
- [x] T010 [US2] Implement view_tasks CLI function in main.py (displays formatted task list)
- [x] T011 [US2] Handle empty list case (display "No tasks" message)
- [x] T012 [US2] Write unit tests for list_tasks in tests/test_todo_manager.py

**Checkpoint**: User Story 2 complete - users can view tasks

---

## Phase 5: User Story 3 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks by ID

**Independent Test**: Can be fully tested by adding tasks, deleting one, and verifying it's removed

- [x] T013 [P] [US3] Implement delete_task method in todo_manager.py (removes task by ID)
- [x] T014 [US3] Implement delete_task CLI function in main.py (prompts for ID, calls delete_task)
- [x] T015 [US3] Handle invalid ID error (display "Task with ID {id} not found")
- [x] T016 [US3] Write unit tests for delete_task in tests/test_todo_manager.py

**Checkpoint**: User Story 3 complete - users can delete tasks

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Users can modify task title and/or description by ID with interactive prompts

**Independent Test**: Can be fully tested by adding a task, updating it, and verifying changes

- [x] T017 [P] [US4] Implement update_task method in todo_manager.py (updates title/description)
- [x] T018 [US4] Implement update_task CLI function in main.py (interactive prompts with current values as defaults)
- [x] T019 [US4] Handle invalid ID error
- [x] T020 [US4] Handle empty title validation (reject with error)
- [x] T021 [US4] Write unit tests for update_task in tests/test_todo_manager.py

**Checkpoint**: User Story 4 complete - users can update tasks

---

## Phase 7: User Story 5 - Mark Task Complete (Priority: P3)

**Goal**: Users can toggle task completion status

**Independent Test**: Can be fully tested by adding tasks, marking one complete, and verifying status

- [x] T022 [P] [US5] Implement mark_complete method in todo_manager.py (sets is_complete=True)
- [x] T023 [P] [US5] Implement mark_incomplete method in todo_manager.py (sets is_complete=False)
- [x] T024 [US5] Implement mark_complete CLI function in main.py (prompts for ID and confirmation)
- [x] T025 [US5] Handle invalid ID error
- [x] T026 [US5] Write unit tests for mark_complete/mark_incomplete in tests/test_todo_manager.py

**Checkpoint**: User Story 5 complete - users can toggle completion status

---

## Phase 8: CLI Integration & Polish

**Purpose**: Final integration and cross-cutting concerns

- [x] T027 [P] Implement main menu loop in main.py with options 1-6
- [x] T028 [P] Add error handling for invalid menu choices
- [x] T029 [P] Add exit confirmation and goodbye message
- [x] T030 Write integration tests in tests/test_cli.py (test full user journeys)

**Checkpoint**: All user stories integrated, CLI complete

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Core implementation (TodoManager methods) before CLI integration
- Error handling after basic functionality
- Story complete before moving to next priority
- Tests written alongside or after implementation

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Core implementation tasks marked [P] within each story can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all core implementation tasks for User Story 1 together:
Task: "Implement add_task method in todo_manager.py"
Task: "Add title validation in add_task method"
```

---

## Implementation Strategy

### MVP First (User Stories 1 + 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. **STOP and VALIDATE**: Test Add + View functionality independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Stories 3, 4, 5
3. Stories complete and integrate independently

---

## Task Summary

| Phase | Tasks | Description | Status |
|-------|-------|-------------|--------|
| Phase 1: Setup | T001-T003 | Project initialization | ✅ Complete |
| Phase 2: Foundational | T004-T005 | Task and TodoManager classes | ✅ Complete |
| Phase 3: US1 Add Task | T006-T008 | Add task functionality | ✅ Complete |
| Phase 4: US2 View Tasks | T009-T012 | View task functionality | ✅ Complete |
| Phase 5: US3 Delete Task | T013-T016 | Delete task functionality | ✅ Complete |
| Phase 6: US4 Update Task | T017-T021 | Update task functionality | ✅ Complete |
| Phase 7: US5 Mark Complete | T022-T026 | Toggle completion status | ✅ Complete |
| Phase 8: Polish | T027-T030 | CLI integration and tests | ✅ Complete |

**Total Tasks**: 30 | **Completed**: 30 | **Remaining**: 0

---

## Test Results

| Test Suite | Tests | Passed | Failed |
|------------|-------|--------|--------|
| test_todo_manager.py | 26 | 26 | 0 |
| test_cli.py | 10 | 10 | 0 |
| **Total** | **36** | **36** | **0** |

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
