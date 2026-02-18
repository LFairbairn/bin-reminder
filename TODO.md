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
- [x] Handle errors gracefully (site down, invalid postcode, etc.)
  - [x] Custom `ScraperError` exception
  - [x] Page load failures (network/site down)
  - [x] Address not found (invalid postcode or missing address)
  - [ ] _(Optional)_ Council page structure changes (selector breakage)
  - [ ] _(Optional)_ Unexpected bin colour not in enum
  - [ ] _(Optional)_ Date format changes

## Phase 5: Redis Caching

- [x] Set up Redis locally (Docker or native)
- [x] Create `cache.py` with connection logic
- [x] Implement cache key generation
- [x] Implement get/set operations
- [x] Add TTL configuration (70 days)
- [x] Test cache hit/miss scenarios

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

**Phase:** Phase 6 - FastAPI Application

**Completed:** Phase 5 - Redis Caching

The cache now:
- Connects to Redis (Docker container)
- Generates unique cache keys from postcode + address
- Stores bin collections as JSON with 70-day TTL
- Retrieves and parses cached data back to models
- Returns None for cache misses

---

## Notes

_Space for questions, blockers, or things to revisit_
