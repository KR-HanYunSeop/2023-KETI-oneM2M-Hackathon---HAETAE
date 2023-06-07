# 2023-KETI-oneM2M-Hackathon-HAETAE
## Storm Drain monitoring service using oneM2M

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597349/_VNBJWI8nvo.blob?auto=compress%2Cformat&w=900&h=675&fit=min"></p>

---

### Team : HAETAE

'HAETAE' is a legendary Korean animal that controls water.It was designed to create a product that can control the huge natural disaster of flooding.

### Problem

The record heavy rain that occurred around August 2022 exceeded the capacity of the city's drainage system design. Accordingly, the Seoul Metropolitan Government announced plans to increase the capacity of the drainage system and install several large-scale rainwater storage and drainage facilities.According to a news report eight months ago, in addition to the large-capacity facilities, the rainwater basin on the side of the road was full of garbage, so it did not play its role properly and even conducted related experiments.

There are many reasons for flooding, but garbage is buried or blocked in the "storm drain" which basically drains accumulated water, so proper drainage is not achieved.The reasons for poor rainwater management are as follows.Basically, there is a huge amount of rainwater catch and no system to control it.There is no system for continuous monitoring and interaction of rainwater basins through sensors.

### The presentation of a solution

We propose a monitoring service that can manage, maintain, and repair storm drain in Seoul (or certain areas).It detects odors, water levels, camera in real time using IoT devices.Communicate information using the MOBIUS platform if a certain level of sensing value or higher is obtained.A camera 'subscribing' each sensor (MOBIUS function) takes a picture of a rainwater trap.It is handed over to the server, and the server periodically checks the status of the rainwater catch through the web page.

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597345/image_HTghUcO0fy.png?auto=compress%2Cformat&w=740&h=555&fit=max"></p>

### Scenario

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597329/image_3bNNv5rlhX.png?auto=compress%2Cformat&w=740&h=555&fit=max"></p>

The picture above shows a service scenario.The sensor checks the condition of the storm drain at all times (with arduino/sensor).In the event of heavy rain forecast or odor detection, request rainwater management/monitoring to the server, respectively.When forecasting heavy rain, the manager monitors the condition of the storm drain and takes preventive measures.When odor is detected, request and take action to monitor the condition of the storm drain.The scenario described above is aimed at facilitating the management of rainwater collectors more effectively than the current method.

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597401/-_extuo2BIRX.png?auto=compress%2Cformat&w=740&h=555&fit=max"></p>

To enable sensing and perform computations, an Arduino board was connected to a Raspberry Pi via serial communication. The MOBIUS server was utilized as the server for data transmission.The protocols used HTTP and MQTT protocols, which are part of the oneM2M protocol.HTTP was used to upload and import data, and MQTT was used for subscriptions.The POST method was used to upload data, and the GET method was used to retrieve data periodically. In addition, subscription was used to receive data asynchronously.Due to the nature of using the camera, File Transfer Protocol (FTP) was available, but I simply wanted to byteize the image, load it on Mobius, and drag it from the server and save the picture (HTTP).

### Used oneM2M Function

- Application and service layer management: AE, CSE management functions
- Communication management: Provides communication with other CSEs, AEs, and NSEs
- Data management: Data storage and arbitration capabilities
- Subscription and Notification: Provides subscriptions and corresponding notifications to track events occurring on a resource

### Resource Structure

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597398/image_0yylBRyndV.png?auto=compress%2Cformat&w=740&h=555&fit=max"></p>

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597400/_2023-06-03__10_56_49_bOUcsqgKSG.png?auto=compress%2Cformat&w=740&h=555&fit=max"></p>

### System Architecture

Connect Arduino Mega and Raspberry Pi 4 via serial communication.In Arduino, an operation for sensing values and event situation detection was conducted, and the odor threshold and the water level threshold were set through tests.It is judged that drainage does not proceed as it is recognized that the odor caused by foreign substances has occurred when the odor and water level to the degree of exceeding the threshold are generated.Serial communication sends signals to raspberry pi 4 in the rain pits.The Raspberry Pi continuously reads values from the Arduino and triggers an abnormal state when values are transmitted. Information from the gas sensor is sent as gas(CNT) and information from the water level sensor is sent as water(CNT) using the POST method.

Each CNT(gas and water) is subscribed to by the AE. When data is received in the gas(CNT) or water(CNT) the camera starts capturing images.

The captured images are converted into bytes and uploaded to the camera(CNT) using the POST method.

The server (MOBIUS Ubuntu Server) executes Python code when buttons are pressed on the web page to retrieve the camera byte information stored in MOBIUS using the GET method.

The retrieved byte information is decoded and stored on the server.

Users (administrators) can use the web page to maintain, repair, and monitor the status of the rainwater collector in real-time or when abnormal situations are detected.

- Gas Sensor / Camera Operation

<p align="center"><img src="https://hackster.imgix.net/uploads/attachments/1597592/___Cqq8KRu5TL.gif?auto=compress&gifq=35&w=740&h=555&fit=max&fm=mp4"></p>
