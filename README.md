# nd064_C1
 
## <a href="https://www.suse.com/" ><img src="https://www.suse.com/assets/img/suse-white-logo-green.svg" style="float:left; max-width: 80px; display: inline" alt="SUSE"/></a>  
  
  
  
                                                 SUSE Scholarship program Cloud Native Foundations Course 
                                             


  
  
Details on the programme can be found at [SUSE](https://www.suse.com/c/suse-sponsors-300-scholarships-in-cloud-native-education-src/) and [Udacity](https://www.udacity.com/scholarships/suse-cloud-native-foundations-scholarship).
 

## Phase -1

****

**Exercise 01**

Extend the Python Flask application with `/status` and `/metrics` endpoints, considering the following requirements:

   - Both endpoints should return an HTTP 200 status code
    
   - Both endpoints should return a JSON response e.g. `{"user": "admin"}`. (Note: the JSON response can be hardcoded at this stage)
    
   - The `/status` endpoint should return a response similar to this example: result: `OK - healthy`
    
   - The `/metrics` endpoint should return a response similar to this example: `data: {UserCount: 140, UserCountActive: 23}`

Tips: If you get stuck, feel free to check the solution video where detailed operations are demonstrated.


****




**Exercise 02: Application Logging**

Logging is a core factor in increasing the visibility and transparency of an application. When in troubleshooting or debugging scenarios, it is paramount to pin-point the functionality that impacted the service. This exercise will focus on bringing the logging capabilities to an application.

At this stage, you have extended the Hello World application to handle different endpoints. Once an endpoint is reached, a log line should be recorded showcasing this operation.

In this exercise, you need to further develop the Hello World application collect logs, with the following requirements:


   - A log line should be recorded the timestamp and the requested endpoint e.g. `"{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"`
    
   - The logs should be stored in a file with the name `app.log`. Refer to the [logging Python module](https://docs.python.org/3/library/logging.html#logging.basicConfig) for more details.
    
   - Enable the collection of Python logs at the `DEBUG` level. Refer to the [logging Python module](https://docs.python.org/3/library/logging.html#logging.basicConfig) for more details.


Tips: If you get stuck, feel free to check the solution video where detailed operations are demonstrated.

