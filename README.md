# <img align="center" width="50" src="https://raw.githubusercontent.com/paramt/1pt/master/resources/favicon/android-chrome-512x512.png">  [1 Point URL Shortener](https://www.1pt.co)

[![Uptime](https://img.shields.io/uptimerobot/ratio/m782561487-e7e43bdb0203a835e6713721.svg?style=flat-square)](https://status.param.me/782561487)

[![Screenshot](resources/assets/screenshot.png)](https://1pt.co)

**1pt** is a simple-to-use URL shortening service.

# Backend

The API runs on a Flask server [hosted on replit](https://repl.it/@paramt/1ptco-API).

## 🖥️ API

The 1pt.co API is public so anyone can create a shortened URL

Endpoint: `api.1pt.co`

### `/addURL`

**Method: `GET`**

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| `long` | **Required** - The long URL to shorten | `https://www.param.me` |
| `short` | **Optional** - The part after `1pt.co/` that will redirect to your long URL. If this paramter is not provided or the requested short URL is already taken, it will return a random 5-letter string | `param` |

#### Example Response

```json
{
  "status": 201,
  "message": "Added!",
  "short": "param",
  "long": "https://www.param.me"
}
```

With this example [1pt.co/param](https://www.param.me) will redirect to `https://www.param.me`

## 🛈 info.1pt.co
Check out [1pt-co/info.1pt.co](https://github.com/1pt-co/info.1pt.co)

## 🛠️ Self-Host

Self-hosting an instance of 1pt requires setting up the Flask server and the Google Sheets API

1. Set up the Google Sheets API
   - Go to [Google Developer Console](https://console.developers.google.com/apis/dashboard) and create a new project
   - Click <kbd>+ ENABLE APIS AND SERVICES</kbd> and enable the "Drive API" as well as the "Sheets API"
   - Navigate to "APIs and Services" > "Credentials"
   - Click <kbd>+ CREATE CREDENTIALS</kbd> and select "Service account"
   - Fill in the required fields, press <kbd>CREATE</kbd>, <kbd>CONTINUE</kbd>, and on the last step click <kbd>+ CREATE KEY</kbd> to download a JSON file
1. Set up the Python server

   - Fork the [1pt.co replit](https://repl.it/@paramt/1ptco-API)
   - Create a file named `.env` and create the following environment variables:

   ```
   SHEET_TYPE=""

   SHEET_PROJECT_ID=""

   SHEET_PRIVATE_KEY_ID=""

   SHEET_PRIVATE_KEY=""

   SHEET_CLIENT_EMAIL=""

   SHEET_CLIENT_ID=""

   SHEET_AUTH_URI=""

   SHEET_TOKEN_URI=""

   SHEET_AUTH_PROVIDER_X509_CERT_URL=""

   SHEET_CLIENT_X509_CERT_URL=""
   ```

   - Copy this [1pt.co Database Template sheet](https://docs.google.com/spreadsheets/d/16y5nLdXFVbmRG3jdzJsa0TOHEbyskc6AQdyhFzKjXto/copy) and share it with the `client_email` found in the JSON file with all the credentials

   - In `config.py` change the value of `spreadsheet` to the name of your Google Sheet

   - Run your repl.it and set it to be **always on**

   > 📝 Note: This requires the [Replit Hacker Plan](https://repl.it/site/pricing). Without the **always on** feature, the server will sleep after 1 hour of inactivity.

-----
###### This project is maintained by [Param Thakkar](https://www.param.me)
