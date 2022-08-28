# Dream-Catcher-Licenta

# Abstract
The final project is a software application made for the Linux platform. This solution is independent from the operating system distribution installed on the host computer. The main target that the application means to reach is the full control of  another targeted machine, by doing reconnaissance work and collecting data with which you can launch a phishing attack. The graphical user interface is made with the help of the Qt platform, keeping in mind to make it as modern as possible. The backend was written in Python and the connection with the frontend was made by working with threads to keep the application as fluid as possible. 

The possible chain of events inside the application gives a walkthrough to the user and aims to keep him engaged following a specific set of actions to reach its final goal. Inside the application  the user can try breaking a WI-FI network using a dictionary attack in three different ways. They can launch a reconnaissance session by scanning the target domain and finding the exposed ports and its information. Another recon functionality is crawling the domain with the help of a spyder to gather all the emails and phone numbers exposed all  throughout the domain and its anchors and references. Having gathered all the information the application can launch a phishing attack on the found email addresses. The contents of the email is written by the user, at the end of the body a link will be automatically attached with a malware. Once downloaded the malware and opening it, a reverse shell connection will be established and the user will gain full control of the target machine. The malware is made for the Windows operating system and it is masked as a generic pop-up error. 

The project touches different areas of security in the context of technology information, notions like: cyber attacks, phishing, crawlers, scrapers, port scanning, WI-FI cracking, creating a server and malware and reverse shell scripting. 

# Gallery

<p align="center">
  <img src="https://user-images.githubusercontent.com/48451382/187082883-dc2262d5-1b2a-4f2f-ac44-4765e5efe62e.png">
  </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/48451382/187082917-a24fce2c-e344-4e58-b893-9b64e849ef3d.png">
  </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/48451382/187082959-f65cea08-d152-44bb-9c1b-35fbde9e041a.png">
  </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/48451382/187082966-0bd4c8ec-6e88-4dbe-9bb4-3ad6125175c8.png">
</p>

# Full Documentation

Below is atached a link to the full documentation of the project as well as motivation. Currently it is only in romanian as it served as my thesis for my bachelor`s degree.

[Click here](https://docs.google.com/document/d/1xEujz7jJFOYVghZMrOUleTg1wP7vuUGzFTs5qK9ECsg/edit?usp=sharing)
