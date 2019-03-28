# Serverless Email attatchment parser

##To create a deployment package

1.Create a folder (examplefolder), and then create a subfolder (node_modules).

2.Install the Node.js platform. For more information, see the Node.js website.

3.Install dependencies. The code uses the following libraries:

  AWS SDK for JavaScript in Node.js
  Async utility module
  mailparser

The AWS Lambda runtime already has the AWS SDK for JavaScript in Node.js, so you only need to install the other libraries. Open a command prompt, navigate to the examplefolder, and install the libraries using the npm command, which is part of Node.js.

```
npm install async mailparser
```

copy paste the json from sampletest.json to the lambda function test case.


# Test Code
Run test.py
Source Bucket : inbox-bucket-test
Destination Bucket : inbox-bucket-testresized
