# dependencies
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.http import FileResponse
from fastai.vision.all import *

# load learner
learn = load_learner("Alzh-sheekar-fast-ai.pkl")
print()


@api_view(['POST'])
def mcc(request):
    image = request.FILES['image']
    default_storage.save(image.name, image)
    result = learn.predict(image.name)
    data = {'result': result}
    default_storage.delete(image.name)

    return Response(data)
