from django.shortcuts import render
import requests



def home(req):
    q = req.GET.get('q')
    api_key = '063788da0dcf40a521363c430649fd22'
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}'

    try:
      response = requests.get(api_url)
      data = response.json()
      if data.get("cod") != 200:
        return render(req,"404.html")
      else:
        city = q
        description = data["weather"][0]["description"]
        temp = data['main']["temp"]
        icon = data["weather"][0]["icon"]
        context ={
          'city': city,
          'description': description,
          'temp': temp,
          'humidity': data['main']['humidity'],
          'icon': icon
        }

        return render(req, 'index.html',context)
    except Exception as e:
        print(e)  
        return render(req, '404.html')   
 