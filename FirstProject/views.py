from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    name = "BASDSADF"
    doc = open("C:/PRUEBAS/FirstProjectDjango/FirstProject/FirstProject/Views/First.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context({"name": name,"lista": ["sdfas","asefasfa","asdfasfa","sadfasfa"]})
    documento = plt.render(ctx)
    return HttpResponse(documento)
