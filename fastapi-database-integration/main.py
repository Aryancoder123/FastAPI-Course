import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import sessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create-employee", response_model=schemas.EmployeeOut)
def create_employtee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


@app.get("/get-employees", response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/get-employee/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found!")
    return employee


@app.put("/update-employee/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(
    emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)
):
    employee = crud.update_employee(
        db,
        emp_id,
        employee,
    )
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found!")
    return employee


@app.delete("/delete-employee/{emp_id}", response_model=schemas.EmployeeOut)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="employee not found!")
    return employee
