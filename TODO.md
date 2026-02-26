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
- [x] Add TTL configuration (42 days / 6 weeks)
- [x] Test cache hit/miss scenarios

## Phase 6: FastAPI Application

- [x] Create basic FastAPI app in `main.py`
- [x] Add health check endpoint (`/health`)
- [x] Add bin schedule endpoint (`/schedule`)
- [x] Wire up scraper and cache
- [x] Add request validation (postcode format, etc.)
- [x] Test endpoints manually with docs UI
- [x] Add cache clear endpoint (`/cache` DELETE)

## Phase 7: Docker

- [x] Write `Dockerfile` for the app
- [x] Write `docker-compose.yml` (Redis + redis-commander for dev)
- [x] Test running locally with Docker Compose
- [x] Document how to run the project

## Phase 8: Testing

- [x] Set up pytest
- [x] Write unit tests for data models
- [x] Write integration test for cache operations
- [x] Write unit tests for scraper (mocked responses)
- [ ] _(Optional)_ Write integration test for full flow
- [x] Add test coverage reporting

## Phase 9: Code Quality & CI/CD

- [x] Configure ruff for linting
- [x] Configure mypy for type checking
- [x] Fix any linting/type errors
- [x] Create GitHub Actions workflow
- [x] Test CI pipeline runs on push

## Phase 10: Frontend

- [x] Create static HTML page served by FastAPI
- [x] Mobile-first responsive design
- [x] Save postcode/address in localStorage
- [x] Display next bin prominently with colour coding
- [x] Show list of upcoming collections (always at least 1, plus others within 7 days)
- [x] Group bins by date (blue+brown can share a day)
- [x] Split colour gradient for combined blue/brown collections
- [ ] _(Optional)_ PWA upgrade (manifest.json, service worker, add to home screen)

## Phase 11: Deployment & Extras

- [x] Add manual cache refresh endpoint
- [x] Write README with setup instructions
- [ ] Deploy somewhere (optional)

---

## Current Focus

**Phase:** Complete

**Completed:** Phase 10 - Frontend

**Also done:**
- Model unit tests with pytest
- Test coverage reporting (30% threshold)
- Ruff linting in CI
- Mypy type checking in CI
- Static HTML frontend with localStorage
- Frontend groups same-day collections with split colour display
- App runs on port 8001

---

## Notes

- Scraper tests done using MagicMock for Playwright page responses
- Council website provides ~7 weeks of data (not 11 as initially assumed)
- Blue and brown bins can go out on the same day (separate rows, same date)
- Green and grey bins always go out on their own
- Cache TTL reduced from 70 days to 42 days (6 weeks) to match actual data window
- Docker Compose maps port 8001 (host) to 8000 (container) to avoid conflicts
