from sqlalchemy.orm import Session
import models, schemas


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def create_employee(db: Session, new_emp: schemas.EmployeeCreate):
    db_employee = models.Employee(name=new_emp.name, email=new_emp.email)
    db.add(db_employee)
    db.commit()

    db.refresh(db_employee)
    return db_employee


def update_employee(db: Session, emp_id: int, new_emp_data: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    if db_employee:
        db_employee.name = new_emp_data.name
        db_employee.email = new_emp_data.email
        db.commit()
        db.refresh(db_employee)

    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    if db_employee:
        db.delete(db_employee)
        db.commit()

    return db_employee
