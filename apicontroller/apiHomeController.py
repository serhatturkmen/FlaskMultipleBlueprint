from . import apiBlueprint as api


@api.route('/', methods=['GET', 'POST'])
def apihome():
   return "Api"


