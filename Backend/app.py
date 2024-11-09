from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Base
import os

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__),"..", "Frontend", "src"), static_url_path="/src")
CORS(app, resources={r"/api/*": {"origins": "http://frontend:3000"}})
DATABASE_URL = 'sqlite:///games.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/admin')
def admin():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/cart')
def cart():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/api/shop', methods=['GET'])
def get_shop():
    with Session() as session:
        games = session.query(Game).all()
        return jsonify([game_to_dict(game) for game in games])
 
@app.route('/shop/<int:game_id>', methods=['GET'])
def get_game(game_id):
     with Session() as session:
       game = session.query(Game).filter_by(id=game_id).first()
       if game:
        return jsonify(game_to_dict(game))
       else:
            return jsonify({"state": "Game not found"}), 404

from datetime import datetime

@app.route('/shop', methods=['POST'])
def add_game():
    try:
        release_date = datetime.strptime(request.json['release_date'], '%Y-%m-%d').date()
        data = request.json
        required_fields = ['name', 'genre', 'price', 'image']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
        
        new_game = Game(
            name=data.get('name'),
            genre=data.get('genre'),
            price=data.get('price'),
            quantity=data.get('quantity'),
            release_date=release_date,
            description=data.get('description'),
            developer=data.get('developer'),
            image=data.get('image')
        )
        with Session() as session:
            session.add(new_game)
            session.commit()
            
            session.refresh(new_game)
            return jsonify(game_to_dict(new_game)), 201

    except Exception as error:
        print("Error adding new game:", error)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/shop/<int:game_id>', methods=['PATCH'])
def update_game(game_id):
    try:
        with Session() as session:
            game = session.query(Game).filter_by(id=game_id).first()
            if game:
                for key, value in request.json.items():
                    setattr(game, key, value)
                session.commit()
                return jsonify(game_to_dict(game))
            else:
                return jsonify({"error": "Game not found"}), 404
    except Exception as error:
        print("Error updating game:", error)
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/shop/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    try:
        with Session() as session:
            game = session.query(Game).filter_by(id=game_id).first()
            if game:
                session.delete(game)
                session.commit()
                return jsonify({"message": "Game deleted"})
            else:
                return jsonify({"error": "Game not found"}), 404
    except Exception as error:
        print("Error deleting game:", error)
        return jsonify({"error": "Internal Server Error"}), 500

def game_to_dict(game):
    return {
        "id": game.id,
        "name": game.name,
        "genre": game.genre,
        "price": game.price,
        "quantity": game.quantity,
        "release_date": game.release_date.isoformat(),
        "description": game.description,
        "developer": game.developer,
        "image": game.image
    }

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True, host='0.0.0.0', port=5000)
