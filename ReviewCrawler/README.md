# Crawler

## Step1: get id
1.1 Use Enterprise Partner Feed Relational (EPF)

```
entry:
   https://feeds.itunes.apple.com/

document:
   https://affiliate.itunes.apple.com/resources/documentation/itunes-enterprise-partner-feed/
   https://affiliate.itunes.apple.com/resources/documentation/getting-started/
   http://resources.organicfruitapps.com/blog/best-way-to-search-for-content/
   http://resources.organicfruitapps.com/documentation/itunes-enterprise-partner-feed/
```

1.2 Deprecated scheme (Use search api to get IDs)

```
https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
e.g., 
https://itunes.apple.com/search?term=productivity&country=us&media=software&limit=20
```
 
## Step2. Use http analyzer to get review data

```request
https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=989673964&displayable-kind=11&startIndex=0&endIndex=100&sort=1&appVersion=current
```

```json
Host:itunes.apple.com  
User-Agent:iTunes/12.5.5 (Windows; Microsoft Windows 10.0 x64 (Build 18363); x64) AppleWebKit/7602.2015.0.18  
Accept:*/*  
Referer:https://apps.apple.com/cn/app/%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80/id989673964?l=en  
Cookie:amia-16975256008=ghQllL+JsE2DDmwr3SZMwn5RjO4raijUVYYnWxr0b0C6LZwvdFl4ZvTGUJRjLX7AT2zmLM3Us9aVPCAhfeXVSg==; amp=WyJPyxxjHcPrL+6RFbwpvpo6U8CMfwmOuQO4LAbviI1j01OXLEue2+tqZ6KUjD/ozxXdVrX7szTAnwGG3jj9PXxazlKncRlUP6W6MS1H4ro=; mt-asn-16975256008=2; mt-tkn-16975256008=AiqKNYupiJboU3LfQlq6dhQlbaF9SMB6sEcM8mO8Khc9aFymVxW+lnv9ssqF+twK65cMXo4n1BHtFUiEfrUnhTv7oDP8vnakcw/KRPA5IrgbGs0q282bTXY8oZKXrEFp/qlVllhmnzZusKsgTBDErsje6TRMLsMhjoUKT+IMWeeICeRt8NN8jfxL2oBgtSa+PTXDMJ8=; mt-tkn-16248681244=AlVXNFneLLzcly/8ofW/DX8UpQH02i5Nm09rKdGeR2bROM74xvF3RHB/XQH0XQyMG0rZkdH1KhzQXL+OXW0b0Zg/ZULSDJNktSJBFfX4tVToFRGf8ij0AqfH/0ZX8EVXsyK2lEivOkfpNMr6gXBpXyu6gPAnSvRaVRV2R7oZZoycN5ugw98pJrXLkobW5oD+m62NZgs=; ns-mzf-inst=180-22-443-116-233-9004-3700208-70-mr23; mzf_in=3700208; xp_ab=1#WqjkRLH+-2+p9nsgcq0#yNFpB6B+-2+o1DRnZi00; xp_abc=p9nsgcq0; xp_ci=3z35DdWHzG6yz4kfzAqNzZ11aJIE0; itspod=70; vrep=CMizt54_EgQIBhAAEgQIDRAAEgQIAhAAEgQIBxAAEgQIBBAAEgQIARAAEgQIAxAAEgQICRAAEgQICBAAEgQIChAAEgQICxAAEgQIDBAAEgQIBRAA; mz_at0-16975256008=AwQAAAECAAHWuQAAAABgSeVowGf4rDpvXy319jTTUHsL4CO7FRA=; mz_at_ssl-16975256008=AwUAAAECAAHWuQAAAABgSeVoMqJObT9ZPDWGiy0dM+chSgclcIw=; pldfltcid=53693a5e34f54acaa78a62b3456645b1070; X-Dsid=16975256008; mz_at0-16248681244=AwQAAAECAAHWtgAAAABgPvyU9aUF0cPJzRAVb38EcegK/qREfkY=; mz_at_ssl-16248681244=AwUAAAECAAHWtgAAAABgPvyUlM3yKq4u1XDaiszn3BQMw3+Z9oI=  
Accept-Language:en-us  
Origin:https://apps.apple.com  
X-Apple-I-MD-RINFO:50660608  
X-Apple-Store-Front:143465-2,32  
X-Dsid:16975256008  
X-Apple-Tz:28800  
X-Apple-I-MD:AAAABQAAABDDxjiw0VsRxrk+IssaEsTAAAAAAg==  
X-Apple-I-MD-M:rmeE0zWT034YBBYznnTujGExviSADdD1RMyil6Hn5nzYfVlF106v1WBTZbtftxhelrkNYNcBn8lfm6JF  
Connection:keep-alive  
Accept-Encoding:gzip, deflate
```
