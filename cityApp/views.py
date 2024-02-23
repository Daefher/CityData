import requests
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import City, Item
from .serializers import CitySerializer, ItemSerializer
import time
from openai import OpenAI
import pathlib
import textwrap

import google.generativeai as genai






class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class FetchAndUpdateCityData(APIView):
    client = OpenAI(
    # This is the default and can be omitted
        api_key= 'API-KEY',
    )

    genai.configure(api_key='API-KEY')

    """  def get(self, request, *args, **kwargs):        
        city_name = request.data.get('name')
        city_summary = ""
        try:
            self.genetate_city_sum()
            else:
                return Response({'error': 'Failed to fetch data from Gemini'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"success": "City info recovered", "summary": city_summary}, status=status.HTTP_200_OK) """

    def post(self, request, *args, **kwargs):
        print('Data: ',request.data)
        city_names = request.data.get('cities', [])
        if not city_names:
            return Response({"error": "No city names provided."}, status=status.HTTP_400_BAD_REQUEST)  
        updated_cities = []  # Store information about updated cities here        
        for city_name in city_names:
            try:
                response = requests.get(f'https://wft-geo-db.p.rapidapi.com/v1/geo/cities?namePrefix={city_name}&countryIds=US&limit=1', headers={'X-RapidAPI-Key': '16435dea1bmshb35e91a5ff1f8d4p1cd6a1jsn74941c12fa22'})
                print(response.status_code)
                print(city_name)              
                if response.status_code == 200:
                    data = response.json()['data'][0]
                    summary = self.genetate_city_sum(city_name, data.get('population', 0) )                    
                    city, created = City.objects.update_or_create(
                        name=city_name, 
                        defaults={
                            'population': data.get('population', 0),
                            'latitude': data.get('latitude', 0),
                            'longitude': data.get('longitude', 0),
                            'region': data.get('region', 0),
                            'summary': summary
                        }
                    )
                    updated_cities.append(CitySerializer(city).data)
                    time.sleep(1)
                else:
                    return Response({'error': 'Failed to fetch data from GeoDB Cities API'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"success": "Cities updated successfully", "cities": updated_cities}, status=status.HTTP_200_OK)

   
    def generate_city_summary(self, city_name, city_population):     
        # Adjusted prompt for a conversational approach
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Write a concise summary for the city named {city_name}, with a population, an area of the city in square kilometers and Mention its top attractions."}
        ]

        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Write a concise summary for the city named {city_name}, with a population, an area of the city in square kilometers and Mention its top attractions.",
                }
            ],
            model="davinci-002",
            )
        time.sleep(10)
        # Accessing the content of the response
        summary = response['choices'][0]['message']['content']
        return summary.strip()
 
    def genetate_city_sum(self, city_name, city_population):
        model = genai.GenerativeModel(
            'gemini-pro',
            )
        chat = model.start_chat()
        response = chat.send_message(
            f"Write a concise summary for the city named {city_name}, with a population, an area of the city in square kilometers and Mention its top attractions.",
        )

        return response.text