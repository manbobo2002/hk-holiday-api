# How to install
### Clone the repo
```shell
$ git clone https://github.com/manbobo2002/hk-holiday-api.git
```

### Install requirements

```shell
$ pip install -r requirements.txt
```

### Start
```shell
$ python3 app.py
```

# How to use

## GUI
```shell
https://hk-holiday-api.herokuapp.com
```
## Post (e.g. the public holiday of 2009)
### Note that the minimum year is 2007 provided by HK gov

### cURL
```shell
$ curl --location --request POST 'https://hk-holiday-api.herokuapp.com/post_submit' \
--header 'Content-Type: application/json' \
--data-raw '{
  "yearinput": "2009"
}'
```

### HTTP
```shell
POST /post_submit HTTP/1.1
Host: hk-holiday-api.herokuapp.com
Content-Type: application/json

{
  "yearinput": "2009"
}
```

### Python
```shell
import requests

url = "https://hk-holiday-api.herokuapp.com/post_submit"

payload = "{\r\n  \"yearinput\": \"2009\"\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```

# Response
```shell
{
    "1": {
        "0": "The first day of January",
        "1": "1 January",
        "2": "Thursday"
    },
    "2": {
        "0": "Lunar New Year’s Day",
        "1": "26 January",
        "2": "Monday"
    },
    "3": {
        "0": "The second day of the Lunar New Year",
        "1": "27 January",
        "2": "Tuesday"
    },
    "4": {
        "0": "The third day of the Lunar New Year",
        "1": "28 January",
        "2": "Wednesday"
    },
    "5": {
        "0": "Ching Ming Festival",
        "1": "4 April",
        "2": "Saturday"
    },
    "6": {
        "0": "Good Friday",
        "1": "10 April",
        "2": "Friday"
    },
    "7": {
        "0": "The day following Good Friday",
        "1": "11 April",
        "2": "Saturday"
    },
    "8": {
        "0": "Easter Monday",
        "1": "13 April",
        "2": "Monday"
    },
    "9": {
        "0": "Labour Day",
        "1": "1 May",
        "2": "Friday"
    },
    "10": {
        "0": "The Buddha’s Birthday",
        "1": "2 May",
        "2": "Saturday"
    },
    "11": {
        "0": "Tuen Ng Festival",
        "1": "28 May",
        "2": "Thursday"
    },
    "12": {
        "0": "Hong Kong Special Administrative Region Establishment Day",
        "1": "1 July",
        "2": "Wednesday"
    },
    "13": {
        "0": "National Day",
        "1": "1 October",
        "2": "Thursday"
    },
    "14": {
        "0": "Chinese Mid-Autumn Festival",
        "1": "3 October",
        "2": "Saturday"
    },
    "15": {
        "0": "Chung Yeung Festival",
        "1": "26 October",
        "2": "Monday"
    },
    "16": {
        "0": "Christmas Day",
        "1": "25 December",
        "2": "Friday"
    },
    "17": {
        "0": "The first weekday after Christmas Day",
        "1": "26 December",
        "2": "Saturday"
    }
}
```