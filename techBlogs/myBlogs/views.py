from django.shortcuts import render , HttpResponse
import requests
# Create your views here.

def index (request):
    context={
        'a':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/iHSwvRVsRyxpX7FE7GbviaDvgGZ.jpg',
        'b':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/9PFonBhy4cQy7Jz20NpMygczOkv.jpg',
        'c':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/3ayWL13P1HeRnyVL9lU9flOdZjq.jpg',
        'd':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/uNjnoT3RChs2r7O9pDyx7TNBvIj.jpg',
        'e':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/npdB6eFzizki0WaZ1OvKcJrWe97.jpg',
        'f':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/7wuKrFvbX7kAIF0ctotARsqayPo.jpg',
        'g':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/8CXbCCGiJxi4AXPBQ1QPrehMIGG.jpg',
        'h':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/6ZfiG4P7jivJV0wgcNMSiS2Owhh.jpg',
        'i':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/jFZJEoPzt2RKSsZG8QEWptX5Xyw.jpg',
        'j':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/ixgnqO8xhFMb1zr8RRFsyeZ9CdD.jpg',
        'k':'https://image.tmdb.org/t/p/w600_and_h900_bestv2/rdNwXdMDVDvjOlcXCPOR3m9t43r.jpg'
        
    }
    
  
    return render(request,'index.html',context)

def home(request):
    response=requests.get("https://api.themoviedb.org/3/tv/popular?api_key=15e383204c1b8a09dbfaaa4c01ed7e17&language=en-US&page=1").json()
    
    return render(request,'index.html' ,{'response':response})