# route.py

from flask import Blueprint, jsonify, request
from model import Manager
from flask import request
from model import Manager, GroupInfo, Visitor ,Influencer  # Importe os modelos adicionais aqui
from database import db

api_blueprint = Blueprint('api', __name__)

################### INFLUENCER ###################################
@api_blueprint.route('/influencers', methods=['GET'])
def get_influencers():
    influencers_list = Influencer.query.all()
    return jsonify([{"influencer_id": influencer.influencer_id, "name": influencer.name,"url": influencer.url} for influencer in influencers_list])


@api_blueprint.route('/influencers', methods=['POST'])
def create_influencer():
    data = request.get_json()
    new_influencer = Influencer(influencer_id=data['influencer_id'],name=data['name'], url=data['url'])  # supondo que o JSON recebido tenha 'name' e 'follower_count'
    db.session.add(new_influencer)
    db.session.commit()
    return jsonify({"message": "Influencer created successfully"}), 201
##################################################################

################### GROUP INFOS ##################################
@api_blueprint.route('/groupinfos', methods=['GET']) 
def get_groups_infos():
    group_infos_list = GroupInfo.query.all()
    return jsonify([{"group_info_id": group_infos.group_info_id, "name": group_infos.name} for group_infos in group_infos_list])

##################################################################

################### MANAGER ##################################
@api_blueprint.route('/managers', methods=['GET'])
def get_managers():
    Manager_list = Manager.query.all()
    return jsonify([{"manager_id": managers.manager_id, "user_name": managers.user_name} for managers in Manager_list])

##################################################################

################### VISITORS #####################################
@api_blueprint.route('/visitors', methods=['GET'])
def get_visitors():
    Visitor_list = Visitor.query.all()
    return jsonify([{"group_info_id": visitors.visitor_id, "name": visitors.name} for visitors in Visitor_list])

##################################################################

@api_blueprint.route('/managers', methods=['POST'])
def create_manager():
    data = request.get_json()
    new_manager = Manager(user_name=data['user_name'], password=data['password'])
    db.session.add(new_manager)
    db.session.commit()
    return jsonify({"message": "Manager created successfully"}), 201

#@api_blueprint.route('/visitors', methods=['GET'])
#def get_visitors():
#    visitors_list = Visitor.query.all()
#    return jsonify([{
#        "visitor_id": visitor.visitor_id,
#        "influencer_id": visitor.influencer_id,
#        "referer": visitor.referer,
#        "location": visitor.location,
#        "link_id": visitor.link_id,
#        "created_at": visitor.created_at.isoformat(),
#        "headers": visitor.headers
#    } for visitor in visitors_list])
# @api_blueprint.route('/api', methods=['GET'])
# def api():
#     data = get_data()
#     return jsonify(data)