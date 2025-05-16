from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import UserDB
from schemas import UserCreate, UserResponse

# สร้างฐานข้อมูล
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create: สร้างสินค้าใหม่
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_item = UserDB(**user.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Read: อ่านสินค้าทั้งหมด
@app.get("/users/", response_model=List[UserResponse])
async def read_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()

# Read: อ่านสินค้าตาม ID
@app.get("/users/{user_id}", response_model=UserResponse)
async def read_item(user_id: int, db: Session = Depends(get_db)):
    db_item = db.query(UserDB).filter(UserDB.id == user_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_item

# Update: อัปเดตสินค้าตาม ID
@app.put("/users/{user_id}", response_model=UserResponse)
async def update_item(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_item = db.query(UserDB).filter(UserDB.id == user_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete: ลบสินค้าตาม ID
@app.delete("/users/{user_id}")
async def delete_item(user_id: int, db: Session = Depends(get_db)):
    db_item = db.query(UserDB).filter(UserDB.id == user_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_item)
    db.commit()
    return {"message": "User deleted"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)