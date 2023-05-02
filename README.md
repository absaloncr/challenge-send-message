# challenge-send-message

This application corresponds to a Rest API built in the python language, which responds to the HTTP POST request method, it requires the following headers to be sent in the request:

1. **X-Parse-REST-API-Key** with a value of **"2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"** , if this header is not sent, send it with an empty value or different from the one indicated, the response will be an error.
2. **X-JWT-KWY** the value varies in each request, but if the header is not sent, the response will be an error.
3. **Content-Type** with value "application/json"

The body of the request must refer to the following payload: </br> **{ “message” : “This is a test”, “to”: “Juan Perez”, “from”: “Rita Asturia”, “timeToLifeSec” : 45}**

All fields are required, so the response will be an error if any are missing.

The response payload in case the request header and body are sent correctly and complete will be the following: </br> **{ “message” : “Hello Juan Perez your message, will be sent” }**
 
# TESTING
## <sub>  local tests </sub>

To locally test the code you must follow the following steps:

1. Install Python3 if you don't have it and set up the development environment for the language in your IDE
2. Run a pull of the code from the repository in your local environment (git clone https://github.com/absaloncr/challenge-send-message.git)
3. Install the requirements indicated in the .txt document (**Flask and Pytest**)
4. Run the command **python -m flask run** to start the web server built into Flask
5. Proceed to test the API using a tool like postman or the curl command in your terminal as follows:

```
curl -X POST -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "X-JWT-KWY: Bearer" -H "Content-Type: application/json" -d "{\"message\": \"This is a test\", \"to\": \"Juan Perez\", \"from\": \"Rita Asturia\", \"timeToLifeSec\": 45}" ${LocalDir}/DevOps

```
**Note**: Remember to replace ${LocalDir} with your domain and local port (localhost:5000)

## <sub> Unit Test </sub>

The execution of the tests is executed with the pytest command, this immediately recognizes the test directories and files and uses them to launch the tests, in the /test directory we will find the test file that will be checked when launching the command **pytests -v**

## <sub> Online Test</sub>

To run the online test of the services already set up in an EKS in AWS, we can use the curl command again as follows: </br>
```
curl -X POST -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "X-JWT-KWY: Bearer" -H "Content-Type: application/json" -d "{\"message\": \"This is a test\", \"to\": \"Juan Perez\", \"from\": \"Rita Asturia\", \"timeToLifeSec\": 45}" http://a4f5893fa75e24feaaca63fc93af17f4-767562501.us-east-1.elb.amazonaws.com/DevOps

```

or use a tool like postman but using the following domain and corresponding endpoint **http://a4f5893fa75e24feaaca63fc93af17f4-767562501.us-east-1.elb.amazonaws.com/DevOps**

# CI/CD

For the integration and continuous Deployment we made use of GitHub Workflows with the necessary steps for the construction, testing and automated deployment of the application in **AWS EKS.**

![image](https://user-images.githubusercontent.com/132222221/235549571-49561688-1a81-4406-80cb-5cb2b03d5bfe.png)

## In general, the steps allow:

- 1 get project code </br>
- 2 Set the python version </br>
- 3 Updated pip to avoid deprecation error </br>
- 4 and 5 we add the **FLASK AND PYTEST packages** (we can reduce to 1 single step) </br>
- 6 We run the unit tests </br>
- 7 We log in to AWS using our keys duly set in **GitHub Secrets**, in order to be able to connect to our AWS account. </br>
- 8, 9 and 10 We **build the docker image**, set the docker hub credentials (login process) and upload the image to our public repository in order to use it for the creation of our pods during the deployment in EKS. </br>
- 11 Launch the **deploy in EKS** for the creation of pods based on the published image, creation of the balancer and subsequent creation of the nodes. (IAC file deploy.yml)</br>

Note: The workflow build file is located in the following path: /.github/workflows/

# License

Copyright © 2023 Absalon Cedeño. All rights reserved.

