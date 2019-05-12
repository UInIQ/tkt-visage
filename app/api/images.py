from app.api import bp
from flask import jsonify
from app.models import Image, ImageStatus
from app import db
from sqlalchemy import func

@bp.route('/images/counts', methods=['GET'])
def get_image_counts():
    out_dict={}
    counts_list = db.session.query(func.count(Image.id),ImageStatus.label).group_by(Image.status).join(ImageStatus).all()
    for count in counts_list:
        out_dict[count[1]]=count[0]
    return jsonify(out_dict)