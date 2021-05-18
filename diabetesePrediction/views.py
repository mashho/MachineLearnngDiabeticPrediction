from django.shortcuts import render
import joblib


def home(request):
    return render(request, "home.html")


def predict(request):
    return render(request, "predict.html")


def result(request):
    model = joblib.load("finalize_model.sav")
    li = []
    li.append(int(request.GET['in1']))
    li.append(int(request.GET['in2']))
    li.append(int(request.GET['in3']))
    li.append(int(request.GET['in4']))
    li.append(int(request.GET['in5']))
    li.append(float(request.GET['in6']))
    li.append(float(request.GET['in7']))
    li.append(int(request.GET['in8']))
    ans = model.predict([li])
    res = ""
    if(ans[0] == 0):
        res = "Result : Negative 😄 Healthy 😄 "
    else:
        res = "Result : Positive \n Oops Need to consult Doctor 😢"

    return render(request, "predict.html", {"res": res, "lis": li})
