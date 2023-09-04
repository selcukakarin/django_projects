# eureka pyton api - mp4 to wav and wav to text

### Yükleme adımları

Projeyi çalıştırabilmek için iki yol var birincisi docker compose ile çalıştırmak ikincisi ise python ile run etmek

**Çalıştırmak için**  
- Projeyi clone et
- Proje klasörüne ilerle (manage.py dosyasının oldugu klasör) (admin or main)

1. yol

- Run `docker-compose up`


** Hata olmazsa proje `0.0.0.0:8000`   portunda çalışmaya başlar.

2. yol

- python3.8.5 sürümünü lokale yükle
- manage.py dizinindeyken `python manage.py runserver` komutunu terminalde çalıştır.


**Çalışma şekli**

Gelen istek aşağıdakiler gibi olmalı. Post requestin body'ne bu proje yolundaki **test_media** isimli klasör yolundaki bir .mp4 dosyasının yolu `file` isimli değişken ile gönderilir. Bu .mp4 dosyasından gönderilen dosya ismini gönderildiği saat ile birleştirerek bu isimde yeni bir wav dosyası oluşturulur. bu wav dosyası da işlenerek geriye aşağıdaki örnekteki output dönmüş olur.

Example Post Request

CURL
```curl
curl --location 'http://127.0.0.1:8000/api/transcribe/' \
--header 'Content-Type: application/json' \
--data '{
   "file": "test_media/test.mp4"
}'
```


C# Http Client
```c#
var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Post, "http://127.0.0.1:8000/api/transcribe/");
var content = new StringContent("{\n   \"file\": \"test_media/test.mp4\"\n}", null, "application/json");
request.Content = content;
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

Python
```python
import requests
import json

url = "http://127.0.0.1:8000/api/transcribe/"

payload = json.dumps({
  "file": "test_media/test.mp4"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```
input
```
{
   "file": "test_media/test3.mp4"
}
```

output
```
[
    {
        "start": 0.0,
        "end": 7.28,
        "text": " Bu şekilde size kitaplan isimden tek tek söylemeyeceğim zaten ekranı görürsün ama ilk başlamanız gereken iki kita birincisi murat kurtuluyun."
    },
    {
        "start": 7.28,
        "end": 16.0,
        "text": " Kitabı ikincisi de şimdi göreceğiz, ebru yeniren kitabı. Bu hiç bilmiyorsanız veya biraz toplamak istiyorsanız gayet işinize yerler."
    },
    {
        "start": 16.0,
        "end": 22.96,
        "text": " Şimdi göreceğiniz kitapla biraz daha böyle alır hafif. Yani İngilizce biliyorum ama konuşamıyorum."
    },
    {
        "start": 22.96,
        "end": 29.76,
        "text": " Toplamak için fikret kananın iki bir sonra kitapsa İngilizce de ileri seviydi ama"
    },
    {
        "start": 29.76,
        "end": 35.44,
        "text": " düzgün kalabalık makalliler falan yazamıyorum biraz daha havalıcımlarını kurmak istiyom diyenler için."
    },
    {
        "start": 35.44,
        "end": 41.44,
        "text": " Bu vahin şekilde ileri seviyi İngilizce isteyenler için. Bu ve bundan sonra geleceğiniz"
    },
    {
        "start": 41.44,
        "end": 46.32,
        "text": " İngilizce kıramenin yürs, serisi ki İngilizc kıramenin yürs, serisi birkaç kitaptır."
    },
    {
        "start": 46.32,
        "end": 50.72,
        "text": " Bu tüm bu seri ileri seviyi İngilizce için, iyice geçtirmek için."
    },
    {
        "start": 50.72,
        "end": 58.0,
        "text": " Daha basit, daha ucuz bir kira parıyorsanız, seri miyeni kendin modern İngilizce kitabında temin edebilirsiniz."
    }
]
```