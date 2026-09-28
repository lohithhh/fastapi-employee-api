from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2)
    email: str
    department: str = Field(min_length=2)
    salary: int = Field(gt=0)


class EmployeeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2)
    email: str | None = None
    department: str | None = Field(default=None, min_length=2)
    salary: int | None = Field(default=None, gt=0)


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str | None
    department: str
    salary: int

    model_config = {
        "from_attributes": True
    }