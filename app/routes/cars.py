from flask import Blueprint, jsonify


class Car():
  def __init__(self, id, driver, team, mass_kg):
    self.id = id
    self.driver = driver
    self.team = team
    self.mass_kg = mass_kg

cars = [
  Car(7,"Sainz", "Ferrari", 795),
  Car (88,"SHARLES", "Ferrari", 880),
  Car(4,"Danny Ric", "McLaren", 1138)
]

cars_bp = Blueprint("cars", __name__, url_prefix = "/cars") #we want route to start with /cars

@cars_bp.route("" , methods = ["GET"]) #route can be empty string bc already defined in L17
def get_all_cars(): #decorator needs to be on top of function so it runs get_all_cars function
  response = []
  for car in cars:
    response.append( #python dict very similar to JSON object
        {
            "id": car.id,
            "driver": car.driver,
            "team": car.team,
            "mass_kg": car.mass_kg
        }
    )
  return jsonify(response) #response is in JSON text bc it has shared format between client/server

@cars_bp.route("/<car_id>" , methods = ["GET"])
def get_one_car(car_id): #variable NEEDS to be exact as string decorator in L33
  try:
    car_id = int(car_id)
  except ValueError:
    return jsonify({'message':f'Invalid carid: "{car_id}". ID must be an interger'}), 400
  chosen_car = None
  for car in cars:
    if car.id == car_id:
      chosen_car = { #want to go from class -> dict -> JSON
          "id": car.id,
          "driver": car.driver,
          "team": car.team,
          "mass_kg": car.mass_kg
      }
  if chosen_car is None:
    return jsonify({"message":f"Could not find car with id {car_id}"}), 404
  return jsonify(chosen_car)