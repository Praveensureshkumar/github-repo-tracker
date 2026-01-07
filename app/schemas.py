from pydantic import BaseModel

class RepoCreate(BaseModel):
    owner: str
    repo_name: str

class RepoUpdate(BaseModel):
    name: str

class RepoResponse(BaseModel):
    id: int
    name: str
    owner: str
    stars: int
    url: str

    class Config:
        orm_mode = True
