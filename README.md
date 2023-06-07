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

