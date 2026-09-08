# Periscope Mining System

An enterprise internal operations, compliance verification, and payroll calculation platform for mining subcontractors.

## System Architecture

- **Frontend:** Next.js (App Router, JavaScript, Tailwind CSS)
- **Backend:** FastAPI (Python 3.12+, SQLAlchemy 2.x, Pydantic v2)
- **Database:** PostgreSQL (Supabase)
- **Authentication:** Supabase Auth
- **File Storage:** Supabase Storage

## Development Setup

### Prerequisites
- Node.js 18+
- Python 3.12+
- `uv` (Python Package Manager)

### Running Backend
```bash
cd backend
uv run uvicorn app.main:app --reload --port 8000