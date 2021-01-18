from . import controllerBlueprint as home


@home.route('/', methods=['GET', 'POST'])
def index():
   return "Home"


