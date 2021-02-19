from flask import Flask, jsonify, request
from http import HTTPStatus

endpoints = """
POST
   "/api/v1/MeteringPoints/{meteringPointId}/ping",
    "/api/v1/MeteringPoints/{meteringPointId}/readdevicelogs",
    "/api/v1/MeteringPoints/{meteringPointId}/readmomentaryvalues",
    "/api/v1/MeteringPoints/{meteringPointId}/readpoweroutagelogs",
    "/api/v1/MeteringPoints/{meteringPointId}/readseries",
    "/api/v1/DeviceConfiguration/{meteringPointId}",
    "/api/v1/MeteringPoints/{meteringPointId}/link",
    "/api/v1/MeteringPoints/{meteringPointId}/unlink",
    "/api/v1/MeteringPoints",
GET
    "/api/v1/MeteringPoints/{meteringPointId}/Device",
    "/api/v1/MeteringPoints/{meteringPointId}/History", 
"""
app = Flask(__name__)

records = [
    {
        "id": "1",
        "name": "Mule Max",
        "class": 5
    },
    {
        "id": "2",
        "name": "John Link",
        "class": 8
    }
]


#################################################
@app.route('/records', methods=['GET'])
def get_records():
    return jsonify({"data": records})


##################################################

##################################################
@app.route("/api/v1/MeteringPoints/<string:meteringPointId>/ping", methods=["POST"])
def ping_meteringpoint(meteringPointId):
    print(f"Looking up meteringpoint {meteringPointId}")
    # record = next((record for record in records if record["id"] == meteringPointId), None)
    # if record:
    #     return jsonify(record)
    return jsonify({"message": "record not found"}), HTTPStatus.NOT_FOUND


@app.route("/api/v1/MeteringPoints/<string:meteringPointId>/readdevicelogs", methods=["GET"])
def read_device_logs_meteringpoint(meteringPointId):
    record = next((record for record in records if record["id"] == meteringPointId), None)
    if record:
        return jsonify(record)
    return jsonify({"message": "record not found"}), HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run(port=5001)
