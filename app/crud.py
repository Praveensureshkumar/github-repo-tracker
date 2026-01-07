from sqlalchemy.orm import Session
from app import models

def create_repo(db: Session, data: dict):
    repo = models.Repository(**data)
    db.add(repo)
    db.commit()
    db.refresh(repo)
    return repo

def get_repo(db: Session, repo_id: int):
    return db.query(models.Repository).filter_by(id=repo_id).first()

def update_repo(db: Session, repo, new_name: str):
    repo.name = new_name
    db.commit()
    db.refresh(repo)
    return repo

def delete_repo(db: Session, repo):
    db.delete(repo)
    db.commit()
