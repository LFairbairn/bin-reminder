# Bin Reminder Project - Progress Tracker

## Phase 1: Project Setup

- [x] Install UV (if not already installed)
- [x] Initialize project with `uv init`
- [x] Set up folder structure (`src/`, `tests/`)
- [x] Initialize git repository
- [x] Create `.gitignore` file
- [x] Add initial dependencies to `pyproject.toml`

## Phase 2: Understand the Problem

- [x] Manually explore the council website
- [x] Document the steps needed to get bin data (screenshots/notes)
- [x] Identify the HTML elements to scrape
- [x] Note any quirks (dropdowns, loading states, etc.)

## Phase 3: Data Modeling

- [x] Define what a "bin collection" looks like (fields, types)
- [x] Create `models.py` with Pydantic models
- [x] Write example JSON of expected API response

## Phase 4: Web Scraper

- [x] Install Playwright and browser dependencies
- [x] Write basic script to open council website
- [x] Add postcode entry automation
- [x] Add house number selection from dropdown
- [x] Refactor scraper into separate functions
- [x] Extract bin schedule table data
- [x] Parse extracted data into our models
- [ ] Handle errors gracefully (site down, invalid postcode, etc.)

## Phase 5: Redis Caching

- [ ] Set up Redis locally (Docker or native)
- [ ] Create `cache.py` with connection logic
- [ ] Implement cache key generation
- [ ] Implement get/set operations
- [ ] Add TTL configuration (70 days)
- [ ] Test cache hit/miss scenarios

## Phase 6: FastAPI Application

- [ ] Create basic FastAPI app in `main.py`
- [ ] Add health check endpoint (`/health`)
- [ ] Add bin schedule endpoint (`/schedule`)
- [ ] Wire up scraper and cache
- [ ] Add request validation (postcode format, etc.)
- [ ] Test endpoints manually with docs UI

## Phase 7: Docker

- [ ] Write `Dockerfile` for the app
- [ ] Write `docker-compose.yml` (app + Redis)
- [ ] Test running locally with Docker Compose
- [ ] Document how to run the project

## Phase 8: Testing

- [ ] Set up pytest
- [ ] Write unit tests for data models
- [ ] Write unit tests for cache operations (mocked Redis)
- [ ] Write unit tests for scraper (mocked responses)
- [ ] Write integration test for full flow
- [ ] Add test coverage reporting

## Phase 9: Code Quality & CI/CD

- [ ] Configure ruff for linting
- [ ] Configure mypy for type checking
- [ ] Fix any linting/type errors
- [ ] Create GitHub Actions workflow
- [ ] Test CI pipeline runs on push

## Phase 10: Optional Enhancements

- [ ] Add manual cache refresh endpoint
- [ ] Consider simple frontend (or stick with API docs)
- [ ] Write README with setup instructions
- [ ] Deploy somewhere (optional)

---

## Current Focus

**Phase:** Phase 4 - Web Scraper (nearly complete)

**Next step:** Handle errors gracefully

The scraper now successfully:
- Navigates to the council website
- Enters postcode and selects address
- Extracts bin schedule data
- Parses into BinCollection Pydantic models

Remaining: Add error handling for edge cases (invalid postcode, site down, etc.)

---

## Notes

_Space for questions, blockers, or things to revisit_
