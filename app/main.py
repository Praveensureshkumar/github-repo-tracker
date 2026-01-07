from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import schemas, crud
from app.github_client import fetch_repo

app = FastAPI(title="GitHub Repo Tracker")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.post("/repos", response_model=schemas.RepoResponse, status_code=201)
def create_repo(payload: schemas.RepoCreate, db: Session = Depends(get_db)):
    data = fetch_repo(payload.owner, payload.repo_name)
    if not data:
        raise HTTPException(status_code=404, detail="Repository not found on GitHub")
    return crud.create_repo(db, data)

@app.get("/repos/{repo_id}", response_model=schemas.RepoResponse)
def get_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = crud.get_repo(db, repo_id)
    if not repo:
        raise HTTPException(status_code=404)
    return repo

@app.put("/repos/{repo_id}", response_model=schemas.RepoResponse)
def update_repo(repo_id: int, payload: schemas.RepoUpdate, db: Session = Depends(get_db)):
    repo = crud.get_repo(db, repo_id)
    if not repo:
        raise HTTPException(status_code=404)
    return crud.update_repo(db, repo, payload.name)

@app.delete("/repos/{repo_id}", status_code=204)
def delete_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = crud.get_repo(db, repo_id)
    if not repo:
        raise HTTPException(status_code=404)
    crud.delete_repo(db, repo)
