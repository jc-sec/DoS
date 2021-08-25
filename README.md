<h1 align="center">DoS</h1>
<p align="center">Tool made for educational purposes!</p>
<p align="center">by Hes</p>
<br>
<img src="https://user-images.githubusercontent.com/84875618/130705580-d34957d5-fa68-49f3-8e4a-d2fc8d70c973.png" width="550" height="370">

### ```Usage```

```
Simple:
  python3 dos.py -u localhost --mode tcp/udp

Advanced:
  python3 dos.py -u localhost -p 8080 -r 50000 -d 0.01 -v --mode tcp  
```

### ```Flags``` :triangular_flag_on_post:

```  
  Optional:
  
  -r, --requests | Number of requests
  -p, --port | Target port <int> DEFAULT: 80
  -v, --verbose | Verbose mode
  -d, --delay | Delay between each request <float> DEFAULT: 0.03
  -u, --url | Target IP/URL 

  Required:
  
  -u, --url | Target IP/URL
  --mode {tcp/udp} | Attack mode
```

###  ```Requirements```
  ```pip3 install colorama==0.4.3```

### ```Download```

  ``` 
  - https://github.com/jc-sec/DoS.git
  
  - https://github.com/jc-sec/DoS/archive/refs/heads/main.zip
  ```
