from models import db, ComputerBaseModel, Storage
from app import app 
from dataclasses import asdict
from flask import jsonify, request, session
from flask_login import login_required, current_user


@app.get("/computerbasemodels")
def list_computerbasemodels():
    # computerbasemodels = db.session.execute(db.select(ComputerBaseModel).join(Storage).order_by(ComputerBaseModel.id)).fetchall()
    computerbasemodels = db.session.execute(db.select(ComputerBaseModel, Storage).join(Storage, Storage.id == ComputerBaseModel.base_storage_id)).fetchall()
    print(computerbasemodels)
    db.session.commit()
    #return computerbasemodels
    #return jsonify([item._asdict()["ComputerBaseModel"] for item in computerbasemodels])
    return jsonify([tuple(row) for row in computerbasemodels])

@app.post("/computerbasemodel")
def create_computerbasemodel():
    print("test")
    print(request)
    data = request.json
    print("DATA:", data)
    computerbasemodel = ComputerBaseModel(
        points_per_member=data["pointsPerMember"],
        points_per_leader=data["pointsPerLeader"]
        )
    db.session.add(computerbasemodel)
    db.session.commit()
    print(computerbasemodel)
    return jsonify(computerbasemodel)



@app.delete("/computerbasemodel/<int:id>")
def delete_computerbasemodel(id: int):
    print(request)
    statement = db.select(ComputerBaseModel).filter_by(id=id)
    computerbasemodel = db.session.execute(statement).scalar_one()
    db.session.delete(computerbasemodel)
    db.session.commit()
    return make_response(f"Successfully deleted computerbasemodel with id {id}", 200)