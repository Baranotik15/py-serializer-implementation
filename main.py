from car.models import Car
import io
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = Car(**serializer.validated_data)
        if 'id' in data:
            car.id = data['id']
        return car
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
