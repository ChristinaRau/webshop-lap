from app import app
from models import db, PointsPerMember, PointsPerLeader, PointsPerTeamView
from flask import jsonify


@app.route("/max_team")
def max_team():
    print("GET request max_team")
    statement = db.select(PointsPerTeamView).where(
        PointsPerTeamView.total_points_sum
        == db.select(db.func.max(PointsPerTeamView.total_points_sum)).scalar_subquery()
    )
    row = db.session.execute(statement).scalar_one_or_none()
    print(row)
    return jsonify({"value": row.total_points_sum, "team_id": row.team_id})


@app.route("/max_leader")
def max_leader():
    print("GET request max_leader")
    statement = db.select(PointsPerLeader).where(
        PointsPerLeader.sum_points
        == db.select(db.func.max(PointsPerLeader.sum_points)).scalar_subquery()
    )
    row = db.session.execute(statement).scalar_one_or_none()
    print(row)
    return jsonify(
        {
            "sum_points": row.sum_points,
            "leader_person_id": row.leader_person_id,
            "person_name": row.person_name,
            "project_count": row.project_count,
        }
    )


@app.route("/max_member")
def max_member():
    print("GET request max_member")

    statement = db.select(PointsPerMember).where(
        PointsPerMember.sum_points
        == db.select(db.func.max(PointsPerMember.sum_points)).scalar_subquery()
    )
    row = db.session.execute(statement).scalar_one_or_none()
    print(row)
    return jsonify(
        {
            "sum_points": row.sum_points,
            "person_id": row.person_id,
            "person_name": row.person_name,
            "project_count": row.project_count,
            "team_count": row.team_count,
        }
    )
