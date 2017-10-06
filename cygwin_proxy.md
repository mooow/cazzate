# Cheatsheet configurazione di cygwin dietro un Proxy su Windows
## Fanculo il Poli che vuole bloccare sempre tutto!
* Comando PowerShell: `[System.Net.WebProxy]::GetDefaultProxy() | select address`
* Impostare proxy su cygwin: `export http_proxy = "http://<proxy>:<port>"`
