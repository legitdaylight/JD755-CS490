import requests

url = 'https://student-info-api.netlify.app/.netlify/functions/submit_student_info'

data = {
    "UCID": "JD755",
    "first_name": "Jeremy",
    "last_name": "De La Rosa",
    "github_username": "legitdaylight",
    "discord_username": "legitdaylight",
    "favorite_cartoon": "Regular Show",
    "favorite_language": "Python",
    "movie_or_game_or_book": "Eternal Sunshine of the Spotless Mind",
    "section": "101"
}

result = requests.post(url, json=data)
if result.status_code != 200:
    print(result.text)
else:
    print("Success!")
    print(result.text)