''' modules is a code that is written by someone else so just import modules and use it to your project that's it 
'''
# Built-in module use: math
import math

print("Square root of 25 is:", math.sqrt(25))
print("Value of pi is:", math.pi)




import requests
response = requests.get("https://api.github.com")
print("Status code from GitHub API:", response.status_code)

# output        menaing
#  200          ✅ Success – OK  
#  404          ❌ Not Found     
#  500          ⚠️ Server Error 
